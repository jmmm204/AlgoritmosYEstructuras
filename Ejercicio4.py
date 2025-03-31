"""Programa que lee un número de tres cifras y determina si es igual al revés del número."""

def verificar_numero():
    while True:
        numero = int(input("Ingrese un número de tres cifras: "))
        if 100 <= numero <= 999:
            numero_str = str(numero)
            numero_invertido = numero_str[::-1]
            
            if numero_str == numero_invertido:
                print(f"El número {numero} es igual a su reverso.")
            else:
                print(f"El número {numero} no es igual a su reverso.")
        else:
            print("El número ingresado no tiene tres cifras.")
        
        repetir = input("¿Desea verificar otro número? (s/n): ").strip().lower()
        if repetir != 's':
            print("Programa finalizado.")
            break

verificar_numero()
