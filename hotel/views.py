from rest_framework import viewsets
from .models import HabitacionDetalle, Habitaciones, Reserva, Factura
from .serializers import HabitacionDetalleSerializer, HabitacionesSerializer, ReservaSerializer, FacturaSerializer

class HabitacionDetalleViewset (viewsets.ModelViewSet):
    queryset = HabitacionDetalle.objects.all()
    serializer_class = HabitacionDetalleSerializer

class HabitacionesViewset (viewsets.ModelViewSet):
    queryset = Habitaciones.objects.all()
    serializer_class = HabitacionesSerializer

class ReservaViewset (viewsets.ModelViewSet):
    queryset = Reserva.objects.all()
    serializer_class = ReservaSerializer

class FacturaViewset(viewsets.ModelViewSet):
    queryset = Factura.objects.all()
    serializer_class = FacturaSerializer