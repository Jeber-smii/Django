from django.shortcuts import render,redirect
from django.template import loader
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.contrib.auth import logout


@login_required
def home(request):
    context={'val':"Menu Acceuil"}
    return render(request,'mysite/home.html',context)

@login_required
def produit_api_view(request):
    data = {'name': 'Product 1', 'price': 10.99}  # Example data
    return JsonResponse(data)
@login_required
def logout_view(request):
    logout(request)
    # Redirigez l'utilisateur vers une page de confirmation de déconnexion ou vers une autre page de votre choix
    #return render(request,'mysite/home.html')
    return redirect('/')