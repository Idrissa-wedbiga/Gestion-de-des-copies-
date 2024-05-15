from Authentification.models import CustomUser
from django.db import models
from django.contrib.auth.models import AbstractUser

class ScolariteModels(CustomUser):
    fonction = models.CharField(max_length=100, verbose_name='Emploi/Fonction')
    etablissement = models.CharField(max_length=100)
    customuser_ptr = models.OneToOneField(CustomUser, on_delete=models.CASCADE,parent_link=True,default="default")
