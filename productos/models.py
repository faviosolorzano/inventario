from django.db import models

class Proveedor(models.Model):
    nombre_empresa = models.CharField(max_length=200)
    ciudad = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre_empresa

class Producto(models.Model):
    nombre = models.CharField(max_length=200)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.IntegerField()
    proveedor = models.ForeignKey(Proveedor, on_delete=models.CASCADE, related_name='productos')

    def __str__(self):
        return self.nombre