while True:
    print("====================================================")
    print("CALCULO DE SUPERFICIES (Version 1.0)")
    print("====================================================")
    eleccion = int(input("1. Cuadrado  |  lado * lado\n2. Circulo  |  pi * radio * radio\n3. Rectangulo  |  base * altura\n4. Trapecio  | (base1 + base2) * altura / 2\n5. Triangulo  |  (base * altura) / 2\n====================================================\n"))

    if eleccion == 1:
        lado_cuadrado = int(input("Ingrese el lado del cuadrado: \n"))
        operacion_cuadrado = lado_cuadrado * lado_cuadrado
        print(f"El area del cuadrado es de {operacion_cuadrado}")
    elif eleccion == 2:
        radio = int(input("Ingrese el radio del circulo: \n"))
        operacion_circulo = 3.14 * (radio * radio)
        print(f"El area del circulo es de {operacion_circulo}")
    elif eleccion == 3:
        base = int(input("Ingrese la base del rectangulo: \n"))
        altura_rectangulo = int(input("Ingrese la altura del rectangulo: \n"))
        operacion_rectangulo = base * altura_rectangulo
        print(f"El area del rectangulo es de {operacion_rectangulo}")
    elif eleccion == 4:
        base1 = int(input("Ingrese la primera base del trapecio: \n"))
        base2 = int(input("Ingrese la segunda base del trapecio: \n"))
        altura_trapecio = int(input("Ingrese la altura del trapecio: \n"))
        operacion_trapecio = (base1 + base2) * altura_trapecio / 2
        print(f"El area del trapecio es de {operacion_trapecio}")
    elif eleccion == 5:
        base_triangulo = int(input("Ingrese la base del triangulo: \n"))
        altura_triangulo = int(input("Ingrese la altura del triangulo: \n"))
        operacion_triangulo = (base_triangulo * altura_triangulo) / 2
        print(f"El area del triangulo es de {operacion_triangulo}")
    else:
        print("Ha seleccionado un numero incorrecto. Por favor, intentelo nuevamente")
        
    continuar = input("¿Desea hacer otro cálculo? (si/no):\n").strip().lower()
    if continuar != 'si':
        print("Fin del programa")
        break

