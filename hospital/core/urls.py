from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.nuevo_paciente, name='nuevo_paciente'),
    path('pacientes/<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
]
