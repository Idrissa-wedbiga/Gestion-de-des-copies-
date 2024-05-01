from django.shortcuts import render
#
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
    if request.method == 'POST':
        name=request.POST.get('name',None)
        prenom=request.POST.get('prenom',None)
        email=request.POST.get('email',None)
        password=request.POST.get('password',None)
        repassword=request.POST.get('repassword',None)
        print("=="*5 ,"NEW POST",name,prenom,email,password,repassword,"=="*5)
    return render(request, "register_page.html")
