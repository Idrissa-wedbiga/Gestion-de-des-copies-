# forms.py
from datetime import datetime
from django import forms
from django.forms.widgets import ClearableFileInput

from Enseignant.models import EnseignantModels
from Etudiant.models import StudentFile
from .models import DossierImageTif

class DossierImageForms(forms.Form):
    MODULE_CHOICES = [
        ('Statistique', 'Statistique'),
        ('Algèbre', 'Algèbre'),
        ('Analyse', 'Analyse'),
        ('Programmation Orientée Objet', 'Programmation Orientée Objet'),
        ('Thermodynamique', 'Thermodynamique'),
        ('Problabilité', 'Problabilité'),
        ('Algorithemique', 'Algorithemique'),
    ]

    PROMOTION_CHOICES = [
        ('MPCI - 2020-2021', 'MPCI - 2020-2021'),
        ('Informatique - 2020-2021', 'Informatique - 2020-2021'),
        ('SVT - 2019-2020', 'SVT - 2019-2020'),
        ('Lettre moderne - 2020-2021', 'Lettre moderne - 2020-2021'),
        ('Allemand - 2017-2018', 'Allemand - 2017-2018'),
    ]

    NIVEAU_CHOICES = [
        ('L1', 'L1'),
        ('L2', 'L2'),
        ('L3', 'L3'),
        ('M1', 'M1'),
        ('M2', 'M2'),
    ]
    UFR_CHOICES = [('Choisir ','Choisir'), 
        ('UFR-SEG', 'UFR-SEG'), ('UFR-ST', 'UFR-ST'),
        ('UFR-LSH', 'UFR-LSH'),
        ('IUT', 'IUT'),
    ]
    promotion = forms.ChoiceField(choices=PROMOTION_CHOICES)
    module = forms.ChoiceField(choices=MODULE_CHOICES)
    niveau = forms.ChoiceField(choices=NIVEAU_CHOICES)
    nombre =forms.IntegerField(label='Nombre de copies')
    enseignant_matricule = forms.CharField(max_length=100, label='Matricule')
    #enseignant_nom = forms.CharField(max_length=100, label='Nom Enseignant', required=False)
    #enseignant_prenom = forms.CharField(max_length=100, label='Prenom(s) Enseignant', required=False)
    

    date = forms.DateTimeField(initial=datetime.now, widget=forms.HiddenInput())  
    
    def __init__(self, *args, **kwargs):
        super(DossierImageForms, self).__init__(*args, **kwargs)
        self.fields['enseignant_matricule'].choices = [(e.matricule, f"{e.username} {e.prenom}") for e in EnseignantModels.objects.all()]  
    class meta:
        model = DossierImageTif
        fields = ['dossier']
        widgets = {
            'dossier': ClearableFileInput(attrs={'allow_multiple_selected': True, 'class': 'form-control'})
        }
        
class UploadFileForm(forms.Form):
    MODULE_CHOICES = [
        ('Statistique', 'Statistique'),
        ('Algèbre', 'Algèbre'),
        ('Analyse', 'Analyse'),
        ('POO', 'POO'),
        ('Algorithemique', 'Algorithemique'),
    ]
    module = forms.ChoiceField(choices=MODULE_CHOICES)
    
    #telechargement_date = forms.DateTimeField(initial=datetime.now, widget=forms.HiddenInput()) 
    class meta:
        model: StudentFile
        fields = ['fichier']
        widgets = {
            'file': ClearableFileInput(attrs={'allow_multiple_selected': True, 'class': 'form-control'})
        }