# Clase base Vehiculo
class Vehiculo:
    def __init__(self, marca, modelo, año):
        self.marca = marca
        self.modelo = modelo
        self.año = año

# Clase derivada Auto
class Auto(Vehiculo):
    def __init__(self, marca, modelo, año, numero_puertas, es_automatico):
        super().__init__(marca, modelo, año)
        self.numero_puertas = numero_puertas
        self.es_automatico = es_automatico

    def mostrar_info(self):
        print(f"Auto: {self.marca} {self.modelo}, Año: {self.año}, "
              f"Puertas: {self.numero_puertas}, Automático: {self.es_automatico}")

# Clase derivada Moto
class Moto(Vehiculo):
    def __init__(self, marca, modelo, año, cilindraje, tipo):
        super().__init__(marca, modelo, año)
        self.cilindraje = cilindraje
        self.tipo = tipo

    def mostrar_info(self):
        print(f"Moto: {self.marca} {self.modelo}, Año: {self.año}, "
              f"Cilindraje: {self.cilindraje}, Tipo: {self.tipo}")

# Función principal
def main():
    # Crear lista de vehículos
    vehiculos = [
        Auto("Toyota", "Corolla", 2020, 4, True),
        Auto("Ford", "Fiesta", 2019, 4, False),
        Moto("Yamaha", "YZF-R3", 2021, 321, "Deportiva"),
        Moto("Honda", "PCX", 2022, 150, "Scooter")
    ]

    # Mostrar información de los vehículos
    for vehiculo in vehiculos:
        vehiculo.mostrar_info()

# Ejecutar la función principal
if __name__ == "__main__":
    main()