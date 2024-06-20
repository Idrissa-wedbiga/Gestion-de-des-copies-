# forms.py
from django import forms
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate

class MatriculeAuthenticationForm(AuthenticationForm):
    matricule = forms.CharField(label='Matricule')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields.pop('username')
        self.fields['matricule'].widget.attrs['placeholder'] = 'Votre matricule'
        self.fields['password'].widget.attrs['placeholder'] = 'Votre mot de passe'

    def clean(self):
        matricule = self.cleaned_data.get('matricule')
        password = self.cleaned_data.get('password')

        if matricule and password:
            self.user_cache = authenticate(self.request, matricule=matricule, password=password)
            if self.user_cache is None:
                raise forms.ValidationError(
                    self.error_messages['invalid_login'],
                    code='invalid_login',
                    params={'username': 'matricule'},
                )
            else:
                self.confirm_login_allowed(self.user_cache)

        return self.cleaned_data

