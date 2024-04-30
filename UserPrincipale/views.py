from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import Administrateur, Etudiant, Enseignant, Scolarite


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

#Login

def login_page(request):
    if request.method == 'POST':
        # Récupérer les données du formulaire soumis
        matricule = request.POST.get('matricule')
        password = request.POST.get('password')
        
        # Authentifier l'utilisateur en utilisant le matricule
        user = authenticate(request, matricule=matricule, password=password)
        
        if user is not None:
            # Authentification réussie, connecter l'utilisateur
            login(request, user)
            # Redirection vers la page appropriée
            if hasattr(user, 'Etudiant'):
                return redirect('Etudiant:index')
            elif hasattr(user, 'Enseignant'):
                return redirect('Enseignant:index')
            elif hasattr(user, 'Scolarite'):
                return redirect('ScolaritePersonal:index')
            elif hasattr(user, 'Administrateur'):
                return redirect('UserPrincipale:index')
        else:
            # Authentification échouée, renvoyer un message d'erreur
            return render(request, 'login.html', {'error_message': 'Matricule   ,INE ou mot de passe incorrect'})
    
    # Si la méthode HTTP est GET ou si l'authentification échoue
    return render(request, 'login.html')
