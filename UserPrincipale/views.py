from django.shortcuts import render, redirect, get_object_or_404
from Etudiant.models import EtudiantModels
from Enseignant.models import EnseignantModels
from django.contrib import messages
from ScolaritePersonal.models import ScolariteModels
from .forms import ScolariteForm, EnseignantForm
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import Q
from django.contrib.auth.decorators import user_passes_test
from django.views.decorators.csrf import csrf_protect
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_user_model


@csrf_protect
#@user_passes_test(lambda u: u.is_superuser)
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
        user_type ='enseignant'
        
        try:
           validate_email(email)
        except ValidationError:
            error = True
            message = "Veuillez entrer un email valide !"

        User = get_user_model()
        
        user = User.objects.filter(email=email).first()
        existing_user = User.objects.filter(matricule=matricule).first()

        if existing_user:
            error = True
            message = f"Le matricule {matricule} existe déjà !"
            
        if user:
            error = True
            message = f"Un utilisateur avec l'email: {email} existe déjà !"

        # Créer un nouvel objet Scolarite
        enseignant = EnseignantModels.objects.create(
            matricule=matricule, 
            username=username,
            prenom=prenom,specialite=specialite, 
            email=email,
            user_type=user_type, 
            password=password
            )
    
        enseignant.save()
        messages.success(request, 'Enseignant bien ajouté !')
        
        # Rediriger vers une autre vue ou un autre URL
        return redirect('userprincipale:enseignant')
    else:
        # Afficher le formulaire vide
        context = {'message': message, 'error': error}
        return render(request, "Enseignant/ajouter.html",context)
    
   
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
    error = False
    message = ""
    if request.method == 'POST':
        
        # Récupérer les données soumises par l'utilisateur
        matricule = request.POST.get('matricule')
        username = request.POST.get('username')
        prenom = request.POST.get('prenom')
        email = request.POST.get('email')
        password = request.POST.get('password')
        fonction = request.POST.get('fonction')
        etablissement = request.POST.get('etablissement')
        user_type='scolarite'
        
        try:
           validate_email(email)
        except ValidationError:
            error = True
            message = "Veuillez entrer un email valide !"

        User = get_user_model()
        
        user = User.objects.filter(email=email).first()
        existing_user = User.objects.filter(matricule=matricule).first()

        if existing_user:
            error = True
            message = f"Le matricule {matricule} existe déjà !"
            
        if user:
            error = True
            message = f"Un utilisateur avec l'email: {email} existe déjà !"

        # Créer un nouvel objet Scolarite
        scolarite = ScolariteModels.objects.create(
            matricule=matricule,                                      
            username=username,
            prenom=prenom, 
            email=email, 
            password=password, 
            fonction=fonction,
            user_type=user_type, 
            etablissement=etablissement
            )
        scolarite.save()
        messages.success(request, 'Scolarité bien ajoutée !')
        
        # Rediriger vers une autre vue ou un autre URL
        return redirect('userprincipale:scolarity')
    else:
        # Afficher le formulaire vide
        context = {'message': message, 'error': error}
        return render(request, 'Scolarite/sc_ajouter.html',context)
    

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

#Afficher les etudiants sur le dashbord de l'administrateur+
def etudiant(request):
    query = request.GET.get('qe')
    if query:
        etudiants = EtudiantModels.objects.filter(
      
                Q(matricule__icontains=query) |
                Q(username__icontains=query) |
                Q(prenom__icontains=query) |
                Q(etudiant_filiere__icontains=query) |
                Q(etudiant_niveau__icontains=query) |
                Q(etudiant_promotion__icontains=query)
            
        )
    else:
        etudiants = EtudiantModels.objects.filter()

    message = messages.get_messages(request)

    context = {'etudiants': etudiants, 'message': message}
    return render(request, "Etudiant/etudiant_list.html", context)