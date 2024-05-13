from django.shortcuts import render,get_object_or_404,redirect
from django.template import loader
from django.http import HttpResponseRedirect
from .models import Produit,Fournisseur,Commande,Categorie,ModificationQuantiteStock
from .forms import ProduitForm,FournisseurForm,CommandeForm,UserCreationForm
from decimal import Decimal ,InvalidOperation
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate 
from django.contrib import messages
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import CategorySerializer,ProduitSerializer

from  rest_framework import viewsets

from django.db.models import Q
#*---------------------------API-----------------------

class CategoryAPIView(APIView):
    def get(self, *args,**kwargs):
        categories= Categorie.objects.all()
        serializer = CategorySerializer(categories,many=True)
        return Response(serializer.data)
    
class ProduitAPIView(APIView):
    def get(self,*args,**kwargs):
        produits = Produit.objects.all()
        serializer = ProduitSerializer(produits,many=True)
        return Response(serializer.data)
#*------------------------
class ProduitViewset(viewsets.ReadOnlyModelViewSet):
    serializer_class=ProduitSerializer
    def get_queryset(self):
        queryset = Produit.objects.all()
        category_id = self.request.GET.get('category_id')
        if category_id:
            queryset = queryset.filter(categorie_id=category_id)
        return queryset


#*----------------------------normal--------------------
def register(request) :
    if request.method == 'POST' : 
        form = UserCreationForm(request.POST) 
        if form.is_valid(): 
            form.save()   
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password1') 
            user = authenticate(username=username, password=password) 
            login(request,user)  
            messages.success(request, f'Coucou {username}, Votre compte a été créé avec succès !') 
            return redirect('home')
    else :
        form = UserCreationForm()
    return render(request,'registration/register.html',{'form' : form})

#!index test
@login_required
def index(request):
    return render(request,'magasin/base.html')
@login_required
#!affichage de produit
def affProduit(request): 
    if request.method =="GET":
        query = request.GET.get('q')
        results = None
        if query:
        # Perform the search query using your model
            results = Produit.objects.filter(Q(libelle__icontains=query) | Q(description__icontains=query))
            return render( request,'mysite/mesProduits.html ',{'products':results} )
    template=loader.get_template('mysite/mesProduits.html')
    products= Produit.objects.all()

    return render( request,'mysite/mesProduits.html ',{'products':products} )

@login_required
#!function add product
def addProduct(request):
    if request.method == "POST":
        lib = request.POST.get('libelle')
        desc = request.POST.get('description')
        prix_str = request.POST.get('prix')
        typ = request.POST.get('type')
        img = request.FILES.get('img')
        error_message = None
        try:
            prix_dec = Decimal(prix_str)
        except InvalidOperation:
            error_message = f"Invalid price format: '{prix_str}'. Please enter a valid decimal number."
            return render(request, 'magasin/majProduits.html', {'error_message': error_message})

        produit = Produit.objects.create(libelle=lib, description=desc, prix=prix_dec, type=typ, img=img)
        produit.save()
        
        #return HttpResponseRedirect('/magasin/majProduits.html')
        return redirect('produit')
    return render(request, 'magasin/majProduits.html')
@login_required
def deletp(request,id):
    p=Produit.objects.get(id=id)
    p.delete()
    return redirect('produit')
@login_required
def editp(request,id):
    
    if request.method=='GET':
        produit=Produit.objects.get(id=id)
        return render(request,'magasin/editp.html',{'produit':produit})
    if request.method=='POST':
        produit=Produit.objects.get(id=id)
        libelle = request.POST.get('libelle')
        description = request.POST.get('description')
        type = request.POST.get('type')
        quantite_en_stock=request.POST.get('qte')
        prix = float(request.POST.get('prix'))

        produit.libelle=libelle
        produit.description=description
        produit.type=type
        produit.img=produit.img
        produit.quantite_en_stock=quantite_en_stock
        produit.prix=prix
        produit.save()
        
        return redirect('produit')
    return render (request,'magasin/editp.html',{'produit':produit})
    




@login_required
#!affichage vitrine
def vitrine(request):
    list=Produit.objects.all() 
    return render(request,'magasin/vitrine.html',{'list':list}) 

#*--------------------------------------------------------fournisseur-----------------------------------
#!affichage de fornisseur
@login_required
def affFournisseur(request):
    action = 'add'
    if request.method =="GET":
        query = request.GET.get('q')
        results = None
        if query:
        # Perform the search query using your model
            results = Fournisseur.objects.filter(Q(nom__icontains=query) | Q(adresse__icontains=query)| Q(email__icontains=query)| Q(telephone__icontains=query))
            return render (request,'magasin/listFournisseur.html',{'listF':results,'action':action})

    listF=Fournisseur.objects.all()
    return render (request,'magasin/listFournisseur.html',{'listF':listF,'action':action})

#!add fournisseur
@login_required
def addFournisseur(request):
    action = 'add'
    listF=Fournisseur.objects.all()
    if request.method == 'POST':
        nom = request.POST.get('name')
        adresse = request.POST.get('adresse')
        email = request.POST.get('email')
        telephone = request.POST.get('phone')
        fournisseur = Fournisseur.objects.create(nom=nom, adresse=adresse, email=email, telephone=telephone)
        fournisseur.save()
        return redirect('listFourinsseur')
    
    return render (request,'magasin/listFournisseur.html',{'listF':listF,'action':action})
#! delete fornisseur
@login_required
def deletef(request,idf):
    if request.method =='POST':
        fournisseur=Fournisseur.objects.get(id=idf)
        fournisseur.delete()
        return redirect('listFourinsseur')
#!edit fournisseur
@login_required
def editf(request,idf):
    action='update'
    listF = Fournisseur.objects.all()
    if request.method=='GET':
       four=Fournisseur.objects.get(id=idf)
       return render (request,'magasin/listFournisseur.html',{'listF':listF , 'four': four,'action':action}) 

    if request.method=='POST':
        four=Fournisseur.objects.get(id=idf)
        four.nom=request.POST.get('name')
        four.adresse=request.POST.get('adresse')
        four.email=request.POST.get('email')
        four.telephone=request.POST.get('phone')

        four.save()
        return redirect('listFourinsseur')
    return render (request,'magasin/listFournisseur.html',{'listF':listF , 'four': four,'action':action})



@login_required
#!add commande
def newCommande(request,idp):
    if request.method == 'POST':
        qte=int(request.POST.get('qte'))
        
        pd=Produit.objects.get(id=idp)
        alert_message = None
    
        if qte > pd.quantite_en_stock :
            alert_message = "Alert: Quantity exceeds available stock!"
            return render(request, 'magasin/errorpage.html', {'alert_message': alert_message})
        else :
            totale = qte*pd.prix
            commande=Commande.objects.create(
                totaleCde=totale,
                qte=qte,
                user= request.user
            )
            #commande.produit.set(pd)
            commande.produit.set([pd])
            commande.save()
            pd.quantite_en_stock=pd.quantite_en_stock-qte
            pd.save()
            ModificationQteStock= ModificationQuantiteStock.objects.create(
                produit=pd,
                ancienne_quantite=pd.quantite_en_stock+qte,
                nouvelle_quantite=pd.quantite_en_stock
            )
            

            return redirect('produit')
        
    else:
        return redirect('produit')
@login_required
def deleteCommande(request, commande_id):
    commande = get_object_or_404(Commande, pk=commande_id)
    commande.delete()
    return redirect('profile')

@login_required
def profile(request):
    comds=Commande.objects.filter(user=request.user)
    
    return render(request,'magasin/profile.html', {'commands':comds})
