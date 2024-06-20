from django.urls import path
from django.urls import include
from .import views
from .views import CustomLoginView

app_name='Authentification'

urlpatterns = [
    #login
    path('login',CustomLoginView.as_view(), name='login'),
   
    #signup
    path('register', views.signup_view, name='signup'),
    path('logout', views.logout_view, name='logout'),
    path('',views.home, name='home'),
    # path('admin/login/', CustomLoginView.as_view(), name='login'),
]
