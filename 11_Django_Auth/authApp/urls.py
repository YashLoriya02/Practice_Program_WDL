from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('home_login/', views.home_login , name='home_login'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
]
