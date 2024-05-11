from django.db import models
from datetime import date
from django.contrib.auth.models import User
from django.utils import timezone
#?table categorie
class Categorie (models.Model):
    TYPE_CHOICES = [('Alimentaire','Alimentaire'),('Meuble','Meuble'),('Sanitaire','Sanitaire'),('Vaisselle','Vaisselle'),
                    ('Vetement','Vetement'),('Jouets','Jouets'),('Ligne de Maison','Ligne de Maison'),('Bijoux','Bijoux'),('Decor','Decor'),
                    ('Immobilier','Immobilier'),('ParaPharmacie','ParaPharmacie'),('Electroménager','Electroménager'),
                    ('Tapis','Tapis'),('Frais','Frais')]
    
    name=models.CharField(max_length=50,choices=TYPE_CHOICES,default='Al')

    def __str__(self):
        return self.name
    
#? table Fournisseur 
class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField(default = ' ')
    email=models.EmailField(default = ' ')
    telephone=models.CharField (max_length=8)
    def __str__(self):
        return f"{self.nom} {self.adresse} {self.email} {str(self.telephone)}"
    
#? table produit 
class Produit (models.Model):
    libelle=models.CharField(max_length=100)
    description=models.TextField()
    prix=models.FloatField()
    quantite_en_stock = models.IntegerField(default=0)
    TYPE_CHOICES=[('em','emballé'),('fr','Frais'),('cs','Conserve')]
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    img=models.ImageField(blank=True)

    def __str__(self) :
        return f"{self.libelle} - {self.description} - {self.prix} - {self.type}"
    

    #?association many to one avec table categorie
    categorie = models.ForeignKey(Categorie, on_delete=models.CASCADE,null=True)

    #?association many to one avec table fournisseur
    fournisseur=models.ForeignKey(Fournisseur,on_delete=models.CASCADE,null=True)
#--------------------------------
class ModificationQuantiteStock(models.Model):
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE)
    ancienne_quantite = models.IntegerField()
    nouvelle_quantite = models.IntegerField()
    def __str__(self):
        return f"{self.id} {self.ancienne_quantite}  {self.nouvelle_quantite}"
    
from django.db.models.signals import post_save
from django.dispatch import receiver
@receiver(post_save, sender=ModificationQuantiteStock)
def verifier_quantite_en_stock(sender, instance, **kwargs):
    if instance.nouvelle_quantite == 0:
        # Si la nouvelle quantité est égale à 0, supprimez le produit
        instance.produit.delete()


#? class produit non  consommable
class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)
    def __str__(self):
        return self.__str__()+' '+self.Duree_garantie

#? class commande
class Commande(models.Model):
    dateCde = models.DateField(null=True, default=date.today)
    totaleCde = models.DecimalField(default=0.0, max_digits=10, decimal_places=2)
    qte = models.IntegerField(default=1)
    user= models.ForeignKey(User, on_delete= models.CASCADE, null=True)

    #* Many-to-Many association with Produit
    produit = models.ManyToManyField(Produit)
    
    def __str__(self):
        return f"{self.dateCde.strftime('%Y-%m-%d')} - {self.totaleCde}"
    
    

    
    
