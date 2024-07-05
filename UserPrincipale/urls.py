from django.urls import path
from .import views

app_name='userprincipale'

urlpatterns=[
    path('',views.index,name='index'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    
    #Enseignant
    path('Enseignant/', views.enseignant, name='enseignant'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('editer/<str:matricule>/', views.editer, name='editer'),
    path('supprimer/<str:matricule>/', views.supprimer, name='supprimer'),
    
    #Scolarité
    path('Scolarite/', views.scolarity, name='scolarity'),
    path('sc_ajouter/', views.sc_ajouter, name='sc_ajouter'),
    path('sc_editer/<str:matricule>/', views.sc_editer, name='sc_editer'),
    path('sc_supprimer/<str:matricule>/', views.sc_supprimer, name='sc_supprimer'),
    
    #Etudiant// Afficher les etudiants sur le dashbord de l'admin
    path('Etudiant/', views.etudiant, name='etudiant'),
]