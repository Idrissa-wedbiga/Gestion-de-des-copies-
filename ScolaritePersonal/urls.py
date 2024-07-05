from django.urls import path
from .import views
app_name="ScolaritePersonal"
urlpatterns=[
    path('',views.index,name='index'),
    path('envoyer',views.envoyer,name='envoyer'),
    path('copie_corrigee',views.copie_corrigee,name='copie_corrigee'),
    path('copie_envoyee',views.copie_envoyee,name='copie_envoyee'),
    path('Profil',views.Profil,name='Profil'),
    path('get_enseignant_details/', views.get_enseignant_details, name='get_enseignant_details'),
    path('send_student',views.upload_and_link_files,name='send_student'),
    path('statistiq',views.statistiques_enseignant,name='statistiq'),
]