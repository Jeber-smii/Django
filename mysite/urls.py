"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin ,auth
from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from magasin.views import ProduitViewset, CategoryAPIView
from rest_framework import routers

from .views import logout_view

#*-------
router =routers.SimpleRouter()

#*----------
router.register('produit',ProduitViewset,basename='produit')

urlpatterns = [
    path('',views.home,name ='home'),
    path('admin/', admin.site.urls),
    path('magasin/', include('magasin.urls')),
    path('blog/', include('blog.urls')),
    path('accounts/', include('django.contrib.auth.urls')),
    path('login/',auth_views.LoginView.as_view(template_name='registration/login.html'), name = 'login'),
    path('logout/',logout_view, name ='logout'), 
    path('api-auth/', include('rest_framework.urls')),
    #!--------------
    path('api/', include(router.urls)),
]+static (settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
