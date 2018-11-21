from django.db import models

# Create your models here.
class newtable01(models.Model):
    CODE_POSTAL = models.CharField(max_length=5)

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

class Commande(models.Model):
    CLIENT = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    DATE_COMMANDE = models.DateField
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

class Compte(models.Model):
    MDP_COMPTE = models.CharField(max_length=32)
    Role = models.ForeignKey(Role, on_delete=models.CASCADE, null=True)

class etat(models.Model): 
    STATUT = models.CharField(max_length=20) 

class Produit (models.Model): 
    NOM_PRODUIT = models.CharField(max_length= 30)
    DESCRIPTION = models.CharField(max_length=400)
    QUANTITEE = models.IntegerField 
    TAILLE_PRODUIT = models.DecimalField 
    POID_PRODUIT = models.DecimalField
    categorie = models.ForeignKey(categorie, on_delete=models.CASCADE, null=True)
    

class livraison(models.Model): 
    NOM_LIVRAISON = models.CharField(max_length=30)
    TRANSPORTEUR = models.CharField(max_length=30)
    DUREE_LIV = models.DecimalField

class paiement(models.Model): 
    TYPE = models.CharField(max_length=30)

class adresse(models.Model): 
    N_VOIRIE = models.CharField(max_length=10)
    VOIRIE = models.CharField(max_length=30)
    NOM_RUE = models.CharField(max_length=255)
    CODE_P  = models.CharField(max_length=5)
    VILLE = models.CharField(max_length=30)
    PAYS = models.CharField(max_length=30)
    CLIENT = models.ForeignKey(Client, on_delete=models.CASCADE, null=True)
    livraison = models.ForeignKey(livraison, on_delete=models.CASCADE, null=True)
    produit = models.ForeignKey(Produit, on_delete=models.CASCADE, null=True)