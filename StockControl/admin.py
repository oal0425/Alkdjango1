from django.contrib import admin
from .models import Proveedor, Producto
# Register your models here.

@admin.register(Proveedor)
class ProveedorAdmin(admin.ModelAdmin):
    """ REGISTRAR EL MODELO PROVEEDOR EN EL ADMIN"""
    list_display = ('id', 'nombre', 'apellido', 'dni')
    search_fields = ('nombre','dni')


@admin.register(Producto)
class Producto(admin.ModelAdmin):
    """ REGISTRAR EL MODELO PRODUCTO EN EL ADMIN"""
    list_display = ('id', 'nombre', 'precio', 'stock_actual', 'proveedor')
    search_fields = ('nombre','proveedor')