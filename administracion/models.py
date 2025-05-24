from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    correo = models.EmailField(unique=True)
    numeroDeSemestre = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
    
class Curso(models.Model):
    nombre = models.CharField(max_length=100)
    codigo = models.CharField(max_length=10, unique=True)

    def __str__(self):
        return self.nombre    

class NotaAlumnoCurso(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    nota = models.DecimalField(max_digits=4, decimal_places=2)

    def __str__(self):
        return f"{self.alumno} - {self.curso}: {self.nota}"
