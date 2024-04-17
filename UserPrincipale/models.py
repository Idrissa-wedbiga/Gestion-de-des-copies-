from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models



# Create your models here.
class Utilisateur(AbstractUser):
    # Vous pouvez ajouter d'autres champs personnalisés si nécessaire
    pass

class Etudiant(models.Model):
    user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=128)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='Etudiant')
    # Autres champs spécifiques à l'étudiant

class Scolarite(models.Model):
    #user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=128)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='Scolarite')
    # Autres champs spécifiques à la scolarité

class Enseignant(models.Model):
    #user = models.OneToOneField(Utilisateur, on_delete=models.CASCADE)
    #email = models.EmailField(unique=True)
    #password = models.CharField(max_length=128)
    user = models.ForeignKey(Utilisateur, on_delete=models.CASCADE, related_name='Enseignant')
    # Autres champs spécifiques à l'enseignant
    # models.py




class Utilisateur(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=128)

    # Champs spécifiques à l'utilisateur (si nécessaire)


class Etudiant(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=128)

    # Champs spécifiques à l'étudiant

class Scolarite(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=128)

    # Champs spécifiques à la scolarité

class Enseignant(models.Model):
    email = models.EmailField(max_length=255, unique=True)
    mot_de_passe = models.CharField(max_length=128)

    # Champs spécifiques à l'enseignant
