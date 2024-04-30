from django.shortcuts import render

# Create your views here.
def index (request):

    return render(request,"enseignant/index.html")

def enseigant_profile (request):

    return render(request,"Profil/enseigant_profile.html")

def Composer (request):

    return render(request,"Copie/compos_copie.html")

def Envoyer (request):

    return render(request,"Copie/envoyer_copie.html")

def Corriger (request):
     
    return render(request,"Copie/corriger_copie.html")