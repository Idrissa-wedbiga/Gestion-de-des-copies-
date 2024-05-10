from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
""" 
class User(AbstractUser):
    
    CREATOR = 'CREATOR'
    SUBSCRIBER = 'SUBSCRIBER'

ROLE_CHOICES = (
    (CREATOR, 'Créateur'),
    (SUBSCRIBER, 'Abonné'),
)
profile_photo = models.ImageField(verbose_name='Photo de profil')
role = models.CharField(max_length=30, choices=ROLE_CHOICES, verbose_name='Rôle') """


class CustomUser(AbstractUser):
    # Ajoutez des champs supplémentaires si nécessaire
    matricule = models.CharField(max_length=100, unique=True, primary_key=True, verbose_name='Matricule',default='')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    

class CustomUserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Le champ email est obligatoire')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    def create_superuser(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(email, password, **extra_fields)
    