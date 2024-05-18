# forms.py

# from django.contrib.auth.forms import AuthenticationForm
# from django import forms

# class CustomAuthenticationForm(AuthenticationForm):
#     matricule = forms.CharField(label="Matricule", max_length=100)
#     password = forms.CharField(label="Password", strip=False, widget=forms.PasswordInput)

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['username'] = self.fields.pop('matricule')
