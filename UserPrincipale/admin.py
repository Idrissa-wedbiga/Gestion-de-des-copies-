from django.contrib import admin
from .models import CustomUser,ScolariteModels


class ScolariteModelsAdmin(admin.ModelAdmin):

    list_display = ('matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email')
    
    search_fields = ('matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email')

admin.site.register(ScolariteModels, ScolariteModelsAdmin)
