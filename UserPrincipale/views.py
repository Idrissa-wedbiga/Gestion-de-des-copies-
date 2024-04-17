from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User


def index(request):

    return render(request, "userprincipale/index.html")

def enseignant(request):

    return render(request, "Enseignant/enseignant.html")

def scolarity(request):

    return render(request, "Scolarite/scolarity.html")

def usersprofile(request):

    return render(request, "Profil/users_profile.html")

def ajouter(request):
    
    return render(request, "Enseignant/ajouter.html")

def editer(request):
    
    return render(request, "Enseignant/edit.html")

#Login

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        remember = request.POST.get('remember')

        user = authenticate(request, email=email, password=password)

        if user is not None:
            login(request, user)
            if remember:
                request.session.set_expiry(1209600)  # 2 weeks
            else:
                request.session.set_expiry(0)  # Session expires when browser is closed

            if hasattr(user, 'utilisateur'):
                # Rediriger vers le tableau de bord de l'utilisateur
                return redirect('dashboard_utilisateur')
            elif hasattr(user, 'etudiant'):
                # Rediriger vers le tableau de bord de l'étudiant
                return redirect('dashboard_etudiant')
            elif hasattr(user, 'scolarite'):
                # Rediriger vers le tableau de bord de la scolarité
                return redirect('dashboard_scolarite')
            elif hasattr(user, 'enseignant'):
                # Rediriger vers le tableau de bord de l'enseignant
                return redirect('dashboard_enseignant')
            else:
                # L'utilisateur n'a pas de type défini, gérer en conséquence
                pass
        else:
            # Gérer l'authentification invalide, par exemple afficher un message d'erreur
            return render(request, 'login.html', {'error_message': 'Nom d\'utilisateur ou mot de passe incorrect'})

    return render(request, 'login.html')
