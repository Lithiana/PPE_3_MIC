from django.db import models
from django.contrib.auth.models import User

class categorie(models.Model): 
    NOM_CAT = models.CharField(max_length=30)

class Role(models.Model): 
    TYPE_ROLE = models.CharField(max_length=15)

class Client(models.Model):
    CIVILITE = models.CharField(max_length=3)
    NOM = models.CharField(max_length=255)
    PRENOM = models.CharField(max_length=255)
    NUM_TEL = models.CharField(max_length=10)
    ADR_MAIL = models.CharField(max_length=255)
    USER_SESSION = models.CharField(null=True, max_length=500)

class Commande(models.Model):
    CLIENT = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    DATE_COMMANDE = models.DateField

class Compte(models.Model):
    MDP_COMPTE = models.CharField(max_length=32)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

class etat(models.Model): 
    STATUT = models.CharField(max_length=20) 

class Produit (models.Model): 
    NOM_PRODUIT = models.CharField(max_length=30)
    DESCRIPTION = models.CharField(max_length=400)
    QUANTITEE_STOCK = models.IntegerField(default=0)
    HAUTEUR_PRODUIT = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2) 
    LARGEUR_PRODUIT = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2) 
    POID_PRODUIT = models.IntegerField(default=0)
    categorie = models.ForeignKey(categorie, on_delete=models.CASCADE, null=True)
    PRIX_PRODUIT = models.DecimalField(blank=True, null=True, max_digits=8, decimal_places=2) 

class livraison(models.Model): 
    NOM_LIVRAISON = models.CharField(max_length=30)
    TRANSPORTEUR = models.CharField(max_length=30)
    DUREE_LIV = models.IntegerField(default=0)

class paiement(models.Model): 
    TYPE = models.CharField(max_length=30)

class adresse(models.Model): 
    ADRESSE = models.CharField(max_length=255)
    CODE_P  = models.CharField(max_length=5)
    VILLE = models.CharField(max_length=30)
    PAYS = models.CharField(max_length=30)
    CLIENT = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    livraison = models.ForeignKey(livraison, on_delete=models.CASCADE, null=True)  

class produit_commande (models.Model):
    QT_PRODUIT = models.IntegerField(default=0)
    Commande = models.ForeignKey(Commande, on_delete=models.CASCADE,null = True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)  

    
