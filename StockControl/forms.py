from django.forms import ModelForm
from .models import Proveedor,Producto

#Formulario de Proveedor
class ProveedorForm(ModelForm):
    class Meta:
        model = Proveedor
        fields = ['nombre', 'apellido','dni']


#Formulario de Producto
class ProductoForm(ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'precio', 'stock_actual', 'proveedor']
