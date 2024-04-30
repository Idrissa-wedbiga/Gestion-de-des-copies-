from django.urls import path
from django.urls import include
from .import views
app_name='userprincipale'

urlpatterns=[
    path('',views.index,name='index'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    #Enseignant
    path('Enseignant/', views.enseignant, name='enseignant'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('editer/', views.editer, name='editer'),
    #Scolarité
    path('Scolarite/', views.scolarity, name='scolarity'),
    path('sc_ajouter', views.sc_ajouter, name='sc_ajouter'),
    path('sc_editer', views.sc_editer, name='sc_editer'),
    #login
    path('login/', views.login_page, name='login'),
    path('login/', include('django.contrib.auth.urls')),
]