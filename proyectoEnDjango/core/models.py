from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.timezone import datetime
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.



#modelo -> tabla 
#creacion de objeto -> fila de la tabla (modelo)

class Entidad(models.Model):
    id = models.BigAutoField(primary_key=True)
    nombre = models.CharField(max_length=100,default="")
    logo = models.ImageField(null=True,blank=True) #la imagen se sube posteriormente
    def __str__(self): #para identifiarse mejor en el administrador
        return self.nombre

class mensaje(models.Model):
    #enum de seleccion tipo mensaje (<valor int,char,etc>,<string>)
    TIPO_CHOICE = [("S","Suspención de actividades"),("C","Suspención de clase"),("I","Informaciones")]



    id = models.BigAutoField(primary_key=True)
    titulo = models.CharField(max_length=100,null=True)
    detalle = models.CharField(max_length=1000,null=True)
    detalle_corto = models.CharField(max_length=100,null=True)
    tipo = models.CharField(max_length=2,
                            choices=TIPO_CHOICE, #choie usa una lista de tuplas, no objetos
                            default="I"
                            )
    entidad = models.ForeignKey(Entidad,
                                null=False,
                                blank=False,
                                on_delete=models.CASCADE)
    visible = models.BooleanField(default=True)
    fecha_publicacion = models.DateTimeField(default=datetime.now)
    fecha_ultima_modificacion = models.DateTimeField(default=datetime.now)
    #publicado_por = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    #modificado_por = models.ForeignKey(User,models.SET_NULL,blank=True,null=True)
    
    def __str__(self): #para identifiarse mejor en el administrador
        return self.titulo 





