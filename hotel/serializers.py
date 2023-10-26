from .models import HabitacionDetalle, Habitaciones, Reserva, Factura
from rest_framework import serializers

class HabitacionDetalleSerializer(serializers.ModelSerializer):
    class Meta:
        model = HabitacionDetalle
        fields = "__all__"

class HabitacionesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Habitaciones
        fields = "__all__"

class ReservaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reserva
        fields = "__all__"

class FacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Factura
        fields = "__all__"