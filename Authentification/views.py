from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q

# Create your views here.
""" class LoginPageView(View):
    template_name = 'login_page.html'
    form_class = forms.LoginForm

    def get(self, request):
        form = self.form_class()
        message = ''
        return render(request, self.template_name, context={'form': form, 'message': message})
        
    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
        message = 'Identifiants invalides.'
        return render(request, self.template_name, context={'form': form, 'message': message}) """
def login_view(request):
    
    return render(request, "login_page.html")
    
def signup_view(request):
    error=False
    message=" "
    
    if request.method == 'POST':
        name=request.POST.get('name',None)
        prenom=request.POST.get('prenom',None)
        email=request.POST.get('email',None)
        password=request.POST.get('password',None)
        repassword=request.POST.get('repassword',None)
        
        try :
            validate_email(email)
        except:
            error=True
            message=" Veuillez entrer un email valide !"
           
        if error==False:
            if password !=repassword:
                error=True
                message = "Mot de passe incorrect !" 
                
        user=User.objects.filter(Q(email=email) | Q(username=name) ).first()
        if user:
            error = True
            message = f"Un utilisateur avec email {email} et un nom {name} existe déjà !"
            
        #Enregister un utilisateur   
        if error==False:
            user = User(
                username=name,
                email=email,
            )
            user.save()
            user.password=password
            user.set_password(password)
            user.save()
            
            print("=="*5 ,"NEW POST",name,prenom,email,password,repassword,"=="*5)
          
    context ={
        'error':error,
        'message':message
        }
    return render(request, "register_page.html",context)
