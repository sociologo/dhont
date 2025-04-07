from django.db import models
from datetime import date

class Elecciones(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   fecha = models.DateField("Fecha", default=date.today)

   def __str__(self):
      return str(self.nombre) + "-" + str(self.fecha)
