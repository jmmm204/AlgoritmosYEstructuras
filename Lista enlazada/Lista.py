# Clase Nodo - representa un nodo de la lista enlazada
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.siguiente = None

# Clase ListaEnlazada - contiene operaciones para manejar la lista
class ListaEnlazada:
    def __init__(self):
        self.cabeza = None  # Al inicio la lista está vacía

    # Insertar al final de la lista
    def insertarFinal(self, valor):
        nuevo = Nodo(valor)
        if not self.cabeza:  # Si la lista está vacía
            self.cabeza = nuevo
        else:
            actual = self.cabeza
            while actual.siguiente:  # Recorremos hasta el último nodo
                actual = actual.siguiente
            actual.siguiente = nuevo

    # Insertar al inicio de la lista
    def insertarInicio(self, valor):
        nuevo = Nodo(valor)
        nuevo.siguiente = self.cabeza  # El nuevo nodo apunta al anterior primero
        self.cabeza = nuevo  # La cabeza ahora es el nuevo nodo

    # Eliminar un nodo con un valor específico
    def eliminar(self, valor):
        actual = self.cabeza
        anterior = None

        while actual:
            if actual.valor == valor:
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                return True
            anterior = actual
            actual = actual.siguiente
        return False

    # Buscar un valor en la lista
    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.siguiente
        return False

    # Imprimir todos los elementos de la lista
    def imprimir(self):
        actual = self.cabeza
        if not actual:
            print("La lista está vacía")
            return
        print("Lista enlazada:", end=" ")
        while actual:
            print(actual.valor, end=" -> ")
            actual = actual.siguiente
        print("None")

    # Contar cuántos nodos hay en la lista
    def longitudLista(self):
        actual = self.cabeza
        contador = 0
        while actual:
            contador += 1
            actual = actual.siguiente
        return contador

    # Verifica si la lista está vacía
    def estaVacia(self):
        return self.cabeza is None

    # Imprimir el último valor de la lista
    def imprimirUltimo(self):
        if not self.cabeza:
            print("La lista está vacía")
            return
        actual = self.cabeza
        while actual.siguiente:
            actual = actual.siguiente
        print("Último valor de la lista:", actual.valor)


# Punto de entrada del programa
if __name__ == "__main__":
    lista = ListaEnlazada()

    # Leer datos para insertar
    cantidad = int(input("¿Cuántos elementos desea insertar al final de la lista?: "))
    for i in range(cantidad):
        valor = int(input(f"Ingrese el valor #{i + 1}: "))
        lista.insertarFinal(valor)

    lista.imprimir()

    # Insertar valores al inicio
    cantidad_inicio = int(input("\n¿Cuántos elementos desea insertar al inicio de la lista?: "))
    for i in range(cantidad_inicio):
        valor = int(input(f"Ingrese el valor #{i + 1} para insertar al inicio: "))
        lista.insertarInicio(valor)

    lista.imprimir()

    # Buscar un valor
    valor_buscar = int(input("\nIngrese un valor para buscar en la lista: "))
    encontrado = lista.buscar(valor_buscar)
    print("¿Valor encontrado?:", encontrado)

    # Eliminar un valor
    valor_eliminar = int(input("\nIngrese un valor para eliminar de la lista: "))
    eliminado = lista.eliminar(valor_eliminar)
    print("¿Valor eliminado?:", eliminado)
    lista.imprimir()

    # Mostrar si está vacía
    print("\n¿La lista está vacía?:", lista.estaVacia())

    # Mostrar longitud
    print("Longitud de la lista:", lista.longitudLista())

    # Mostrar último valor
    lista.imprimirUltimo()