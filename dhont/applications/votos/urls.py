from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

app_name = "votos_app"

urlpatterns = [
      path('ingreso-exitoso', 
      views.IngresoExitoso.as_view(), 
      name = 'exito'),
      path('seleccionar-eleccion/', 
      views.SeleccionarEleccionView.as_view(),),
      path('partidos/', 
      views.PartidosPorEleccionView.as_view(), 
      name='partidos_por_eleccion'),
      path('resultados/', 
      views.AsignarEscanosView.as_view(), 
      name='resultados_por_eleccion'),
      path('resultados/', 
      views.AsignarEscanosView.as_view(), 
      name='resultados_por_eleccion'),
      path('calcular-escanos/', 
      views.CalcularEscanosView.as_view(), 
      name='calcular_escanos'),
]