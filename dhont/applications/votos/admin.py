from django.contrib import admin
from .models import Votos

class VotosAdmin(admin.ModelAdmin):
    list_display = (
        'votos',
        'eleccion',
        'partido',
    )

# Registra el modelo usando la clase personalizada VotosAdmin
admin.site.register(Votos, VotosAdmin)
