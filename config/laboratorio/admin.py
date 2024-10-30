from django.contrib import admin
from .models import Laboratorio, DirectorGeneral, Producto

@admin.register(Laboratorio)
class LaboratorioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre')
    search_fields = ['nombre']

@admin.register(DirectorGeneral)
class DirectorGeneralAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio')
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'laboratorio', 'f_fabricacion', 'p_costo', 'p_venta')
    list_filter = ['nombre', 'laboratorio']
    search_fields = ['nombre']