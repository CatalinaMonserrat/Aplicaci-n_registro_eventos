from django.shortcuts import render, redirect
from django.contrib import menssages
from django.forms import modelformset_factory
from django.db import transaction
from .forms import EventoForm, ParticipanteForm, ParticipanteFormSet
from .models import Evento, Participante

# Create your views here.
@transaction.atomic
def registrar_evento(request):
    ParticipanteFormSet = modelformset_factory(Participante, form=ParticipanteForm, extra=1, can_delete=True, validate_min=True)
    
    if request.method == "POST":
        evento_form = EventoForm(request.POST)
        formset = ParticipanteFormSet(request.POST, queryset=Participante.objects.none())
        
        if evento_form.is_valid() and formset.is_valid():
            evento = evento_form.save() #Guardamos el evento primero
            for form in formset: #Luego guardamos los participantes asociandolos al evento
                if form.cleaned_data and not form.cleaned_data.get["DELETE", False]:
                    participante = form.save(commit=False)
                    participante.evento = evento
                    participante.save()
            menssages.success(request, "¡Evento registrado exitosamente!")
            return redirect('registro_exitoso')
        else:
            menssages.error(request, "Revisa los errores del formulario")
    else:
        evento_form = EventoForm()
        formset = ParticipanteFormSet(queryset=Participante.objects.none())

    return render(request, "registro/registrar_evento.html", {'evento_form': evento_form, "formset": formset})

def registro_exitoso(request):
    return render(request, "registro/registro_exitoso.html")