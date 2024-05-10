from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

#admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    # Liste des champs à afficher dans le tableau de bord de l'administrateur
    list_display = ('username','prenom','matricule','email')  

    # Champ de recherche pour le tableau de bord de l'administrateur
    search_fields = ('username','prenom','matricule','email')  
    
admin.site.register(CustomUser, CustomUserAdmin)
