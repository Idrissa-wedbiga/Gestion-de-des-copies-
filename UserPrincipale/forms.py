from django import forms
from Etudiant.models import EtudiantModels
from Enseignant.models import EnseignantModels
from ScolaritePersonal.models import ScolariteModels

class ScolariteForm(forms.ModelForm):
    class Meta:
        model = ScolariteModels
        fields = ['matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email']
        
class EnseignantForm(forms.ModelForm):
    class Meta:
        model = EnseignantModels
        fields = ['matricule', 'username', 'prenom', 'specialite', 'email']
class EtudiantForm(forms.ModelForm):
    class Meta:
        model = EtudiantModels
        fields = ['matricule', 'username', 'prenom', 'etudiant_filiere','etudiant_promotion','etudiant_niveau','email']