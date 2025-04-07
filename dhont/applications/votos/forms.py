from django import forms
from .models import Partidos, Elecciones, Votos

class SeleccionarEleccionForm(forms.Form):
    eleccion = forms.ModelChoiceField(
        queryset=Elecciones.objects.all(),
        label="Selecciona una elección",
        required=True
    )

class VotosForm(forms.Form):
   eleccion = forms.ModelChoiceField(
      queryset=Elecciones.objects.all(),
      label="Elección",
      required=True
   )

   def __init__(self, *args, **kwargs):
      super().__init__(*args, **kwargs)
      partidos = Partidos.objects.all()
      for partido in partidos:
            self.fields[f'votos_{partido.id}'] = forms.IntegerField(
               label=f"{partido.nombre} ({partido.siglas})",
               min_value=0,
               required=True
   )

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
