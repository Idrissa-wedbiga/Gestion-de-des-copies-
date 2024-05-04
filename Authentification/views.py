from django.shortcuts import render,redirect
from django.core.validators import validate_email
from django.contrib.auth.models import User
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout

# Create your views here.
#@login_required(login_url='Authentification:login')
def login_view(request):
    
    if request.method == 'POST':
        email=request.POST.get('email',None)
        password=request.POST.get('password',None)
        
        user =User.objects.filter(email=email).first()
        if user:
            auth_user = authenticate(username=user.username,password=password)
            if auth_user:
                print(auth_user.email,auth_user.username)
            else:
                print("Wrong password")
        else:
            print("User doesn't exist")
            
        print("=="*5 ,"NEW POST",email,password,"=="*5)
        
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
            
            return redirect('Authentification:login')
           
          
    context ={
        'error':error,
        'message':message
        }
    return render(request, "register_page.html",context)

