from django.urls import path
from .import views
app_name="Etudiant"
urlpatterns=[
    path('',views.index,name='index'),
    
]