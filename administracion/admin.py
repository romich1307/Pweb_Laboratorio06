from django.contrib import admin
from .models import Alumno,Curso,NotaAlumnoCurso

@admin.register(Alumno)
class AlumnoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'apellido', 'dni', 'correo', 'numeroDeSemestre')
    search_fields = ('nombre', 'apellido', 'dni')
    list_filter = ('numeroDeSemestre',)

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'codigo')
    search_fields = ('nombre', 'codigo')
    
@admin.register(NotaAlumnoCurso)
class NotaAdmin(admin.ModelAdmin):
    list_display = ('id', 'alumno', 'curso', 'nota')
    list_filter = ('curso',)
    search_fields = ('alumno__nombre', 'curso__nombre')