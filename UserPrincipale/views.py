from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import ScolariteModels
from django.contrib import messages



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
    message=messages.get_messages(request)
    scolarites = ScolariteModels.objects.all()

    context = {'scolarites': scolarites, 'message': message}
    return render(request, "Scolarite/scolarity.html", context)

def sc_ajouter(request):
   # Verifier si le formulaire a ete soumis
    if request.method == 'POST':
        # Récupérer les données soumises par l'utilisateur
        matricule = request.POST.get('matricule')
        username = request.POST.get('username')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fonction = request.POST.get('fonction')
        etablissement = request.POST.get('etablissement')

        # Créer un nouvel objet Scolarite
        scolarite = ScolariteModels.objects.create(matricule=matricule, username=username,prenom=prenom, email=email, password=password, fonction=fonction, etablissement=etablissement)
        scolarite.save()
        messages.success(request, 'Scolarité bien ajoutée !')
        
        # Rediriger vers une autre vue ou un autre URL
        return redirect('userprincipale:scolarity')
    else:
        # Afficher le formulaire vide
        return render(request, 'Scolarite/sc_ajouter.html')


def sc_editer(request):
    
    return render(request, "Scolarite/sc_edit.html")

#user profil
def usersprofile(request):

    return render(request, "Profil/users_profile.html")
