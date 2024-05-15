from django.shortcuts import render,redirect
from django.core.validators import validate_email
from Authentification.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.views import LoginView
from .forms import CustomAuthenticationForm

    # Create your views here.
    #@login_required(login_url='Authentification:login')
@requires_csrf_token
def login_view(request):
    message = ""
   
    if request.method == 'POST':
        matricule = request.POST.get('matricule', None)
        password = request.POST.get('password', None)
        
        # Authentifier l'utilisateur en utilisant le matricule et le mot de passe
        User = get_user_model( )
        user = User.objects.filter(matricule=matricule).first()
      
        if user:
            auth_user = authenticate(matricule=user.matricule, password=password)
            
            if auth_user:
                login(request, auth_user)
                print(auth_user)
                #print(auth_user.matricule, auth_user.password)
                return redirect('userprincipale:index')
            else:
                if user.password != password:
                # Informer l'utilisateur que la connexion a échoué
                    message = "Mot de passe incorrect." 
                else:
                    
                    message = "Matricule/INE  incorrect."
                
        else:
            
            message = "L'utilisateur n'existe pas !."
            
    context = {
        'message': message
            }
    return render(request, "login_page.html", context)

    
def signup_view(request):
    error = False
    message = ""
    
    if request.method == 'POST':
        username = request.POST.get('username', None)
        prenom = request.POST.get('prenom', None)
        matricule= request.POST.get('matricule', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        
        try:
            validate_email(email)
        except:
            error = True
            message = "Veuillez entrer un email valide !"
           
        if error == False:
            if password != repassword:
                error = True
                message = "Les mots de passe ne correspondent pas !" 
                
        User = get_user_model()
        user = User.objects.filter(email=email).first()
        existing_user = User.objects.filter(matricule=matricule).first()
        
        if existing_user:
            error = True
            message = f"Le matricule {matricule} existe déjà !"
        
        if user:
            error = True
            message = f"Un utilisateur avec l'email {email} existe déjà !"
            
        # Enregistrer un utilisateur   
        if error == False:
            user = User.objects.create_user(username=username,prenom=prenom,matricule=matricule, email=email, password=password)
            user.matricule = matricule
            user.username = username
            user.prenom = prenom
            user.email = email
            user.save()
            
            return redirect('Authentification:login')
           
          
    context = {
        'error': error,
        'message': message
    }
    return render(request, "register_page.html", context)

def logout_view(request):
    
    logout(request)
    
    return redirect('Authentification:home')
def home(request):
    
    return render(request,"home.html")

class CustomLoginView(LoginView):
    authentication_form = CustomAuthenticationForm
