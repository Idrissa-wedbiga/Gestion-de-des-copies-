from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.translation import gettext_lazy as _
from Authentification.models import CustomUser
from django.contrib.auth import get_user_model



class EtudiantModels(CustomUser):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, related_name='etudiant_profile', default=None, blank=True, null=True)
    etudiant_filiere = models.CharField(max_length=100, default=None, verbose_name='Filière', blank=True, null=True)
    etudiant_niveau = models.CharField(max_length=5, default=None, verbose_name='Niveau', blank=True, null=True)
    etudiant_promotion = models.CharField(max_length=100, default=None, verbose_name='Promotion', blank=True, null=True)

    class Meta:
        verbose_name = "Etudiant"
        verbose_name_plural = "Etudiants"
        
    def __str__(self):
        if self.user:
            return f"{self.user.matricule} - {self.user.prenom} {self.user.name} - {self.etudiant_filiere} - {self.etudiant_promotion} - {self.etudiant_niveau}"
        return "Sans Matricule"
        
    def save(self, *args, **kwargs):
        if not self.pk and self.password:
            self.password = make_password(self.password)
        super(EtudiantModels, self).save(*args, **kwargs)
