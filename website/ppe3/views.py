from django.shortcuts import render
from django.http import HttpResponse
from ppe3.models import newtable01

# Create your views here.
def index(request):
    t = newtable01()
    t.CODE_POSTAL = '37000'
    t.save()
    return HttpResponse("Nouvelle ligne créée : " + t.CODE_POSTAL)