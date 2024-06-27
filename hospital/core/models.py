# core/models.py

from django.db import models

class Paciente(models.Model):
    nombre = models.CharField(max_length=100)
    edad = models.IntegerField()
    direccion = models.CharField(max_length=255)

    def __str__(self):
        return self.nombre

class Doctor(models.Model):
    nombre = models.CharField(max_length=100)
    especialidad = models.CharField(max_length=100)

    def __str__(self):
        return f'Doc. {self.nombre}'

class Cita(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    fecha_cita = models.DateTimeField()
    motivo = models.TextField()

    def __str__(self):
        return f'Cita con {self.doctor.nombre} para {self.paciente.nombre} el {self.fecha_cita}'
