from django.contrib import admin


# Register your models here.
from .models import Produit,Categorie,Fournisseur,ProduitNC,Commande,ModificationQuantiteStock
admin.site.register(Produit)
admin.site.register(Categorie)
admin.site.register(Fournisseur)
admin.site.register(ProduitNC)
admin.site.register(Commande)
admin.site.register(ModificationQuantiteStock)