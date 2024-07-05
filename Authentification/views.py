from urllib import request
from django.shortcuts import render,redirect
from django.core.validators import validate_email
from Authentification.backends import MatriculeBackend
from Authentification.forms import MatriculeAuthenticationForm
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
from django.contrib.auth import get_backends
from django.contrib.auth import authenticate
from django.contrib.auth.views import LoginView
from django.urls import reverse
from django.contrib import messages


    # Create your views here.
    
class CustomLoginView(LoginView):
    
    authentication_form = MatriculeAuthenticationForm
    template_name = 'login_page.html'
    
    def get_success_url(self):
        user = self.request.user
        if user.user_type == 'student':
            return reverse('Etudiant:index')
        elif user.user_type == 'enseignant':
            return reverse('Enseignant:index')
        elif user.user_type == 'scolarite':
            return reverse('ScolaritePersonal:index')
        elif user.is_superuser:
            return reverse('userprincipale:index')
        else:
            messages.error(self.request, 'Matricule ou mot de passe incorrect. Veuillez réessayer.')
            return reverse('Authentification:login')
    def form_valid(self, form):
        # Rediriger vers l'URL de succès appropriée après la validation du formulaire
        return super().form_valid(form)

        
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
        user_type = 'student'

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
            etudiant_promotion=etudiant_promotion,
            user_type=user_type
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

@login_required
def profil_view(request):
    context = {
        'user': request.user,
        # Ajoutez d'autres contextes ici si nécessaire
    }
    return render(request, 'base.html', context)