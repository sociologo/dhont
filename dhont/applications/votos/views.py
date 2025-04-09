from django.views.generic import( # type: ignore
   FormView,
   TemplateView,
   ListView,
   View) # type: ignore
from django.urls import reverse, reverse_lazy
from applications.partidos.models import Partidos
from applications.elecciones.models import Elecciones
from applications.votos.models import Votos
from applications.escanos.models import Escanos
from .forms import SeleccionarEleccionForm, VotosPorPartidoForm
from django.shortcuts import redirect, render, get_object_or_404
from django.db.models import Sum

class IngresoExitoso(TemplateView):
    template_name = "votos/ingresoexitoso.html"

class SeleccionarEleccionView(FormView):
    template_name = 'votos/seleccionar_eleccion.html'
    form_class = SeleccionarEleccionForm

    def form_valid(self, form):
        # Capturar solo el valor de 'eleccion' desde los datos del formulario
        eleccion = form.cleaned_data['eleccion']
        print(f"Elección seleccionada: {eleccion.nombre}")  # Depuración

        # Redirigir al listado de partidos con la elección seleccionada como parámetro
        return redirect(reverse('votos_app:partidos_por_eleccion') + f'?eleccion={eleccion.id}')

class PartidosPorEleccionView(FormView):
   
   template_name = 'votos/partidos_por_eleccion.html'
   form_class = VotosPorPartidoForm
   success_url = reverse_lazy('votos_app:exito')

   def get_form_kwargs(self):
      kwargs = super().get_form_kwargs()
      eleccion_id = self.request.GET.get('eleccion')  # Obtener elección desde los parámetros GET
      eleccion = get_object_or_404(Elecciones, id=eleccion_id)
      partidos = Partidos.objects.filter(votos__eleccion=eleccion).distinct()

      # Solo pasa los partidos al formulario, pero no 'escanos_totales'
      kwargs['partidos'] = partidos
      self.eleccion = eleccion  # Guarda elección para el contexto
      return kwargs

   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context['eleccion'] = self.eleccion  # Pasa la elección al contexto
      return context

   def form_valid(self, form):
      print("Iniciando procesamiento de votos", flush=True)
      # Capturar el número de escaños desde el formulario
      escanos_totales = form.cleaned_data['escanos_totales']
      print(f"Escaños totales a repartir: {escanos_totales}", flush=True)
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
               # Mostrar en consola los votos asignados
               print(f"Partido: {partido.nombre}, Votos asignados: {value}")
      # return super().form_valid(form)  # Redirigir al listado o página de confirmación
      
      

      # Llamar al cálculo de escaños
      self.calcular_escanos(self.eleccion, escanos_totales)



      return redirect(reverse('votos_app:resultados_por_eleccion') + f'?eleccion={self.eleccion.id}')



   def calcular_escanos(self, eleccion, escanos_totales):
      # Calcular votos totales por partido
      votos_partidos = {
         partido: Votos.objects.filter(eleccion=eleccion, partido=partido).aggregate(
               total=Sum('votos')
         )['total'] or 0
         for partido in Partidos.objects.all()
      }

      # Aplicar el método D'Hondt
      asignaciones = {partido: 0 for partido in votos_partidos}
      divisores = {
         partido: [votos // divisor for divisor in range(1, escanos_totales + 1)]
         for partido, votos in votos_partidos.items()
      }

      for _ in range(escanos_totales):
         partido_max = max(divisores.keys(), key=lambda p: divisores[p][0])
         asignaciones[partido_max] += 1
         divisores[partido_max].pop(0)

      # Guardar los resultados en la base de datos
      for partido, escanos in asignaciones.items():
         Escanos.objects.update_or_create(
               eleccion=eleccion,
               partido=partido,
               defaults={'escanos': escanos}
         )










class CalcularEscanosView(View):

   def post(self, request, *args, **kwargs):
      form = SeleccionarEleccionForm(request.POST)

      if form.is_valid():
         eleccion = form.cleaned_data['eleccion']
         escanos_totales = form.cleaned_data['escanos_totales']

         # Calcular votos totales por partido
         votos_partidos = {
               partido: Votos.objects.filter(eleccion=eleccion, partido=partido).aggregate(
                  total=Sum('votos')
               )['total'] or 0
               for partido in Partidos.objects.all()
         }

         # Aplicar el método D'Hondt
         asignaciones = {partido: 0 for partido in votos_partidos}
         divisores = {
               partido: [votos // divisor for divisor in range(1, escanos_totales + 1)]
               for partido, votos in votos_partidos.items()
         }

         for _ in range(escanos_totales):
               partido_max = max(divisores.keys(), key=lambda p: divisores[p][0])
               asignaciones[partido_max] += 1
               divisores[partido_max].pop(0)

         # Guardar resultados en la base de datos
         for partido, escanos in asignaciones.items():
               Escanos.objects.update_or_create(
                  eleccion=eleccion,
                  partido=partido,
                  defaults={'escanos': escanos}
               )

         # Redirigir a resultados
         return redirect(reverse('resultados_por_eleccion') + f'?eleccion={eleccion.id}')

      # Si el formulario no es válido, renderizar con errores
      return render(request, self.template_name, {'form': form})
   





class AsignarEscanosView(ListView):
   model = Escanos
   template_name = 'votos/asignar_escanos.html'
   context_object_name = 'escanos'

   def get_queryset(self):
      # Validar el parámetro 'eleccion'
      eleccion_id = self.request.GET.get('eleccion')
      if not eleccion_id:
         raise ValueError("Falta el parámetro 'eleccion' en la URL.")
      self.eleccion = get_object_or_404(Elecciones, id=eleccion_id)

      queryset = Escanos.objects.filter(eleccion=self.eleccion)
      print(f"Escanos asociados: {queryset}")  # Imprime el queryset en la consola para depuración
      return queryset

   def get_context_data(self, **kwargs):
      # Pasar datos adicionales al contexto
      context = super().get_context_data(**kwargs)
      context['eleccion'] = self.eleccion
      return context

