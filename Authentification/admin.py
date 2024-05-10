from django.contrib import admin
from .models import CustomUser
from django.contrib.auth.admin import UserAdmin

# Register your models here.


#admin.site.register(CustomUser)

class CustomUserAdmin(UserAdmin):
    # Liste des champs à afficher dans le tableau de bord de l'administrateur
    list_display = ('username','prenom','matricule','email')  # Ajoutez les champs que vous souhaitez afficher

    # Champ de recherche pour le tableau de bord de l'administrateur
    search_fields = ('username','prenom','matricule','email')  # Ajoutez les champs que vous souhaitez inclure dans la recherche
    
#admin.site.register(CustomUser, CustomUserAdmin)
