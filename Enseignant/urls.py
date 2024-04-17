from django.urls import path
from .import views
app_name="Enseignant"
urlpatterns=[
    path('',views.index,name='index'),
    
]