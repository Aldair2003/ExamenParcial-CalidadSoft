from django import forms
from .models import Paciente, Doctor, Cita

class PacienteForm(forms.ModelForm):
    class Meta:
        model = Paciente
        fields = ['nombre', 'edad', 'direccion']
        widgets = {
            'direccion': forms.Textarea(attrs={'rows': 2}),
        }

class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = ['nombre', 'especialidad']

class CitaForm(forms.ModelForm):
    class Meta:
        model = Cita
        fields = ['paciente', 'doctor', 'fecha_cita', 'motivo']
        widgets = {
            'fecha_cita': forms.DateInput(attrs={'class': 'form-control', 'placeholder': 'Fecha de la cita'}),
            'motivo': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
        }
