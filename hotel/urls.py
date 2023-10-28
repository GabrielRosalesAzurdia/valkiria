from django.urls import path , include
from rest_framework import routers
from .views import HabitacionDetalleViewset, HabitacionesViewset, ReservaViewset, FacturaViewset, UsuarioViewest

router = routers.DefaultRouter()
router.register(r'habitaciondetalle', HabitacionDetalleViewset)
router.register(r'habitaciones', HabitacionesViewset)
router.register(r'reservas', ReservaViewset)
router.register(r'facturas', FacturaViewset)
router.register(r'usuario',UsuarioViewest)

urlpatterns = [
    path('', include(router.urls)) ,
]