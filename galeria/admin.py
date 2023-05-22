from django.contrib import admin
from.models import Galeria

# Register your models here.
class GaleriasAdmin(admin.ModelAdmin):
    readonly_fields=("creado", "actualizado")
    list_display = ('imagen', 'titulo', 'descripcion', 'precio')

admin.site.register(Galeria, GaleriasAdmin)

