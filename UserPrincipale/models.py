from Authentification.models import CustomUser
from django.db import models

class VotreModeleUserPrincipale(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
