from django import forms
from .models import Paciente, Doctor, Cita

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2}),
        }
        labels = {
            'nombre': 'Nombre:',
            'edad': 'Edad:',
            'direccion': 'Dirección:',
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad']
        labels = {
            'nombre': 'Nombre:',
            'especialidad': 'Especialidad:',
        }

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'doctor', 'fecha_cita', 'motivo']
        widgets = {
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'motivo': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
        labels = {
            'paciente': 'Paciente:',
            'doctor': 'Doctor:',
            'fecha_cita': 'Fecha de la cita:',
            'motivo': 'Motivo:',
        }

    def __init__(self, *args, **kwargs):
        super(CitaForm, self).__init__(*args, **kwargs)
        for field in self.fields.values():
            field.required = False
