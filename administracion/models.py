from django.db import models

class Alumno(models.Model):
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    dni = models.CharField(max_length=8, unique=True)
    correo = models.EmailField(unique=True)
    numeroDeSemestre = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.nombre} {self.apellido}"
# Create your models here.
