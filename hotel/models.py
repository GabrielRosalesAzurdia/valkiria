from django.db import models
from django.contrib.auth import get_user_model

class Clientes (models.Model):
    edad = models.IntegerField
    nacionalidad = models.CharField(200)
    nit = models.IntegerField

class Habitaciones (models.Model):
    numeroHabitacion = models.IntegerField
    locacion = models.CharField(200)
    camasCant = models.IntegerField
    precioCombo = models.FloatField

class Reserva (models.Model):
    cliente = models.ForeignKey(Clientes,on_delete=models.CASCADE)
    habitacion = models.ForeignKey(Habitaciones,on_delete=models.CASCADE)
    nocheIngreso = models.DateField
    nocheSalida = models.DateField

class Factura (models.Model):
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
    empleado = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
