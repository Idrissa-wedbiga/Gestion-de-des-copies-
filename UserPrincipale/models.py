from Authentification.models import CustomUser
from django.db import models
from django.contrib.auth.hashers import make_password


    #Scolarite
class ScolariteModels(CustomUser):
    fonction = models.CharField(max_length=100, verbose_name='Emploi/Fonction')
    etablissement = models.CharField(max_length=100)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE,parent_link=True,default="default")
    def save(self, *args, **kwargs):
        if not self.pk:  # Lors de la création initiale
            self.password = make_password(self.password)
        super(ScolariteModels, self).save(*args, **kwargs)
    
    #Enseignant
class EnseignantModels(CustomUser):
    specialite = models.CharField(max_length=100, verbose_name='Specialite')
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE,parent_link=True,default="default")
    def save(self, *args, **kwargs):
        if not self.pk:  # Lors de la création initiale
            self.password = make_password(self.password)
        super(EnseignantModels, self).save(*args, **kwargs)