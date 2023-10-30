# API VALKIRIA

## Models

### Habitaciones

    numeroHabitacion = int

### HabitacionDetalle

    habitacion = Habitacion
    locacion = string
    camasCant = int
    precioCombo = float

### Reserva

    cliente = User
    habitacionDetalle = HabitacionDetalle
    nocheIngreso = date
    nocheSalida = date

### Factura

    reserva = Reserva

## Endpoints

A todos estos endpoints se les peude aplicar

GET
POST

Si se quiere eliminar algo en especificio se debe
colocar al final de la url

> http://127.0.0.1:8000/habitaciondetalle/

> http://127.0.0.1:8000/habitaciones/

> http://127.0.0.1:8000/reservas/

> http://127.0.0.1:8000/facturas/

Ejemplo especifico

> http://127.0.0.1:8000/facturas/1

A estas se les puede hacer

DELETE
UPDATE