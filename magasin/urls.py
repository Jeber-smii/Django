from django.urls import path,include
from . import views
from .views import CategoryAPIView , ProduitAPIView,ProduitViewset



urlpatterns = [
    #path('',views.index,name='index'),

    
    #*------------------------Produit-------------------------------
    path('',views.affProduit,name='produit'),
    path('ajouterProduit/',views.addProduct, name='AddP'),
    path('editP/<int:id>',views.editp, name='editp'),
    path('deleteP/<int:id>',views.deletp, name='deletep'),
    path('vitrine/',views.vitrine),


    #*------------------------Fournisseur---------------------------
    path('fournisseur/',views.affFournisseur,name='listFourinsseur'),
    path('ajouterFournisseur/',views.addFournisseur, name='AddF'),
    path('deleteFournisseur/<int:idf>/' ,views.deletef,name ='deletef'),
    path('editFournissuer/<int:idf>/',views.editf,name='EditF'),
    #path('redirect/<int:idf>/',views.redirectf,name='redirectf'),


    #*-------------------------Commande-----------------------------
    path('NewCommande/<int:idp>', views.newCommande, name='NewCommande'),
    path('delete/<int:commande_id>/', views.deleteCommande, name='delete_commande'),

    #*-------------------------------------------------------------
    path('register/',views.register, name = 'register'),

    #*-----------------------------API------------------------------
    path('api/category/',CategoryAPIView.as_view()),
    path('api/produit/',ProduitAPIView.as_view()),

    #*-------------
    path('blog/', include('blog.urls')),
    #*--------------- profile
    path('profile/', views.profile,name='profile'),
]

