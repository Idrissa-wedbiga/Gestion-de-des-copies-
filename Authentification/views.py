from django.shortcuts import render,redirect
from django.core.validators import validate_email
from Authentification.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import requires_csrf_token
from UserPrincipale.models import EnseignantModels, ScolariteModels
from django.contrib.auth.hashers import check_password


    # Create your views here.
    
@requires_csrf_token
def login_view(request):
    message = ""
   
    if request.method == 'POST':
        matricule = request.POST.get('matricule', None)
        password = request.POST.get('password', None)

        # Vérifier si l'utilisateur est un enseignant
        enseignant = EnseignantModels.objects.filter(matricule=matricule, password=password).first()
        if enseignant:
            # Connecter l'enseignant
            request.session['user_matricule'] = enseignant.matricule  # Stocker le matricule de l'enseignant dans la session
            return redirect('Enseignant:index')
        else:
            # Vérifier si l'utilisateur est une scolarité
            scolarite = ScolariteModels.objects.filter(matricule=matricule, password=password).first()
            if scolarite:
                # Connecter la scolarité
                request.session['user_matricule'] = scolarite.matricule  # Stocker le matricule de la scolarité dans la session
                return redirect('ScolaritePersonal:index')
            else:
                # Vérifier si l'utilisateur est un administrateur
                admin_user = CustomUser.objects.filter(matricule=matricule).first()
                if admin_user and check_password(password, admin_user.password):
                    user = get_user_model().objects.get(username=admin_user.username)  # Obtenir l'utilisateur associé
                    user.backend = 'django.contrib.auth.backends.ModelBackend'  # Spécifier le backend d'authentification
                    login(request, user)
                    return redirect('userprincipale:index')
                else:
                    message = "Matricule ou mot de passe incorrect."
    context = {'message': message}
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

# class CustomLoginView(LoginView):
#     authentication_form = CustomAuthenticationForm
