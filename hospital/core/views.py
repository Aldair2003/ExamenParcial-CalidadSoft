from django.shortcuts import render, get_object_or_404, redirect
from .models import Paciente, Doctor, Cita
from .forms import PacienteForm, DoctorForm, CitaForm

def home(request):
    return render(request, 'core/home.html')

def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'core/lista_pacientes.html', {'pacientes': pacientes})

def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'core/detalle_paciente.html', {'paciente': paciente})

def nuevo_paciente(request):
    if request.method == "POST":
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'core/nuevo_paciente.html', {'form': form})
