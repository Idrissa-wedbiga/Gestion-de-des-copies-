from datetime import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from GestionDesCopies import settings
from ScolaritePersonal.models import DossierImageTif
from Enseignant. models import EnseignantModels
from .forms import DossierImageForms
import os
from django.http import JsonResponse
from django.contrib.auth.decorators import login_required

#from Enseignant.models import EnseignantModel


# Create your views here.
@login_required(login_url='Authentification:login')
def index (request):
    return render(request,"ScolaritePersonal/index.html")

# views.py


def handle_uploaded_files(files):
    upload_dir = 'media/uploads/'
    if not os.path.exists(upload_dir):
        os.makedirs(upload_dir)
    for f in files:
        with open(os.path.join(upload_dir, f.name), 'wb+') as destination:
            for chunk in f.chunks():
                destination.write(chunk)

def envoyer(request):
    if request.method == 'POST':
        form = DossierImageForms(request.POST, request.FILES)
        if form.is_valid():
            files = request.FILES.getlist('dossier')
            enseignant_nom = form.cleaned_data['enseignant_nom']
            enseignant_prenom = form.cleaned_data['enseignant_prenom']
            enseignant_matricule = form.cleaned_data['enseignant_matricule']
            enseignant = EnseignantModels.objects.get(matricule=enseignant_matricule)
            handle_uploaded_files(files)  # Passer tous les fichiers à la fonction
            for f in files:
                DossierImageTif.objects.create(
                    dossier=f,
                    enseignant=enseignant,
                    module=form.cleaned_data['module'],
                    promotion=form.cleaned_data['promotion'],
                    niveau=form.cleaned_data['niveau'],
                    nombre=form.cleaned_data['nombre'],
                    enseignant_nom=enseignant_nom,
                    enseignant_prenom=enseignant_prenom,
                    date=datetime.now()
                )
            return redirect('ScolaritePersonal:envoyer')
    else:
        form = DossierImageForms()
    return render(request, "copie/envoyer_copie.html", {'form': form})

def get_enseignant_details(request):
    
    enseignants = EnseignantModels.objects.all()
    enseignants_json = list(enseignants.values('matricule', 'username', 'prenom'))
    
    return JsonResponse(enseignants_json, safe=False)

def copie_corrigee (request):
    
        return render (request,'copie/copie_corrigee.html')


def copie_envoyee (request):
    copies_list = DossierImageTif.objects.all()
    paginator = Paginator(copies_list, 10)  # 10 copies par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    return render(request, 'copie/copie_envoyee.html', {'page_obj': page_obj})

def Profil (request):
    
    return render(request,"Profil/scolarite_profil.html") 