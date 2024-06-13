from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Authentification import models
from django.db import transaction
from Etudiant.models import EtudiantModels


# Create your views here.
def index (request):
    return render(request,"etudiant/index.html")

def Mes_copies (request):
    
    return render(request,"copie/mes_copies.html")

def Fichier_Personnel (request):
    
    return render(request,"dossier/fichier_personel.html")

def Profil (request):
    
    return render(request,"Profil/etudiant_profil.html")
