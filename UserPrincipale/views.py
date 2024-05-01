from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User



def index(request):

    return render(request, "userprincipale/index.html")

#enseignant
def enseignant(request):

    return render(request, "Enseignant/enseignant.html")

def ajouter(request):
    
    return render(request, "Enseignant/ajouter.html")

def editer(request):
    
    return render(request, "Enseignant/edit.html")


#scolarite
def scolarity(request):

    return render(request, "Scolarite/scolarity.html")

def sc_ajouter(request):

    return render(request, "Scolarite/sc_ajouter.html")

def sc_editer(request):
    
    return render(request, "Scolarite/sc_edit.html")

#user profil
def usersprofile(request):

    return render(request, "Profil/users_profile.html")
