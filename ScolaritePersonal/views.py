from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,"ScolaritePersonal/index.html")

def envoyer (request):
    
    return render(request,"copie/envoyer_copie.html")

def copie_corrigee (request):
    
    return render(request,"copie/copie_corrigee.html")

def Profil (request):
    
    return render(request,"Profil/scolarite_profil.html") 