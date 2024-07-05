from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from Authentification import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from Etudiant.models import EtudiantModels, StudentFile
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required
def index(request):
    student_files_list = StudentFile.objects.filter(student=request.user).order_by('-telechargement_date')
    paginator = Paginator(student_files_list, 10)  # 10 fichiers par page

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'student_files_list': page_obj
    }
    return render(request, "etudiant/index.html", context)


def Mes_copies (request):
    
    return render(request,"copie/mes_copies.html")

def Fichier_Personnel (request):
    
    return render(request,"dossier/fichier_personel.html")

def Profil (request):
    
    return render(request,"Profil/etudiant_profil.html")
