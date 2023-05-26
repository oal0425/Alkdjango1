from django.urls import path
from StockControl import views

urlpatterns = [
    path('',views.index),
    path('productos/agregar', views.agregar_producto),
    path('proveedores/agregar', views.agregar_proveedor),
    path ('proveedores/listado', views.proveedores),
    path ('productos/listado', views.productos),
]