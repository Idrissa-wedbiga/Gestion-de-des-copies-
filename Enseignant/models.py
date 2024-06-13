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