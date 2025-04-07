from django.contrib import admin # type: ignore
from django.urls import path, include # type: ignore
from . import views

app_name = "votos_app"

urlpatterns = [
      path('registrar-votos/', 
      views.RegistrarVotosView.as_view(), 
      name='registrar_votos'),
      path('ingreso-exitoso', 
      views.IngresoExitoso.as_view(), 
      name = 'exito'),
      path('seleccionar-eleccion/', 
      views.SeleccionarEleccionView.as_view(),),
      path('partidos/', 
      views.PartidosPorEleccionView.as_view(), 
      name='partidos_por_eleccion'),
]