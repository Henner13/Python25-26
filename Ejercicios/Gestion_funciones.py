alumnos = {}

def agregar_alumno():
    dni = input("Introduce el DNI del alumno: ").strip()
    if dni in alumnos:
        print("El alumno con ese DNI ya existe.")
    else:
        nombre = input("Introduce el nombre del alumno: ").strip()
        try:
            edad = int(input("Introduce la edad del alumno: "))
            nota = float(input("Introduce la nota final del alumno (0-10): "))
            if 0 <= nota <= 10:
                alumnos[dni] = {
                    "nombre": nombre,
                    "edad": edad,
                    "nota": nota
                }
                print("Alumno agregado correctamente.")
            else:
                print("La nota debe estar entre 0 y 10.")
        except ValueError:
            print("Por favor, introduce valores numéricos válidos para la edad y la nota.")

def mostrar_alumnos():
    if not alumnos:
        print("No hay alumnos registrados.")
    else:
        for dni, datos in alumnos.items():
            print(f"DNI: {dni} | Nombre: {datos['nombre']} | Edad: {datos['edad']} | Nota: {datos['nota']}")

def buscar_alumno():
    dni = input("Introduce el DNI a buscar: ").strip()
    if dni in alumnos:
        datos = alumnos[dni]
        print(f"Datos del alumno:\nNombre: {datos['nombre']}, Edad: {datos['edad']}, Nota: {datos['nota']}")
    else:
        print("Alumno no encontrado.")

def mostrar_aprobados():
    aprobados = False
    for dni, datos in alumnos.items():
        if datos['nota'] >= 5:
            print(f"APROBADO -> DNI: {dni} | Nombre: {datos['nombre']} | Nota: {datos['nota']}")
            aprobados = True
    if not aprobados:
        print("Nadie ha aprobado. Masacre a la vista.")

def calcular_media():
    if not alumnos:
        print("No hay alumnos. No se puede calcular la media.")
    else:
        suma = sum(datos['nota'] for datos in alumnos.values())
        media = suma / len(alumnos)
        print(f"La nota media es: {media:.2f}")

def mostrar_mejor_alumno():
    if not alumnos:
        print("No se puede sacar de donde no hay.")
    else:
        mejor_dni = max(alumnos, key=lambda dni: alumnos[dni]['nota'])
        mejor = alumnos[mejor_dni] 
        print(f"El mejor alumno es: {mejor['nombre']} (DNI: {mejor_dni}) con una nota de {mejor['nota']}")
#Otra opción sería:
#       mejor = max(alumnos.values(),key=lambda n: n['nota'])
#       print(f"El mejor es: {mejor['nombre']} con un {mejor['nota']}")

def mostrar_peor_alumno():
    if not alumnos:
        print("No hay peor, todos son igual de pateticos.")
    else:
        peor_dni = min(alumnos, key=lambda dni: alumnos[dni]['nota'] )
        peor = alumnos[peor_dni]
        print(f"El peor alumno es: {peor['nombre']} (DNI: {peor_dni}) con una nota de {peor['nota']}")

def main():
    while True:
        print("\nMenú de opciones:")
        print("1. Agregar alumno")
        print("2. Mostrar todos los alumnos")
        print("3. Buscar alumno por DNI")
        print("4. Mostrar alumnos aprobados")
        print("5. Calcular la media de las notas")
        print("6. Mostrar el mejor alumno y al peor")
        print("7. Salir")

        opcion = int(input("Elige una opción (1-7): "))
        match opcion:
            case 1:
                agregar_alumno()
            case 2:
                mostrar_alumnos()
            case 3:
                buscar_alumno()
            case 4:
                mostrar_aprobados()
            case 5:
                calcular_media()
            case 6:
                mostrar_mejor_alumno()
                mostrar_peor_alumno()
            case 7:
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida, por favor selecciona una opción del 1 al 7.")

if __name__ == "__main__":
    main()
