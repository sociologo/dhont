from django import forms
from .models import Partidos, Elecciones, Votos

class SeleccionarEleccionForm(forms.Form):
   eleccion = forms.ModelChoiceField(
      queryset=Elecciones.objects.all(),
      label="Selecciona una elección",
      required=True
   )
"""    escanos_totales = forms.IntegerField(
      label="Número total de escaños",
      min_value=1,
      required=True,  # Obligatorio para garantizar que se ingrese un valor
   ) """

class VotosPorPartidoForm(forms.Form):
   def __init__(self, *args, **kwargs):
      partidos = kwargs.pop('partidos', [])
      super().__init__(*args, **kwargs)
      for partido in partidos:
            self.fields[f'votos_{partido.id}'] = forms.IntegerField(
               label=partido.nombre,
               min_value=0,
               required=False  # Permitir campos vacíos si no se ingresan votos
   )
   # Campo adicional para el número total de escaños
      self.fields['escanos_totales'] = forms.IntegerField(
         label="Número total de escaños",
         min_value=1,
         required=True  # Obligatorio para garantizar que se ingrese un valor
      )