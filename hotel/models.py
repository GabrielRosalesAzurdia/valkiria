from django.db import models
from django.contrib.auth import get_user_model

class Habitaciones (models.Model):
    numeroHabitacion = models.IntegerField()

class HabitacionDetalle (models.Model):
    habitacion = models.ForeignKey("hotel.Habitaciones", on_delete=models.CASCADE)
    locacion = models.CharField( max_length=200)
    camasCant = models.IntegerField()
    precioCombo = models.FloatField()

class Reserva (models.Model):
    cliente = models.ForeignKey(get_user_model(),on_delete=models.CASCADE)
    habitacionDetalle = models.ForeignKey("hotel.HabitacionDetalle", on_delete=models.CASCADE)
    nocheIngreso = models.DateField()
    nocheSalida = models.DateField()

class Factura (models.Model):
    reserva = models.ForeignKey("hotel.Reserva", on_delete=models.CASCADE)
