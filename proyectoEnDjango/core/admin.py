from typing import Any
from django.contrib import admin
from django.db.models.query import QuerySet
from django.http.request import HttpRequest
from django.utils.timezone import datetime
from .models import Entidad,mensaje


# Register your models here. -> sitio de administracion
class mensajeAdmin(admin.ModelAdmin):
    list_display = ('detalle_corto', 'fecha_publicacion', "entidad","publicado_por","modificado_por") #se me va mostrar esos dos campos del modelo al momento de gestionar mas objetos
    ordering = ('-fecha_publicacion',) #ordena descendentementen por el '-'
    def save_model(self, request: Any, objeto_retorno: Any , form: Any, change: Any) -> None:
        if not change: #ve si no hay cambio
            objeto_retorno.publicado_por = request.user #el request hace peticion a la pagina de administrador para obtener el usuario y lo guarda
            objeto_retorno.fecha_publicacion = datetime.now()
            return super().save_model(request, objeto_retorno, form, change)
        else:
            objeto_retorno.modificado_por = request.user
            objeto_retorno.fecha_ultima_modificacion = datetime.now()
            return super().save_model(request, objeto_retorno, form, change)
    
    def get_exclude(self, request: HttpRequest, objeto_retorno: Any | None = ...) -> Any:
        if not request.user.is_superuser:
            return ("fecha_publicacion","fecha_ultima_modificacion") #no puede ver estos campos
        return None
class entidadAdminsite(admin.ModelAdmin):
    list_display = ('id', 'nombre') #se me va mostrar esos dos campos del modelo al momento de gestionar mas objetos







        


admin.site.register(mensaje,mensajeAdmin)
admin.site.register(Entidad,entidadAdminsite)

    


