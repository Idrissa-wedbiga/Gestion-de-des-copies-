from django.urls import path
from .import views
app_name="ScolaritePersonal"
urlpatterns=[
    path('',views.index,name='index'),
    path('envoyer',views.envoyer,name='envoyer'),
    path('copie_corrigee',views.copie_corrigee,name='copie_corrigee'),
    path('Profil',views.Profil,name='Profil'),
    
]