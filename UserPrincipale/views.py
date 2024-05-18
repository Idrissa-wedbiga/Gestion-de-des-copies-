from django.shortcuts import render, redirect, get_object_or_404
from .models import ScolariteModels
from .models import EnseignantModels
from django.contrib import messages
from .forms import ScolariteForm, EnseignantForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q


def index(request):

    return render(request, "userprincipale/index.html")

#enseignant
def enseignant(request):
    query = request.GET.get('q')
    if query:
        enseignants = EnseignantModels.objects.filter(
            Q(matricule__icontains=query) |
            Q(username__icontains=query) |
            Q(prenom__icontains=query) |
            Q(specialite__icontains=query)
        )
    else:
        enseignants = EnseignantModels.objects.all()

    message = messages.get_messages(request)

    context = {'enseignants': enseignants, 'message': message}
    return render(request, "Enseignant/enseignant.html", context)


    
def ajouter(request):
    if request.method == 'POST':
        # Récupérer les données soumises par l'utilisateur
        matricule = request.POST.get('matricule')
        username = request.POST.get('username')
        prenom = request.POST.get('prenom')
        specialite = request.POST.get('specialite')
        email = request.POST.get('email')
        password = request.POST.get('password')
        

        # Créer un nouvel objet Scolarite
        enseignant = EnseignantModels.objects.create(matricule=matricule, username=username,prenom=prenom,specialite=specialite, email=email, password=password)
        enseignant.save()
        messages.success(request, 'Enseignant bien ajouté !')
        
        # Rediriger vers une autre vue ou un autre URL
        return redirect('userprincipale:enseignant')
    else:
        # Afficher le formulaire vide
        return render(request, "Enseignant/ajouter.html")
    
   
def editer(request, matricule):
    enseignant = get_object_or_404(EnseignantModels, matricule=matricule)
    
    if request.method == 'POST':
        # Créer un formulaire de modification et pré-remplir avec les données actuelles de la scolarité
        form = EnseignantForm(request.POST, instance=enseignant)
        if form.is_valid():
            form.save()
            return redirect('userprincipale:enseignant')
    else:
        # Afficher le formulaire pré-rempli
        form = EnseignantForm(instance=enseignant)
    
    return render(request, 'Enseignant/edit.html', {'form': form})

def supprimer(request, matricule):
    if request.method == 'POST':
        enseignant = get_object_or_404(EnseignantModels, matricule=matricule)
        enseignant.delete()
    return HttpResponseRedirect(reverse('userprincipale:enseignant'))
#scolarite
def scolarity(request):
    query=request.GET.get('qs')
    if query:
        scolarites = ScolariteModels.objects.filter(
            Q(matricule__icontains=query) |
            Q(username__icontains=query) |
            Q(prenom__icontains=query) |
            Q(etablissement__icontains=query)
        )
    else:
        scolarites = ScolariteModels.objects.all()
        
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


def sc_editer(request, matricule):
    # Récupérer la scolarité à modifier
    scolarite = get_object_or_404(ScolariteModels, matricule=matricule)
    
    if request.method == 'POST':
        # Créer un formulaire de modification et pré-remplir avec les données actuelles de la scolarité
        form = ScolariteForm(request.POST, instance=scolarite)
        if form.is_valid():
            form.save()
            return redirect('userprincipale:scolarity')
    else:
        # Afficher le formulaire pré-rempli
        form = ScolariteForm(instance=scolarite)
    
    return render(request, 'Scolarite/sc_edit.html', {'form': form})

def sc_supprimer(request, matricule):
    
    if request.method == 'POST':
       
        scolarite = ScolariteModels.objects.get(matricule=matricule)
        scolarite.delete()
       
    return HttpResponseRedirect(reverse('userprincipale:scolarity'))

#user profil
def usersprofile(request):

    return render(request, "Profil/users_profile.html")
