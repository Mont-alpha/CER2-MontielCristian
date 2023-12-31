

"""
URL configuration for proyectoPrueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views #toma las funciones que se contengan en views de la aplicacion core

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name="inicio"),
    path("<int:buscar>/",views.filtrar,name="filtrado") #recibe el parametro entidad.id , buscar recibe lo que hay en la url : /1/ -> buscar = 1

]


admin.site.index_title = "Modelos"
admin.site.site_header = 'Sistema integrado de gestión'
admin.site.site_title = 'Administración'