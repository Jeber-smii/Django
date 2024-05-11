from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'slug', 'content', 'status', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'title-class'}),
            'slug': forms.TextInput(attrs={'class': 'slug-class'}),
            'content': forms.TextInput(attrs={'class': 'content-class'}),
            'status': forms.Select(attrs={'class': 'status-class'}),
            'image': forms.FileInput(attrs={'class': 'image-class'}),
        }
