from django import forms
from .models import ScolariteModels, EnseignantModels

class ScolariteForm(forms.ModelForm):
    class Meta:
        model = ScolariteModels
        fields = ['matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email']
        
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = EnseignantModels
        fields = ['matricule', 'username', 'prenom', 'specialite', 'email']
