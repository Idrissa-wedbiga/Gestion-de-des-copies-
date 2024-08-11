from django.db import models
from Authentification.models import CustomUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model



# Create your models here.
    #Enseignant
class EnseignantModels(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='enseignant_profile', default=None, blank=True, null=True)
    specialite = models.CharField(max_length=100, verbose_name='Specialite')
    
    class Meta:
        verbose_name = "Enseignant"
        verbose_name_plural = "Enseignants"

    def save(self, *args, **kwargs):
        if not self.pk:  # Lors de la création initiale
            self.password = make_password(self.password)
        super(EnseignantModels, self).save(*args, **kwargs)
        
# class EnvoiCopieCorrigee(DossierImageTif):
    
#     enseignant = models.ForeignKey(EnseignantModels, on_delete=models.CASCADE,default =None)
#     scolarite = models.ForeignKey(ScolariteModels, on_delete=models.CASCADE, default='', blank=True, null=True)
    
#     enseignant_nom = models.CharField(max_length=100,default='')
#     enseignant_prenom = models.CharField(max_length=100,default='')
#     module = models.CharField(max_length=100, verbose_name='Module',default='')
#     promotion = models.CharField(max_length=100,verbose_name='Promotion',default='')
#     niveau = models.CharField(max_length=100, verbose_name='Niveau',default='')
#     nombre = models.IntegerField(verbose_name='Nombre de copies',default='')
#     dossier = models.FileField(upload_to='uploads/', max_length=100)
#     date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
       return f"{self.matricule}-{self.name}-{self.prenom}"