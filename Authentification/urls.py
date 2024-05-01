from django.urls import path
from django.urls import include
from .import views
app_name='Authentification'

urlpatterns = [
    #login
    path('',views.login_view, name='login'),

    #logout
    #path('logout', views.logout_view, name='logout'),

    #signup
    path('register', views.signup_view, name='signup'),
]
