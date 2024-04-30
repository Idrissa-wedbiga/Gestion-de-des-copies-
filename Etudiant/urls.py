from django.urls import path
from .import views
app_name="Etudiant"
urlpatterns=[
    path('',views.index,name='index'),
    path('Mes_copies',views.Mes_copies,name='Mes_copies'),
    path('Fichier_Personnel',views.Fichier_Personnel,name='Fichier_Personnel'),
    path('Profil',views.Profil,name='Profil'),
    
]