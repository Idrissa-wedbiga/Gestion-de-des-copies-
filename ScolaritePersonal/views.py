from django.utils import timezone
from django.core.files.base import ContentFile
import zipfile
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from GestionDesCopies import settings
from ScolaritePersonal.models import DossierImageTif, ScolariteModels
from Enseignant. models import EnseignantModels
from .forms import DossierImageForms
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
import logging
import re
from Etudiant.models import StudentFile, EtudiantModels
from .forms import UploadFileForm
from django.db.models import Sum
logger = logging.getLogger(__name__)

#from Enseignant.models import EnseignantModel


# Create your views here.
@login_required(login_url='Authentification:login')
def index (request):
     # Récupérer l'utilisateur connecté (scolarite)
    scolarite = request.user

    # Récupérer les copies reçues par la scolarité
    copies_recues = DossierImageTif.objects.filter(scolarite=scolarite).order_by('-date')

    context = {
        'copies_recues': copies_recues
    }
    
    return render(request,"ScolaritePersonal/index.html",context)


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
def envoyer(request):
    if request.method == 'POST':
        form = DossierImageForms(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('dossier')
            enseignant_matricule = form.cleaned_data['enseignant_matricule']
            
            try:
                enseignant = EnseignantModels.objects.get(matricule=enseignant_matricule)
            except EnseignantModels.DoesNotExist:
                message = f"Aucun enseignant trouvé avec le matricule {enseignant_matricule}."
                return render(request, 'copie/copie_envoyee.html', {'message': message})

            # Crée un dossier pour l'enseignant
            folder_name = f'{enseignant_matricule}_{enseignant.username}'
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
                enseignant=enseignant,
                module=form.cleaned_data['module'],
                promotion=form.cleaned_data['promotion'],
                niveau=form.cleaned_data['niveau'],
                nombre=form.cleaned_data['nombre'],
                date=timezone.now(),
            )
            # Message de succès
            success_message = f"Copie envoyée avec succès à {enseignant.username} {enseignant.prenom}."
            messages.success(request, success_message)
        else:
            messages.error(request, "Veuillez vérifier les informations du formulaire.")
    else:
        form = DossierImageForms()

    return render(request, "copie/envoyer_copie.html", {'form': form})

@login_required(login_url='Authentification:login')
def statistiques_enseignant(request):
   # Nombre d'enseignants ayant reçu des copies de la scolarité
    total_enseignants = DossierImageTif.objects.filter(scolarite=request.user.scolarite).values('enseignant').distinct().count()

    # Nombre total de copies envoyées par la scolarité
    total_copies = DossierImageTif.objects.filter(scolarite=request.user_type.scolarite).aggregate(total_copies=Sum('nombre'))['total_copies']

    # Nombre de modules non corrigés pour les copies envoyées par la scolarité
    total_modules = DossierImageTif.objects.filter(scolarite=request.user_type.scolarite).values('module').distinct().count()

    context = {
        'total_enseignants': total_enseignants,
        'total_copies': total_copies,
        'total_modules': total_modules,
    }

    return render(request, "ScolaritePersonal/index.html", context)


@login_required
def get_enseignant_details(request):
    
    enseignants = EnseignantModels.objects.all()
    enseignants_json = list(enseignants.values('matricule', 'username', 'prenom'))
    
    return JsonResponse(enseignants_json, safe=False)
@login_required
def copie_corrigee (request):
    
        return render (request,'copie/copie_corrigee.html')

@login_required
def copie_envoyee(request):
    try:
        # Récupérer l'utilisateur connecté (scolarité)
        scolarite = ScolariteModels.objects.get(user=request.user)
    except ScolariteModels.DoesNotExist:
        # Si aucune instance n'est trouvée, rediriger ou gérer l'erreur
        message = 'Aucune scolarité associée à cet utilisateur.'
        context = {'message': message} 
        return render(request, 'copie/copie_envoyee.html', context)
    
    # Récupérer les copies envoyées par cette scolarité
    copies_envoyees = DossierImageTif.objects.filter(scolarite=scolarite).order_by('-date')

    # Pagination des copies
    paginator = Paginator(copies_envoyees, 10)  # 10 copies par page

    page_number = request.GET.get('page')
    try:
        copies = paginator.page(page_number)
    except PageNotAnInteger:
        # Si la page n'est pas un entier, renvoyer la première page.
        copies = paginator.page(1)
    except EmptyPage:
        # Si la page est hors limites, renvoyer la dernière page de résultats.
        copies = paginator.page(paginator.num_pages)

    context = {
        'copies': copies,
        'scolarite': scolarite,
    }

    return render(request, 'copie/copie_envoyee.html', context)


@login_required
def Profil (request):
    
    return render(request,"Profil/scolarite_profil.html") 


@login_required
def upload_and_link_files(request):
    if request.method == "POST":
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('fichier')
            module = form.cleaned_data['module']
            upload_dir = os.path.join(settings.MEDIA_ROOT, 'student_files')

            # Créer le répertoire si nécessaire
            if not os.path.exists(upload_dir):
                os.makedirs(upload_dir)

            for file in files:
                file_path = os.path.join(upload_dir, file.name)  # Assurez-vous du chemin ici

                with open(file_path, 'wb+') as destination:
                    for chunk in file.chunks():
                        destination.write(chunk)

                if zipfile.is_zipfile(file_path):
                    extracted_path = os.path.join(upload_dir, 'extracted')
                    with zipfile.ZipFile(file_path, 'r') as zip_ref:
                        zip_ref.extractall(extracted_path)
                    os.remove(file_path)  # Supprimez le fichier zip après extraction

                    for filename in os.listdir(extracted_path):
                        if filename.endswith('.pdf'):
                            link_file_to_student(os.path.join('student_files', 'extracted', filename), module)
                else:
                    if file.name.endswith('.pdf'):
                        link_file_to_student(os.path.join('student_files', file.name), module)

            return redirect('ScolaritePersonal:send_student')  # Rediriger vers le tableau de bord ou une autre page après l'upload
    else:
        form = UploadFileForm()
    return render(request, 'copie/Student_copie.html', {'form': form})

def link_file_to_student(file_path, module):
    filename = os.path.basename(file_path)
    matricule_match = re.search(r'([EN]\d{11})', filename)  # Match matricules commençant par E ou N suivis de 11 chiffres
    if matricule_match:
        matricule = matricule_match.group(1)
        try:
            student = EtudiantModels.objects.get(matricule=matricule)
            student_file = StudentFile(student=student, fichier=file_path, module=module)
            student_file.save()
        except EtudiantModels.DoesNotExist:
            # Gérez le cas où aucun étudiant avec ce matricule n'existe
            pass
