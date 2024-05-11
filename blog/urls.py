from django.urls import path
from .views import ListePosts , CreerPost , ModifierPost , SupprimerPost , DetailPost

urlpatterns = [
    path('', ListePosts.as_view(), name='liste_posts'), 
    path('CreerPost', CreerPost.as_view(), name='creer_post'), 
    path('<int:pk>/ModifierPost', ModifierPost.as_view(), name='modifier_post'), 
    path('<int:pk>/SupprimerPost', SupprimerPost.as_view(), name='supprimer_post'), 
    path('<int:pk>/', DetailPost.as_view(), name='detail_post'),
]