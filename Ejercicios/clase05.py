""" Imagina que estás desarrollando un pequeño sistema en Python para una cafetería.
    El sistema debe permitir registrar distintos tipos de productos que se pueden pedir (por ejemplo, cafés, tés y bollería),
    llevar un control de los pedidos y calcular el precio total. 
    Para ello deberás crear una clase Producto con los siguientes datos:
    Nombre, precio y método mostrar_info 
    Además de esta clase deberás crear tres clases derivadas llamadas Bebida: 
    con un atributo adicional llamado tipo (string),
    sobreescribiendo el método mostrar_info Comida: con un atributo adicional llamado caliente (boolean),
    sobreescribiendo el método mostrar_info Menú: con un atributo adicional llamado completo (boolean),
    sobreescribiendo el método mostrar_info
    Por último, crea una clase llamada Pedido, el cual pueda contener tantos productos como el cliente considere necesario,
    además de un atributo coste total donde se calcule el coste del pedido 
    Puedes generar un par de pedidos con productos dentro o realizar un menú para la gestión de los pedidos.
"""
class producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio

    def mostrar_info(self):
        return f"Producto: {self.nombre}, Precio: {self.precio:.2f}€"

# Herencia de la clase producto para crear las clases bebida, comida y menu
class bebida(producto):
    def __init__(self, nombre, precio, tipo):
        super().__init__(nombre, precio)
        self.tipo = tipo

    def mostrar_info(self):
        return f"Bebida: {self.nombre}, Tipo: {self.tipo}, Precio: {self.precio:.2f}€"

class comida(producto):
    def __init__(self, nombre, precio, caliente):
        super().__init__(nombre, precio)
        self.caliente = caliente

    def mostrar_info(self):
        estado = "Caliente" if self.caliente else "Fría"
        return f"Comida: {self.nombre}, Estado: {estado}, Precio: {self.precio:.2f}€"

class menu(producto):
    def __init__(self, nombre, precio, completo):
        super().__init__(nombre, precio)
        self.completo = completo

    def mostrar_info(self):
        estado = "Completo" if self.completo else "No Completo"
        return f"Menú: {self.nombre}, Estado: {estado}, Precio: {self.precio:.2f}€"
    


# Clase pedido para gestionar los pedidos de los clientes
class pedido:
    def __init__(self):
        self.productos = []
        self.coste_total = 0.0

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.coste_total += producto.precio

    def mostrar_pedido(self):
        info = "Pedido:\n"
        for producto in self.productos:
            info += producto.mostrar_info() + "\n"
        info += f"Coste Total: {self.coste_total:.2f}€"
        return info  
    
# Función para gestionar los pedidos a través de un menú interactivo    
def gestion_pedidos():
    pedido_actual = pedido()
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar bebida")
        print("2. Agregar comida")
        print("3. Agregar menú")
        print("4. Mostrar pedido actual")
        print("5. Salir")

        opcion = int(input("Elige una opción (1-5): "))
        match opcion:
            case 1:
                nombre = input("Nombre de la bebida: ")
                precio = float(input("Precio de la bebida: "))
                tipo = input("Tipo de bebida: ")
                pedido_actual.agregar_producto(bebida(nombre, precio, tipo))
            case 2:
                nombre = input("Nombre de la comida: ")
                precio = float(input("Precio de la comida: "))
                caliente = input("¿La comida es caliente? (s/n): ").lower() == 's'
                pedido_actual.agregar_producto(comida(nombre, precio, caliente))
            case 3:
                nombre = input("Nombre del menú: ")
                precio = float(input("Precio del menú: "))
                completo = input("¿El menú es completo? (s/n): ").lower() == 's'
                pedido_actual.agregar_producto(menu(nombre, precio, completo))
            case 4:
                print(pedido_actual.mostrar_pedido())
            case 5:
                print("Gracias por su pedido. ¡Hasta luego!")
                break

if __name__ == "__main__":
    gestion_pedidos()



""" Ejemplo de uso
pedido1 = pedido()
pedido1.agregar_producto(bebida("Café", 2.50, "Espresso"))
pedido1.agregar_producto(comida("Croissant", 1.20, True))
print(pedido1.mostrar_pedido())

pedido2 = pedido()
pedido2.agregar_producto(menu("Desayuno Completo", 5.00, True))
print(pedido2.mostrar_pedido()) 
"""

