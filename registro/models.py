from django.db import models

class Evento(models.Model):
    nombre = models.CharField(max_length=100)
    ubicacion = models.CharField(max_length=200, blank=True)
    fecha = models.DateField()

    def __str__(self):
        return f"{self.nombre} ({self.fecha})"
    
class Participante(models.Model):
    nombre = models.CharField(max_length=100)
    email = models.EmailField()
    evento = models.ForeignKey(Evento, on_delete=models.CASCADE, related_name='participantes')

    def __str__(self):
        return f"{self.nombre} <{self.email}>"