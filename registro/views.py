from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import transaction
from .forms import EventoForm, ParticipanteFormSet 
from .models import Participante

@transaction.atomic
def registrar_evento(request):
    if request.method == 'POST':
        evento_form = EventoForm(request.POST)
        formset = ParticipanteFormSet(request.POST, queryset=Participante.objects.none())
        if evento_form.is_valid() and formset.is_valid():
            evento = evento_form.save()
            for form in formset:
                if form.cleaned_data and not form.cleaned_data.get("DELETE", False):
                    p = form.save(commit=False)
                    p.evento = evento
                    p.save()
            messages.success(request, "¡Evento registrado con éxito!")
            return redirect('registro_exito')
        else:
            messages.error(request, "Revisa los errores del formulario.")
    else:
        evento_form = EventoForm()
        formset = ParticipanteFormSet(queryset=Participante.objects.none())  # <-- aquí
    return render(request, 'registro/registrar_evento.html', {'evento_form': evento_form, 'formset': formset})

def registro_exitoso(request):
    return render(request, "registro/registro_exitoso.html")