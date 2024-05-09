from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('create/', views.create, name='create'),
    path('students/<int:pk>/delete/', views.delete_student, name='delete'),
]
