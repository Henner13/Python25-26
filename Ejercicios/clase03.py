"""
Crea una aplicación en python que permita gestionar los proyectos de una empresa.
Para ello sigue estos pasos:
• Pregunta al usuario cuantos proyectos va a registrar
• Por cada proyecto, pide el código, nombre, responsable y presupuesto del proyecto
• Guarda la información de todos los proyectos en un diccionario 
(puedes utilizar el código como la clave y como valor puedes utilizar otro diccionario o lista 
• Muestra por consola solo el nombre y presupuesto de cada uno de los proyectos 
"""
def main():
    proyectos = {}
    try:
        num_proyectos = int(input("¿Cuántos proyectos va a registrar?"))
    except ValueError:
        print("Por favor, ingrese un número válido.")
        return

    for i in range(num_proyectos):
        print(f"\n--- Registro del proyecto {i + 1} ---")
        codigo = input("Ingrese el código del proyecto:")
        nombre = input("Ingrese el nombre del proyecto: ")
        responsable = input("Ingrese el responsable del proyecto: ")

        while True:
            try:
                presupuesto = float(input("Ingrese el presupuesto del proyecto: "))
            except ValueError:
                print("Por favor, ingrese un número válido para el presupuesto.")
            else:
                break
        proyectos[codigo] = {
            "nombre": nombre,
            "responsable": responsable,
            "presupuesto": presupuesto
        }
    #Muestra el numero de proyecto registrados.
    print("\n--- Número total de proyectos registrados ---")
    print(f"Total de proyectos: {len(proyectos)}")

    #Muestra el nombre y presupuesto de cada proyecto registrado.
    print("\n" + "="*30)
    print("Proyectos registrados")
    print("="*30)
    for codigo, info in proyectos.items():
        print(f"Código: {codigo}\nNombre: {info['nombre']}\nPresupuesto: {info['presupuesto']:.2f}€\n")

if __name__ == "__main__":
    main()  
