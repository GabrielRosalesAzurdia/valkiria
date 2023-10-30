from django.contrib import admin
from .models import HabitacionDetalle, Habitaciones, Reserva, Factura, Usuario
# Register your models here.

admin.site.register(Usuario),
admin.site.register(HabitacionDetalle),
admin.site.register(Habitaciones),
admin.site.register(Reserva),
admin.site.register(Factura)