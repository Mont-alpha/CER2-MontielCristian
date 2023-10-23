from django.shortcuts import render
from django.http import HttpResponse
from .models import *

# Create your views here.

def index(request):
    entidades = Entidad.objects.all() # obetener los nombres de las entidades para luego darselo al dropdown
    comunicados = mensaje.objects.all()
    #ordenarlas de mas reciente a mas antigua     
    data = {"lista": entidades,"mensaje":comunicados}            
    return render(request,"complemento.html",data)

def filtrar(request,buscar):
    #ordenarlas de mas reciente a mas antigua
    entidades = Entidad.objects.all()
    mensajes_buscados = mensaje.objects.filter(entidad=buscar)
    data = {"lista": entidades,"mensaje":mensajes_buscados} #solo muestra los mensajes de la entidad correspondiente
    return render(request,"complemento.html",data) #agregar comunicado_filtrado


