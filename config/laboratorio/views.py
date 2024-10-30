from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Laboratorio
from django.forms import ModelForm

class LaboratorioForm(ModelForm):
    class Meta:
        model = Laboratorio
        fields = ['nombre', 'ciudad', 'pais']

def laboratorio_list(request):
    # Manejo del contador de visitas
    visits = request.session.get('visits', 0)
    request.session['visits'] = visits + 1
    
    laboratorios = Laboratorio.objects.all()
    return render(request, 'laboratorio/laboratorio_list.html', {
        'laboratorios': laboratorios,
        'visits': visits
    })

def laboratorio_create(request):
    if request.method == 'POST':
        form = LaboratorioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list')
    else:
        form = LaboratorioForm()
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

def laboratorio_update(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        form = LaboratorioForm(request.POST, instance=laboratorio)
        if form.is_valid():
            form.save()
            return redirect('laboratorio:laboratorio_list')
    else:
        form = LaboratorioForm(instance=laboratorio)
    return render(request, 'laboratorio/laboratorio_form.html', {'form': form})

def laboratorio_delete(request, pk):
    laboratorio = get_object_or_404(Laboratorio, pk=pk)
    if request.method == 'POST':
        laboratorio.delete()
        return redirect('laboratorio:laboratorio_list')
    return render(request, 'laboratorio/laboratorio_confirm_delete.html', {'object': laboratorio})
