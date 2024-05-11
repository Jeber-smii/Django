from django import forms
from .models import Produit,Fournisseur,Commande
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class ProduitForm(forms.ModelForm):
    class Meta:
        model = Produit
        fields = '__all__'

class FournisseurForm(forms.ModelForm):
    class Meta:
        model = Fournisseur
        fields = ["nom", "adresse", "email", "telephone"]
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nom'}),
            'adresse': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresse'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Téléphone'}),
        }


class CommandeForm(forms.ModelForm):
    class Meta:
        model =Commande
        fields =['dateCde','produit']

class UserRegistrationForm(UserCreationForm): 
    first_name = forms.CharField(label='Prenom') 
    last_name = forms.CharField(label='Nom') 
    email = forms.EmailField(label='Adresse e-mail')


class Meta(UserCreationForm.Meta):
    model = User
    fields = UserCreationForm.Meta.fields + ('first_name', 'last_name' , 'email') 
