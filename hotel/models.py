from django.db import models
from django.utils import timezone
from django.contrib.auth import get_user_model

class Usuario (models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    nit = models.CharField(max_length=100)
    fechaNacimiento = models.DateTimeField(null=True, blank=True)
    correo = models.CharField(max_length=60)
    usuario = models.CharField(max_length=50)
    contraseña = models.CharField(max_length=60)
    
    
class Habitaciones (models.Model):
    numeroHabitacion = models.IntegerField()

class HabitacionDetalle (models.Model):
    habitacion = models.ForeignKey("hotel.Habitaciones", on_delete=models.CASCADE, default=1)
    locacion = models.CharField( max_length=200)
    camasCant = models.IntegerField()
    precioCombo = models.FloatField()

class Reserva (models.Model):
    usuario = models.ForeignKey("hotel.Usuario",on_delete=models.CASCADE)
    habitacionDetalle = models.ForeignKey("hotel.HabitacionDetalle", on_delete=models.CASCADE)
    nocheIngreso = models.DateField()
    nocheSalida = models.DateField()

class Factura (models.Model):
    reserva = models.ForeignKey("hotel.Reserva", on_delete=models.CASCADE)


    