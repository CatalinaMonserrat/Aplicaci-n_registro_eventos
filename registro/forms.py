from django import forms
from django.forms import modelformset_factory #Libreria para crear multiples formularios basados en un modelo
from django.utils import timezone
from .models import Evento, Participante

class EventoForm(forms.ModelForm):
    class Meta:
        model = Evento
        fields = ['nombre', 'ubicacion', 'fecha']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'ubicacion': forms.TextInput(attrs={'class': 'form-control'}),
        }
#MEtodo para validar que la fecha sea futura
    def clean_fecha(self):
        fecha = self.cleaned_data['fecha']
        if fecha <= timezone.localdate():
            raise forms.ValidationError("La fecha debe ser futura.")
        return fecha
    
 #Metodo para validar que el nombre tenga menos de 100 caracteres   
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        if len(nombre) > 100:
            raise forms.ValidationError("El nombre debe tener menos de 100 caracteres.")
        return nombre
    
class ParticipanteForm(forms.ModelForm):
    class Meta:
        model = Participante
        fields = ['nombre', 'email']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

#Conjunto de formularios para manejar varios participantes a la vez
ParticipanteFormSet = modelformset_factory(Participante, form=ParticipanteForm, extra=3, validate_min=True)