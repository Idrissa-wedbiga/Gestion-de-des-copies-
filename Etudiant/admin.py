from django.contrib import admin
from Etudiant.models import EtudiantModels
from Authentification.models import CustomUser
# Register your models here.
class EtudiantModelAdmin(admin.ModelAdmin):
    list_display = ('matricule','username','prenom','etudiant_filiere','etudiant_niveau','etudiant_promotion','email')
    
    search_fields = ('matricule','username','prenom','etudiant_filiere','etudiant_niveau','etudiant_promotion','email')

admin.site.register(EtudiantModels, EtudiantModelAdmin)