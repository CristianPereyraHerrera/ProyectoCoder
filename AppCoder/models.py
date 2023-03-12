from django.db import models

class Inicio(models.Model):
    logo = models.Index


class Curso(models.Model):
    nombre = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)

    def __str__(self):
        return f"Curso: {self.nombre} {self.camada}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    curso = models.CharField(max_length=40)
    camada = models.IntegerField(unique=True)
    fecha_de_entrega = models.DateField()
    entregado = models.BooleanField()

    def __str__(self):
        return f"Entregable: {self.nombre} {self.apellido} {self.curso} {self.camada} {self.fecha_de_entrega} {self.entregado}"


class Estudiante(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return f"Estudiante: {self.nombre} {self.apellido}"


class Profesor(models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)
    email = models.EmailField()
    profesion = models.CharField(max_length=30)

    def __str__(self):
        return f"Profesor: {self.nombre} {self.apellido}"


