from django.db import models

# Create your models here.

class Persona(models.Model):
	nombre = models.CharField(max_length = 50)
	apellido = models.CharField(max_length = 50)
	edad = models.IntegerField()
	telefono =models.CharField(max_length = 10)
	email = models.EmailField()
	domicilio = models.CharField(max_length = 50)