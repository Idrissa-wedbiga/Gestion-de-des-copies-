from django.shortcuts import render,redirect
from django.core.validators import validate_email
from Authentification.models import CustomUser
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth import get_user_model
from django.views.decorators.csrf import requires_csrf_token
from django.contrib.auth.hashers import check_password
from Enseignant.models import EnseignantModels
from Etudiant.models import EtudiantModels
from ScolaritePersonal.models import ScolariteModels
from django.core.exceptions import ValidationError
from django.core.validators import validate_email
from django.contrib.auth import get_backends

    # Create your views here.
    
@requires_csrf_token
def login_view(request):
    message = ""
   
    if request.method == 'POST':
        matricule = request.POST.get('matricule', None)
        password = request.POST.get('password', None)

        # Essayer d'authentifier en tant qu'utilisateur générique
        user = CustomUser.objects.filter(matricule=matricule).first()
        if user and check_password(password, user.password):
            if hasattr(user, 'enseignant_profile'):
                request.session['user_matricule'] = user.matricule
                return redirect('Enseignant:index')
            elif hasattr(user, 'scolarite_profile'):
                request.session['user_matricule'] = user.matricule
                return redirect('ScolaritePersonal:index')
            elif user.is_superuser:
                # Spécifier le backend pour le superuser
                for backend in get_backends():
                    user.backend = f"{backend.__module__}.{backend.__class__.__name__}"
                    login(request, user)
                    return redirect('userprincipale:index')
            elif hasattr(user, 'etudiant_profile'):
                request.session['user_matricule'] = user.matricule
                return redirect('Etudiant:index')
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
        matricule = request.POST.get('matricule', None)
        email = request.POST.get('email', None)
        password = request.POST.get('password', None)
        repassword = request.POST.get('repassword', None)
        etudiant_filiere = request.POST.get('etudiant_filiere', None)
        etudiant_niveau = request.POST.get('etudiant_niveau', None)
        etudiant_promotion = request.POST.get('etudiant_promotion', None)

        try:
            validate_email(email)
        except ValidationError:
            error = True
            message = "Veuillez entrer un email valide !"

        if not error:
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
                    
            # Créer un profil étudiant associé
        etudiant = EtudiantModels.objects.create(
            matricule=matricule,
            email=email,
            username=username,
            prenom=prenom,
            password=password,
            etudiant_filiere=etudiant_filiere,
            etudiant_niveau=etudiant_niveau,
            etudiant_promotion=etudiant_promotion
        )
        etudiant.save()
        print(etudiant)

        return redirect('Authentification:login')

    context = {'message': message, 'error': error}
    return render(request, "register_page.html", context)

def logout_view(request):
    
    logout(request)
    
    return redirect('Authentification:home')
def home(request):
    
    return render(request,"home.html")
