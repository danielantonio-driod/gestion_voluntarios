from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Voluntario, Evento
from .forms import VoluntarioForm, EventoForm

def index(request):
    return render(request, 'index.html')

@login_required
def voluntario_list(request):
    voluntarios = Voluntario.objects.all()
    return render(request, 'voluntarios/voluntario_list.html', {'voluntarios': voluntarios})

@login_required
def evento_list(request):
    eventos = Evento.objects.all()
    return render(request, 'eventos/evento_list.html', {'eventos': eventos})

@login_required
def voluntario_detail(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    return render(request, 'voluntarios/voluntario_detail.html', {'voluntario': voluntario})

@login_required
def evento_detail(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    return render(request, 'eventos/evento_detail.html', {'evento': evento})

@login_required
def voluntario_create(request):
    if request.method == 'POST':
        form = VoluntarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('voluntario_list')
    else:
        form = VoluntarioForm()
    return render(request, 'voluntarios/voluntario_form.html', {'form': form})

@login_required
def evento_create(request):
    if request.method == 'POST':
        form = EventoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm()
    return render(request, 'eventos/evento_form.html', {'form': form})

@login_required
def voluntario_update(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        form = VoluntarioForm(request.POST, instance=voluntario)
        if form.is_valid():
            form.save()
            return redirect('voluntario_list')
    else:
        form = VoluntarioForm(instance=voluntario)
    return render(request, 'voluntarios/voluntario_form.html', {'form': form})

@login_required
def evento_update(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        form = EventoForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('evento_list')
    else:
        form = EventoForm(instance=evento)
    return render(request, 'eventos/evento_form.html', {'form': form})

@login_required
def voluntario_delete(request, pk):
    voluntario = get_object_or_404(Voluntario, pk=pk)
    if request.method == 'POST':
        voluntario.delete()
        return redirect('voluntario_list')
    return render(request, 'voluntarios/voluntario_confirm_delete.html', {'voluntario': voluntario})

@login_required
def evento_delete(request, pk):
    evento = get_object_or_404(Evento, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('evento_list')
    return render(request, 'eventos/evento_confirm_delete.html', {'evento': evento})
