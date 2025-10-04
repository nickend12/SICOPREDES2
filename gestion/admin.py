from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Colegio, Estudiante, Asistencia

@admin.register(Colegio)
class ColegioAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo_dane', 'ubicacion')
    search_fields = ('nombre', 'codigo_dane')

@admin.register(Estudiante)
class EstudianteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellidos', 'fecha_nacimiento', 'colegio', 'grado')
    list_filter = ('colegio', 'grado')
    search_fields = ('nombre', 'apellidos')

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('estudiante', 'fecha', 'estado')
    list_filter = ('fecha', 'estado', 'estudiante__colegio')

# Registra tus otros modelos como de costumbre
