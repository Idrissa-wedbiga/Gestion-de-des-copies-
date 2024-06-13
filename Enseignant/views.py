from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Enseignant.models import EnseignantModels
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
@login_required(login_url='Authentification:login')
def index (request):

    return render(request,"enseignant/index.html")


def enseigant_profile (request):

    return render(request,"Profil/enseigant_profile.html")

def Composer (request):

    return render(request,"Copie/compos_copie.html")

def Envoyer (request):

    return render(request,"Copie/envoyer_copie.html")

def Corriger (request):
     
    return render(request,"Copie/corriger_copie.html")