from django.urls import path
from .import views
app_name="ScolaritePersonal"
urlpatterns=[
    path('',views.index,name='index'),
    
]