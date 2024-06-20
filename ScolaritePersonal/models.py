from django.db import models
from Authentification.models import CustomUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model

from Enseignant.models import EnseignantModels



# Create your models here.

    #Scolarite
class ScolariteModels(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='scolarite_profile', default=None, blank=True, null=True)    
    fonction = models.CharField(max_length=100, verbose_name='Emploi/Fonction')
    etablissement = models.CharField(max_length=100)
    
    class Meta:
        verbose_name = "Scolarite"
        verbose_name_plural = "Scolarites"

    def save(self, *args, **kwargs):
        if not self.pk:  # Lors de la création initiale
            self.password = make_password(self.password)
        super(ScolariteModels, self).save(*args, **kwargs)
        
class DossierImageTif(models.Model):
    enseignant = models.ForeignKey(EnseignantModels, on_delete=models.CASCADE,default =None)
    
    enseignant_nom = models.CharField(max_length=100,default='')
    enseignant_prenom = models.CharField(max_length=100,default='')
    module = models.CharField(max_length=100, verbose_name='Module',default='')
    promotion = models.CharField(max_length=100,verbose_name='Promotion',default='')
    niveau = models.CharField(max_length=100, verbose_name='Niveau',default='')
    nombre = models.IntegerField(verbose_name='Nombre de copies',default='')
    dossier = models.FileField(upload_to='uploads/', max_length=100)
    date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"{self.dossier.name} - {self.enseignant.username} {self.enseignant.prenom}"