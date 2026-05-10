# Crea un programa en Python que permita gestionar una lista de productos de una tienda.
# El programa debe utilizar funciones para realizar las siguientes operaciones:
# Agregar productos con su nombre y precio. 
# Mostrar todos los productos disponibles. 
# Buscar un producto por su nombre y mostrar su precio. 
# Calcular el precio total de todos los productos.
# Organiza tu código en funciones separadas para cada una de estas acciones.
# El usuario debe poder elegir qué hacer mediante un menú simple.
# Además, tendrás que utilizar estructuras de control como listas para poder almacenar todos los productos.

productos = []

def agregar_producto():
    nombre = input("Introduce el nombre del producto: ").strip()
    try:
        precio = float(input(f"Introduce el precio de {nombre}(ej. 2.00) : "))
        productos.append((nombre, precio))
        print(f"Producto agregado: {nombre} - {precio:.2f}€")
    except ValueError:
        print("Error: El precio debe ser un número válido.")

def mostrar_productos():
    if not productos:
        print("No hay productos disponibles.")
    else:
        print("Productos disponibles:")
        for nombre, precio in productos:
            print(f"{nombre} - {precio:.2f}€")

def buscar_producto(**kwargs):
    nombre = input("Introduce el nombre del producto a buscar: ").strip()
    encontrado = False
    for prod_nombre, prod_precio in productos:
        if prod_nombre.lower() == nombre.lower():
            print(f"Producto encontrado: {prod_nombre} - {prod_precio:.2f}€")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.")

def calcular_precio_total():
    if not productos:
        print("No hay productos para calcular el precio total.")
    else:
        total = sum(precio for _, precio in productos)
        print(f"Precio total de todos los productos: {total:.2f}€")

while True:
    print("\n----- Menú de opciones -----")
    print("1. Agregar producto")
    print("2. Mostrar todos los productos")
    print("3. Buscar producto por nombre")
    print("4.Calcular el precio total de todos los productos")
    print("5. Salir")

    opcion = input("Selecciona una opción (1-5): ")
    if opcion == "1":
        print("\n----- Agregar un producto -----")
        agregar_producto()
    elif opcion == "2":
        print("\n----- Mostrar todos los productos -----")
        mostrar_productos()
    elif opcion == "3":
        print("\n----- Buscar un producto por su nombre -----")
        buscar_producto()
    elif opcion == "4":
        print("\n----- Calcular el precio total de todos los productos -----")
        calcular_precio_total()
    elif opcion == "5":
        print("Saliendo del programa.¡Hasta la próxima!")
        break
    else:
        print("No me sirve, tienes que elegir una opción del 1 al 5.")
