from django.views.generic import( # type: ignore
   FormView,
   TemplateView,
   ListView) # type: ignore
from django.urls import reverse_lazy
from applications.partidos.models import Partidos
from applications.elecciones.models import Elecciones
from applications.votos.models import Votos
from .forms import VotosForm
from .forms import SeleccionarEleccionForm
from django.shortcuts import redirect
from django.urls import reverse
from django.shortcuts import get_object_or_404
from .forms import VotosPorPartidoForm

class IngresoExitoso(TemplateView):
    template_name = "votos/ingresoexitoso.html"

class SeleccionarEleccionView(FormView):
    template_name = 'votos/seleccionar_eleccion.html'
    form_class = SeleccionarEleccionForm

    def form_valid(self, form):
        eleccion = form.cleaned_data['eleccion']
        # Redirigir al listado de partidos con la elección seleccionada como parámetro
        return redirect(reverse('votos_app:partidos_por_eleccion') + f'?eleccion={eleccion.id}')

class PartidosPorEleccionView(FormView):
   template_name = 'votos/partidos_por_eleccion.html'
   form_class = VotosPorPartidoForm
   success_url = reverse_lazy('votos_app:exito')

   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      eleccion_id = self.request.GET.get('eleccion')  # Obtener la elección desde los parámetros GET
      eleccion = get_object_or_404(Elecciones, id=eleccion_id)
      partidos = Partidos.objects.filter(votos__eleccion=eleccion).distinct()
      kwargs['partidos'] = partidos  # Pasar los partidos al formulario dinámico
      self.eleccion = eleccion  # Guardar elección para usar en el contexto
      return kwargs

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['eleccion'] = self.eleccion  # Pasa la elección al contexto
      return context


   def form_valid(self, form):
      for field_name, value in form.cleaned_data.items():
            if field_name.startswith('votos_'):  # Identificar los campos dinámicos
               partido_id = int(field_name.split('_')[1])
               partido = get_object_or_404(Partidos, id=partido_id)
               # Crear o actualizar los votos en la base de datos
               Votos.objects.update_or_create(
                  partido=partido,
                  eleccion=self.eleccion,
                  defaults={'votos': value}
               )
      return super().form_valid(form)  # Redirigir al listado o página de confirmación

class RegistrarVotosView(FormView):
   template_name = 'votos/registrar_votos.html'
   form_class = VotosForm
   success_url = reverse_lazy('votos_app:exito')  # Cambia 'votos_exito' por el nombre de tu URL.

   def form_valid(self, form):
      eleccion = form.cleaned_data['eleccion']
      for field_name, value in form.cleaned_data.items():
            if field_name.startswith('votos_'):
               partido_id = int(field_name.split('_')[1])
               partido = Partidos.objects.get(id=partido_id)
               # Guardar votos en la base de datos
               Votos.objects.update_or_create(
                  eleccion=eleccion,
                  partido=partido,
                  defaults={'votos': value}
               )
      return super().form_valid(form)



