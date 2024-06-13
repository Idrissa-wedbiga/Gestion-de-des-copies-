from django.contrib import admin

from Enseignant.models import EnseignantModels
from ScolaritePersonal.models import ScolariteModels


class ScolariteModelsAdmin(admin.ModelAdmin):

    list_display = ('matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email')
    
    search_fields = ('matricule', 'username', 'prenom', 'fonction', 'etablissement', 'email')
    actions = ['supprimer_scolarite']
    
    def supprimer_scolarite(self, request, queryset):
        for scolarite in queryset:
            scolarite.delete()
        self.message_user(request, "Les scolarités sélectionnées ont été supprimées avec succès.")


admin.site.register(ScolariteModels, ScolariteModelsAdmin)

class EnseignantModelsAdmin(admin.ModelAdmin):

    list_display = ('matricule', 'username', 'prenom', 'specialite', 'email')
    
    search_fields = ('matricule', 'username', 'prenom', 'specialite', 'email')

admin.site.register(EnseignantModels, EnseignantModelsAdmin)
