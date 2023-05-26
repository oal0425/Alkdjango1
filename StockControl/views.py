from django.shortcuts import render,redirect, get_object_or_404
from django.http import HttpResponse
from StockControl.models import Proveedor,Producto
from .forms import ProveedorForm, ProductoForm

# Create your views here.

def agregar_producto (request):
    form = ProductoForm()

    if request.method == 'POST':
        form = ProductoForm(request.POST)
        if form.is_valid():
            form.save()
            print("Producto Agregado")
        else:
            print("No se pudo agregar el producto")

    return render(request, 'agregar_producto.html', {'form': form, 'submit': 'Agregar Producto'})

#chequear si podemos usar un try/except para devolver el valor de la excepcion

def agregar_proveedor(request):
    form = ProveedorForm()

    if request.method == 'POST':
        form = ProveedorForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print ("No se pudo agregar el proveedor")

    return render(request, 'agregar_proveedor.html', {'form': form, 'submit': 'Agregar Proveedor'})

def productos(request):
    productos = Producto.objects.all();
    return render(request, 'listado_productos.html', {'productos':productos})

def proveedores(request):
    proveedores = Proveedor.objects.all()
    return render(request, 'listado_proveedores.html', {'proveedores': proveedores})