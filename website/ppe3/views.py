from django.shortcuts import render #by default
from django.http import HttpResponse #permet de construire une réponse HTTP
from django.contrib import messages
from django.core.mail import send_mail, BadHeaderError
from django.shortcuts import render, get_object_or_404, redirect #rendu page html (css)
from django.urls import reverse
import random
from .models import Produit, Commande, Client, produit_commande, adresse #import bdd 
from .forms import ContactForm, ClientForm

# ------------------------VIEWS WEB PAGE -----------------------------------------
#---------------------------------------------------------------------------------

def index(request):
    context = {'id':1}
    return render(request, 'ppe3/index.html', context)

def produits(request):
    prod_lst = Produit.objects.all()
    context = {'produits': prod_lst}
    return render(request, 'ppe3/produits.html', context)

def details_produit(request, id_produit):
    p = get_object_or_404(Produit, id=id_produit)
    context = {'produit': p}
    return render(request, 'ppe3/produit.html', context)

def contact(request):
    if request.method == 'GET' : 
        form = ContactForm()
    else : 
        form = ContactForm(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            message = form.cleaned_data ['message']

            try : 
                send_mail(subject, message, from_email, ['caroline.duballet@gmail.com'])
            except BadHeaderError : 
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render (request, "ppe3/Contact.html", {'form' : form})

def a_propos(request):
    context = {'id':1}
    return render(request, 'ppe3/a_propos.html', context)

def authentification(request):
    context = {'id':1}
    return render(request, 'ppe3/authentification.html', context)

def mentions_legales(request):
    context = {'id':1}
    return render(request, 'ppe3/mentions_legales.html', context)

# ------------------------VIEWS FONCTIONNALITEE ----------------------------------
#---------------------------------------------------------------------------------

def successView(request) : 
    return HttpResponse('Envoyé ! Merci de votre message !')

# ------------------------VIEWS PANIER -------------------------------------------
#---------------------------------------------------------------------------------

def ajouter_panier(request, id_produit):
    if 'user_session' in request.session:
        user_session = request.session['user_session']
    else:
        user_session = random.randint(0, 500)

    clt, _ = Client.objects.get_or_create(USER_SESSION=user_session)
    com, _ = Commande.objects.get_or_create(CLIENT=clt)
    prd = get_object_or_404(Produit, id=id_produit)
    prd_com = produit_commande(Commande=com, produit=prd, QT_PRODUIT=1)
    prd_com.save()
    
    request.session['user_session'] = user_session

    messages.info(request, "Article ajouté au panier")
    return redirect(reverse('produits'))

def panier(request): 
    if 'user_session' in request.session:
        user_session = request.session['user_session']
    else:
        user_session = random.randint(0, 500)

    clt, _ = Client.objects.get_or_create(USER_SESSION=user_session)
    com, _ = Commande.objects.get_or_create(CLIENT=clt)
    prd_lst = produit_commande.objects.filter(Commande=com)
    total = sum(p.produit.PRIX_PRODUIT * p.QT_PRODUIT for p in prd_lst)
    context = {'panier': prd_lst, 'total': total}

    return render(request, 'ppe3/panier.html', context)

def modifier_quantite(request, method, id_produit):
    prod = get_object_or_404(produit_commande, id=id_produit)

    if method == 'add':
        prod.QT_PRODUIT += 1
    elif method == 'sub':
        prod.QT_PRODUIT -= 1

    prod.save()
    if prod.QT_PRODUIT == 0:
        prod.delete()

    return redirect(reverse('panier'))

def supprimer_produit(request, id_produit):
    prod = get_object_or_404(produit_commande, id=id_produit)
    prod.delete()

    return redirect(reverse('panier'))

def client(request):
    if request.method == 'GET':
        form = ClientForm()
        return render(request, "ppe3/client.html", {'form' : form})
    else:
        form = ClientForm(request.POST)
        if form.is_valid():
            civ = form.cleaned_data['civilite']
            nom = form.cleaned_data['nom']
            prenom = form.cleaned_data['prenom']
            tel = form.cleaned_data['tel']
            email = form.cleaned_data['email']
            adr = form.cleaned_data['adresse']
            cp = form.cleaned_data['code_postal']
            ville = form.cleaned_data['ville']
            pays = form.cleaned_data['pays']

            user_session = request.session['user_session']
            clt = get_object_or_404(Client, USER_SESSION=user_session)
            clt.CIVILITE = civ
            clt.NOM = nom
            clt.PRENOM = prenom
            clt.NUM_TEL = tel
            clt.ADR_MAIL = email
            clt.save()

            bdd_adr, _ = adresse.objects.get_or_create(CLIENT=clt)
            bdd_adr.ADRESSE = adr
            bdd_adr.CODE_P = cp
            bdd_adr.VILLE = ville
            bdd_adr.PAYS = pays
            bdd_adr.save()

            return render(request, "ppe3/paiement.html")