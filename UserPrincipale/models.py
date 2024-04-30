from django.db import models
from django.contrib.auth.models import AbstractUser

class Administrateur(AbstractUser):
    matricule = models.CharField(max_length=255, blank=True)
    # Champs spécifiques à l'utilisateur (si non présente)

class Etudiant(models.Model):
    user = models.OneToOneField(Administrateur, on_delete=models.CASCADE)
    # Champs spécifiques à l'étudiant

class Scolarite(models.Model):
    user = models.OneToOneField(Administrateur, on_delete=models.CASCADE)
    # Champs spécifiques à la scolarité

class Enseignant(models.Model):
    user = models.OneToOneField(Administrateur, on_delete=models.CASCADE)
    # Champs spécifiques à l'enseignant
