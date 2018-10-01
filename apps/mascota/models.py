from django.db import models
from apps.adopcion.models import Persona

# Create your models here.
class Vacuna(models.Model):
	nombre = models.CharField(max_length = 50)

class Mascota(models.Model):
	persona = models.ForeignKey(Persona,null=True,blank=True,on_delete=models.CASCADE)
	vacuna = models.ManyToManyField(Vacuna)
	nombre = models.CharField(max_length=5)
	sexo = models.CharField(max_length=5)
	edad_aproximada = models.IntegerField()
	fecha_rescate = models.DateField()
