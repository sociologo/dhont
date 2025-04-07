from django.db import models

class Partidos(models.Model):
   nombre = models.CharField("Nombre", max_length=50)
   siglas = models.CharField("Nombre", max_length=50)

   def __str__(self):
      return self.nombre + "-" + self.siglas