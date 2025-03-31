"""Programa que calcule el importe a pagar por un vehículo al circular por una autopista. El vehículo
puede ser una bicicleta, una moto, un carro o un camión. Para definir el conjunto de vehículos
deben utilizar una estructura adecuada. El importe se calculará según los siguientes datos:
a) Un importe fijo de 100 córdobas para la bicicleta.
b) Las motos y los carros pagarán 30 córdobas por Km.
c) Los camiones pagarán 30 córdobas por Km. más 25 córdobas por toneladas."""

def calcular_importe():
    while True:
        print("\nBienvenido al sistema de importe")
        print("Seleccione el tipo de vehículo:")
        tipoVehiculo = int(input("1. Bicicleta\n2. Moto o carro\n3. Camión\n"))

        if tipoVehiculo == 1:
            print("Su importe es de 100 córdobas")
        elif tipoVehiculo == 2:
            kilometros = int(input("¿Cuántos km ha recorrido?\n"))
            importe = kilometros * 30
            print(f"Su importe es de {importe} córdobas")
        elif tipoVehiculo == 3:
            kilometros = int(input("¿Cuántos km ha recorrido?\n"))
            toneladas = int(input("¿Cuántas toneladas transporta?\n"))
            importe = kilometros * 30 + 25 * toneladas
            print(f"Su importe es de {importe} córdobas")
        else:
            print("Ha seleccionado un número incorrecto. Vuelva a intentarlo.")
            continue
        
        repetir = input("¿Desea calcular otro importe? (s/n): ").strip().lower()
        if repetir != 's':
            print("Gracias por usar el sistema de importe. ¡Hasta luego!")
            break

calcular_importe()
    
