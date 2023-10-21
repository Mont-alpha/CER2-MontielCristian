from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.





class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField
    logo = models.ImageField

class mensaje(models.Model):
    #enum de seleccion tipo mensaje (<valor int,char,etc>,<string>)
    TIPO_CHOICE = [("S","Suspención de actividades"),("C","Suspención de clase"),("I","Informaciones")]



    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField
    detalle = models.CharField
    detalle_corto = models.CharField
    tipo = models.CharField(max_length=2,
                            choices=TIPO_CHOICE, #choie usa una lista de tuplas, no objetos
                            default="I"
                            )
    entidad = models.ForeignKey(Entidad,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    visible = models.BooleanField
    fecha_publicacion = models.DateTimeField 
    fecha_ultima_modificacion = models.DateTimeField  
    #publicado_por = models.CharField(mas)
    #modificado_por =


