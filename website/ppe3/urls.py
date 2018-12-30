from django.urls import path
from django.contrib import admin
from django.urls import path, include
from . import views

#1 argument = fragment d'url / 2 eme = vue du fichier views.py

urlpatterns = [

    #----------Les pages WEB --------------------
    #--------------------------------------------

    path('index', views.index, name='index'), #premier argument vide = home page
    path('', views.index, name = 'home'),
    path('produits', views.produits, name='produits' ),
    path('produit/<int:id_produit>', views.details_produit, name='details'),
    path('a-propos', views.a_propos, name ='a-propos'),
    path('contact', views.contact, name ='contact'), 
    path('mentions-legales', views.mentions_legales, name = 'mentions-legales'),
    path('authentification', views.authentification, name='authentification'),

    #-----------------AUTRE-----------------------
    #---------------------------------------------

    path('admin/', admin.site.urls),
    path('success/', views.successView, name='success'),

    #---------------PANIER DACHAT-----------------
    #---------------------------------------------

    path('panier', views.panier, name='panier'), 
    path('produit/ajouter/<int:id_produit>', views.ajouter_panier, name='ajouter_panier'),
    path('panier/supprimer/<int:id_produit>', views.supprimer_produit, name='supprimer_panier'),
    path('panier/<str:method>/<int:id_produit>', views.modifier_quantite, name='modifier_quantite'),
    path('panier/client', views.client, name='client'),
]

