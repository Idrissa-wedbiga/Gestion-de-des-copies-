from django.db import models
from Authentification.models import CustomUser
from django.db import models
from django.contrib.auth.hashers import make_password
from django.contrib.auth import get_user_model


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
            