from django.db import models

# Create your models here.
class Proveedor(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    dni = models.IntegerField()

    def __str__(self):
        return '{}'.format(self.nombre)

class Producto(models.Model):
    nombre = models.CharField(max_length=50)
    precio = models.FloatField(max_length=6)
    stock_actual = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.SET_NULL, null=True)