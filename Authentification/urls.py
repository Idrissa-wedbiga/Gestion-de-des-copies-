from django.urls import path
from django.urls import include
from .import views
app_name='Authentification'

urlpatterns = [
    #login
    path('', authentication.views.login_page.as_view(), name='login'),

    #logout
]
