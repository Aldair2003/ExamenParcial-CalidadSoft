from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('pacientes/', views.lista_pacientes, name='lista_pacientes'),
    path('pacientes/nuevo/', views.nuevo_paciente, name='nuevo_paciente'),
    path('pacientes/<int:pk>/', views.detalle_paciente, name='detalle_paciente'),
    path('pacientes/<int:pk>/editar/', views.editar_paciente, name='editar_paciente'),
    path('pacientes/<int:pk>/eliminar/', views.eliminar_paciente, name='eliminar_paciente'),
    path('doctores/', views.lista_doctores, name='lista_doctores'),
    path('doctores/nuevo/', views.nuevo_doctor, name='nuevo_doctor'),
    path('doctores/<int:pk>/', views.detalle_doctor, name='detalle_doctor'),
    path('doctores/<int:pk>/editar/', views.editar_doctor, name='editar_doctor'),
    path('doctores/<int:pk>/eliminar/', views.eliminar_doctor, name='eliminar_doctor'),
    path('citas/', views.lista_citas, name='lista_citas'),
    path('citas/nueva/', views.nueva_cita, name='nueva_cita'),
    path('citas/<int:pk>/', views.detalle_cita, name='detalle_cita'),
    path('citas/<int:pk>/editar/', views.editar_cita, name='editar_cita'),
    path('citas/<int:pk>/eliminar/', views.eliminar_cita, name='eliminar_cita'),
]
