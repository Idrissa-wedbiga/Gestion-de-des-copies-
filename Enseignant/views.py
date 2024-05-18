from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from UserPrincipale.models import EnseignantModels
from django.contrib.auth import authenticate, login
from django.contrib import messages


# Create your views here.
@login_required(login_url='Authentification:login')
def index (request):

    return render(request,"enseignant/index.html")

#connexion d'un enseignant
# def enseignant_login (request):
#     if request.method == 'POST':
#         matricule = request.POST.get('matricule')
#         password = request.POST.get('password')

#         try:
#             enseignant = EnseignantModels.objects.get(matricule=matricule)
#             user = authenticate(request, username=enseignant.user.username, password=password)
#             if user is not None:
#                 login(request, user)
#                 return redirect('Enseignant:index')
#             else:
#                 messages.error(request, "Matricule ou mot de passe incorrect.")
#         except EnseignantModels.DoesNotExist:
#             messages.error(request, "Matricule ou mot de passe incorrect.")
#     return render(request, 'Authentification/login_page.html')

def enseigant_profile (request):

    return render(request,"Profil/enseigant_profile.html")

def Composer (request):

    return render(request,"Copie/compos_copie.html")

def Envoyer (request):

    return render(request,"Copie/envoyer_copie.html")

def Corriger (request):
     
    return render(request,"Copie/corriger_copie.html")