"""Programa que permite emitir la FACTURA correspondiente, a una compra de un artículo determinado, del que
se adquieren una o varias unidades. El IVA a aplicar es de 15% y si el Sub Total (precio de venta por
cantidad), es mayor de 1000, se aplicará un descuento del 12%."""

def calcular_factura():
    while True:
        print("\n--- FACTURACIÓN DE COMPRA ---")
        
        try:
            precio_articulo = float(input("Ingrese el precio del artículo: "))
            unidades = int(input("Ingrese la cantidad de unidades compradas: "))
            
            if precio_articulo < 0 or unidades < 0:
                print("El precio y la cantidad deben ser valores positivos.")
                continue
            
            sub_total = precio_articulo * unidades
            IVA = sub_total * 0.15
            precio_total = sub_total + IVA
            
            if sub_total > 1000:
                print("Se aplicará un 12% de descuento por superar los 1000 córdobas.")
                descuento = precio_total * 0.12
                precio_total -= descuento
            
            print(f"\nSubtotal: {sub_total:.2f} córdobas")
            print(f"IVA (15%): {IVA:.2f} córdobas")
            print(f"Total a pagar: {precio_total:.2f} córdobas")

        except ValueError:
            print("Por favor, ingrese valores numéricos válidos.")
            continue

        repetir = input("\n¿Desea calcular otra factura? (S/N): ").strip().lower()
        if repetir != 's':
            print("Gracias por utilizar el sistema de facturación.")
            break

calcular_factura()
