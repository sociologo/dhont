from django.db import models
from applications.elecciones.models import Elecciones
from applications.partidos.models import Partidos

class Votos(models.Model):
   votos = models.IntegerField()
   eleccion = models.ForeignKey(Elecciones, on_delete=models.CASCADE)
   partido = models.ForeignKey(Partidos, on_delete=models.CASCADE)

   def __str__(self):
      return str(self.votos) 
