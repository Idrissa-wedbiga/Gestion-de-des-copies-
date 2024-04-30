from django.urls import path
from .import views
app_name="Enseignant"
urlpatterns=[
    path('',views.index,name='index'),
    path('enseigant_profile',views.enseigant_profile,name='enseigant_profile'),
    path('Composer',views.Composer,name='Composer'),
    path('Envoyer',views.Envoyer,name='Envoyer'),
    path('Corriger',views.Corriger,name='Corriger'),
]