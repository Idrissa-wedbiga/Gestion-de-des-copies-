from django.utils import timezone
import os
import zipfile
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from Enseignant.models import EnseignantModels
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.core.files.base import ContentFile

from GestionDesCopies import settings
from ScolaritePersonal.forms import DossierImageForms
from ScolaritePersonal.models import DossierImageTif, ScolariteModels


# Create your views here.
@login_required(login_url='Authentification:login')
def index (request):
    # Récupérer l'utilisateur connecté (enseignant)
    enseignant = request.user

    # Récupérer les copies reçues par l'enseignant
    copies_recues = DossierImageTif.objects.filter(enseignant=enseignant).order_by('-date')

    context = {
        'copies_recues': copies_recues
    }
    return render(request,"enseignant/index.html",context)


def handle_uploaded_files(files, folder_path):
    zip_subfolder_path = os.path.join(folder_path, 'copies.zip')
    with zipfile.ZipFile(zip_subfolder_path, 'w') as zipf:
        for f in files:
            file_path = os.path.join(folder_path, f.name)
            with open(file_path, 'wb+') as destination:
                for chunk in f.chunks():
                    destination.write(chunk)
            zipf.write(file_path, os.path.basename(file_path))
            os.remove(file_path)  # Optionally remove the original files
    return zip_subfolder_path

@login_required(login_url='Authentification:login')
def Envoyer(request):
    if request.method == 'POST':
        form = DossierImageForms(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('dossier')
            scolarite_matricule = form.cleaned_data['enseignant_matricule']#ici c'est plutot scolarité_matricule qui sera recuperer
            
            try:
                scolarite = ScolariteModels.objects.get(matricule=scolarite_matricule)
            except ScolariteModels.DoesNotExist:
                message = f"Aucun enseignant trouvé avec le matricule {scolarite_matricule}."
                return render(request, 'copie/copie_envoyee.html', {'message': message})

            # Crée un dossier pour l'enseignant
            folder_name = f'{scolarite_matricule}_{scolarite.username}'
            folder_path = os.path.join(settings.MEDIA_ROOT, 'uploads', folder_name)

            if not os.path.exists(folder_path):
                os.makedirs(folder_path)

            # Gérer le fichier uploadé
            zip_file_path = handle_uploaded_files(files, folder_path)

            # Obtenir l'instance de ScolariteModels de l'utilisateur connecté
            
            #scolarite = ScolariteModels.objects.get(user=request.user)
            
                # message = 'Aucune scolarité associée à cet utilisateur.'
                # return render(request, 'copie/copie_envoyee.html', {'message': message})
            
            #logger.debug(f'Scolarite: {scolarite}')

            # Créer l'objet DossierImageTif
            DossierImageTif.objects.create(
                dossier=ContentFile(open(zip_file_path, 'rb').read(), 'copies.zip'),
                scolarite=scolarite,
                module=form.cleaned_data['module'],
                promotion=form.cleaned_data['promotion'],
                niveau=form.cleaned_data['niveau'],
                nombre=form.cleaned_data['nombre'],
                #enseignant_nom=form.cleaned_data['enseignant_nom'],
                #enseignant_prenom=form.cleaned_data['enseignant_prenom'],
                date=timezone.now(),
                #scolarite=scolarite  # Enregistrer l'utilisateur connecté
            ) 
            # Message de succès
            success_message = f"Copie envoyée avec succès à {scolarite.username} {scolarite.prenom}."
            messages.success(request, success_message)
            
            return redirect('Enseignant:Envoyer')
        else:
            messages.error(request, "Veuillez vérifier les informations du formulaire.")
    else:
        form = DossierImageForms()

    return render(request, "Copie/envoyer_copie.html", {'form': form})


def enseigant_profile (request):

    return render(request,"Profil/enseigant_profile.html")

def Composer (request):

    return render(request,"Copie/compos_copie.html")


def Corriger (request):
     
    return render(request,"Copie/corriger_copie.html")