from django.db import models

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

# add user model (employee)
# class Factura (models.Model):
#     reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE)
#     empleado = models.ForeignKey(, on_delete=models.CASCADE)
