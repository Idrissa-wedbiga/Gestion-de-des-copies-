from Authentification.models import CustomUser
from django.db import models

class VotreModeleUsUerPrincipale(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
