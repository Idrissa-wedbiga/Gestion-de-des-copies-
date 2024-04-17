from django.urls import path
from django.urls import include
from .import views
app_name='userprincipale'

urlpatterns=[
    path('',views.index,name='index'),
    #path('dashboard/', views.dashboard, name='dashboard'),
    #path('abonnes/', views.abonnes, name='abonnes'),
    path('Scolarite/', views.scolarity, name='scolarity'),
    path('Enseignant/', views.enseignant, name='enseignant'),
    path('usersprofile/', views.usersprofile, name='usersprofile'),
    path('ajouter/', views.ajouter, name='ajouter'),
    path('editer/', views.editer, name='editer'),
    path('login/', views.login, name='login'),
    path('login/', include('django.contrib.auth.urls')),
]