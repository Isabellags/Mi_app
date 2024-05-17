from django.db import models
from django.contrib.auth.models import User

class OrdenCompra(models.Model):
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=20)
    comuna = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'Orden de compra #{self.pk}'

class Libro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=100)
    precio = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.titulo

class DetalleOrdenCompra(models.Model):
    orden_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    libro = models.ForeignKey(Libro, on_delete=models.CASCADE)
    cantidad = models.IntegerField()

    def __str__(self):
        return f'{self.libro} ({self.cantidad})'

