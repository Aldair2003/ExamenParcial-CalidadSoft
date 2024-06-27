from django.shortcuts import render, redirect, get_object_or_404
from .models import Paciente, Doctor, Cita
from .forms import PacienteForm, DoctorForm, CitaForm
from django.utils.dateformat import DateFormat

# Vista Home
def home(request):
    return render(request, 'core/home.html')

# Vistas de Pacientes
def lista_pacientes(request):
    pacientes = Paciente.objects.all()
    return render(request, 'core/lista_pacientes.html', {'pacientes': pacientes})

def nuevo_paciente(request):
    if request.method == 'POST':
        form = PacienteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm()
    return render(request, 'core/nuevo_paciente.html', {'form': form})

def editar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        form = PacienteForm(request.POST, instance=paciente)
        if form.is_valid():
            form.save()
            return redirect('lista_pacientes')
    else:
        form = PacienteForm(instance=paciente)
    return render(request, 'core/editar_paciente.html', {'form': form})

def eliminar_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    if request.method == 'POST':
        paciente.delete()
        return redirect('lista_pacientes')
    return render(request, 'core/eliminar_paciente.html', {'paciente': paciente})

def detalle_paciente(request, pk):
    paciente = get_object_or_404(Paciente, pk=pk)
    return render(request, 'core/detalle_paciente.html', {'paciente': paciente})

# Vistas de Doctores
def lista_doctores(request):
    doctores = Doctor.objects.all()
    return render(request, 'core/lista_doctores.html', {'doctores': doctores})

def nuevo_doctor(request):
    if request.method == 'POST':
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_doctores')
    else:
        form = DoctorForm()
    return render(request, 'core/nuevo_doctor.html', {'form': form})

def editar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        form = DoctorForm(request.POST, instance=doctor)
        if form.is_valid():
            form.save()
            return redirect('lista_doctores')
    else:
        form = DoctorForm(instance=doctor)
    return render(request, 'core/editar_doctor.html', {'form': form})

def eliminar_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    if request.method == 'POST':
        doctor.delete()
        return redirect('lista_doctores')
    return render(request, 'core/eliminar_doctor.html', {'doctor': doctor})

def detalle_doctor(request, pk):
    doctor = get_object_or_404(Doctor, pk=pk)
    return render(request, 'core/detalle_doctor.html', {'doctor': doctor})

# Vistas de Citas
def lista_citas(request):
    citas = Cita.objects.all()
    formatted_citas = [
        {
            'pk': cita.pk,
            'paciente': cita.paciente,
            'doctor': cita.doctor,
            'fecha_cita': DateFormat(cita.fecha_cita).format('Y-m-d'),
            'motivo': cita.motivo,
        }
        for cita in citas
    ]
    return render(request, 'core/lista_citas.html', {'citas': formatted_citas})

def nueva_cita(request):
    if request.method == 'POST':
        form = CitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm()
    return render(request, 'core/nueva_cita.html', {'form': form})

def editar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        form = CitaForm(request.POST, instance=cita)
        if form.is_valid():
            form.save()
            return redirect('lista_citas')
    else:
        form = CitaForm(instance=cita)
    return render(request, 'core/editar_cita.html', {'form': form})

def eliminar_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    if request.method == 'POST':
        cita.delete()
        return redirect('lista_citas')
    return render(request, 'core/eliminar_cita.html', {'cita': cita})

def detalle_cita(request, pk):
    cita = get_object_or_404(Cita, pk=pk)
    return render(request, 'core/detalle_cita.html', {'cita': cita})
