"""Un supermercado ha puesto en oferta la venta al por mayor de cierto producto, ofreciendo un descuento
del 15% por la compra de más de 3 docenas y 10% en caso contrario. Además, por la compra de más de 3
docenas se obsequia una unidad del producto por cada docena en exceso sobre 3. Diseñe un programa que
determine el monto de la compra, el monto del descuento, el monto a pagar y el número de unidades de
obsequio por la compra de cierta cantidad de docenas del producto."""

def calcular_compra():
    while True:
        print("\n--- CÁLCULO DE COMPRA EN SUPERMERCADO ---")
        
        try:
            cantidad_docenas = int(input("Ingrese la cantidad de docenas que desea comprar: "))
            precio_por_docena = float(input("Ingrese el precio por docena: "))

            if cantidad_docenas <= 0 or precio_por_docena <= 0:
                print("La cantidad de docenas y el precio deben ser valores positivos.")
                continue

            if cantidad_docenas > 3:
                descuento = 0.15
                unidades_obsequio = cantidad_docenas - 3
            else:
                descuento = 0.10
                unidades_obsequio = 0

            monto_compra = cantidad_docenas * precio_por_docena
            monto_descuento = monto_compra * descuento
            monto_pagar = monto_compra - monto_descuento

            print(f"\nMonto de la compra (sin descuento): {monto_compra:.2f} córdobas")
            print(f"Monto del descuento: {monto_descuento:.2f} córdobas")
            print(f"Monto a pagar: {monto_pagar:.2f} córdobas")
            print(f"Unidades de obsequio: {unidades_obsequio}")

        except ValueError:
            print("Error: Ingrese valores numéricos válidos.")
            continue

        repetir = input("\n¿Desea realizar otra compra? (S/N): ").strip().lower()
        if repetir != 's':
            print("Gracias por su compra. ¡Vuelva pronto!")
            break

calcular_compra()
