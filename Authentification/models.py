from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models

# Create your models here.
class CustomUserManager(BaseUserManager):
    def create_user(self, matricule, email, username, prenom, password=None, **extra_fields):
        if not matricule:
            raise ValueError('The matricule must be set')
        if not email:
            raise ValueError('The email must be set')
        if not username:
            raise ValueError('The username must be set')
        if not prenom:
            raise ValueError('The prenom must be set')

        email = self.normalize_email(email)
        user = self.model(matricule=matricule, email=email, username=username, prenom=prenom, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, matricule, email, name, prenom, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        return self.create_user(matricule, email, name, prenom, password, **extra_fields)

class CustomUser(AbstractUser):
    USER_TYPE_CHOICES = [
        ('student', 'Etudiant'), 
        ('scolarite', 'Scolarite'),
        ('enseignant', 'Enseignant')
    ]
    user_type = models.CharField(choices=USER_TYPE_CHOICES, default='', max_length=20)
    matricule = models.CharField(max_length=100, primary_key=True, verbose_name='Matricule',default='')
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=100 ,blank=True, null=True)
    username = models.CharField(max_length=150, blank=True, null=True, verbose_name='Nom d\'utilisateur')
    prenom = models.CharField(max_length=100)
    
    USERNAME_FIELD = 'matricule'
    REQUIRED_FIELDS = ['email', 'prenom', 'name']

    objects = CustomUserManager()
    
    def save(self, *args, **kwargs):
        if not self.name:
            self.name = self.username
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.matricule 
   
    
    @property
    def is_student(self):
        return self.user_type == 'student'
    
    @property
    def is_enseignant(self):
        return self.user_type == 'enseignant'
    
    @property
    def is_scolarite(self):
        return self.user_type == 'scolarite'
    
    @property
    def is_admin(self):
        return self.is_superuser