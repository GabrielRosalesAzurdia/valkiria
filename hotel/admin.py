from django.contrib import admin
from .models import HabitacionDetalle, Habitaciones, Reserva, Factura
# Register your models here.

admin.site.register(HabitacionDetalle),
admin.site.register(Habitaciones),
admin.site.register(Reserva),
admin.site.register(Factura)