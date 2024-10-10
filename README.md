# VEHICULOS
# Sistema de Gestión de Vehículos

Este proyecto es un sistema simple para gestionar diferentes tipos de vehículos en un concesionario. Se implementan clases para representar vehículos como autos y motos.

## Estructura del Proyecto

- **Clase `Vehiculo`**: Clase base que contiene propiedades comunes a todos los vehículos:
  - `Marca` (string)
  - `Modelo` (string)
  - `Año` (int)

- **Clase `Auto`**: Hereda de `Vehiculo` y tiene propiedades específicas:
  - `NumeroPuertas` (int)
  - `EsAutomatico` (bool)

- **Clase `Moto`**: Hereda de `Vehiculo` y tiene propiedades específicas:
  - `Cilindraje` (int)
  - `Tipo` (string)

## Funcionalidades

El programa crea cuatro objetos de diferentes tipos (autos y motos) y muestra su información específica en la consola.

## Instrucciones para Ejecutar

1. Clona el repositorio en tu máquina local.
2. Asegúrate de tener Python instalado.
3. Ejecuta el programa con el siguiente comando:

   ```bash
   python nombre_del_archivo.py