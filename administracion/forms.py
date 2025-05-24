from django import forms
from .models import Alumno, Curso, NotaAlumnoCurso

class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = '__all__'

class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = '__all__'

class NotaAlumnoCursoForm(forms.ModelForm):
    class Meta:
        model = NotaAlumnoCurso
        fields = '__all__'