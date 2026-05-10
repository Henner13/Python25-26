"""
Crea una aplicación en consola donde se permitan gestionar las calificaciones de la asignatura.
Para ello, mediante un menú permite las siguientes acciones:
1. Introducir notas: el usuario introducirá notas hasta que meta un -1. Esto indicará que la introducción ha terminado. Una vez realizado esto volverá a aparecer el menú.
2. Listar notas: se mostrarán todas las notas de una en una.
3. Obtener extremos: se mostrarán la nota más alta y baja.
4. Obtener información: se mostrarán los siguientes datos sobre las notas: total introducidas, número suspensos, número aprobados, nota media.
5. Salir
"""

opcion = 0
listaNotas = []
while opcion != 5:
  print ("MENU")
  print ("1 Introducir notas:")
  print ("2 Listar notas:")
  print ("3 Obtener extremos:")
  print ("4 Obtener información:")
  print ("5 Salir:")
  opcion = int(input("Elige una opción"))
  match opcion:
    case 1:
      print("1 Introducir notas:")
      nota = float(input("mete nota:"))
      listaNotas.append(nota)
    case 2:
      print ("2 Listar notas:")
      print(listaNotas)
    case 3:
      print ("3 Obtener extremos:")
      print ("La nota más alta es ",max(listaNotas))
      print ("La nota más baja es ",min(listaNotas))
    case 4:
      print ("4 Obtener información:")
      print ("El número total de notas es",len(listaNotas))
      numeroSuspensos = 0
      suma=0
      for notai in listaNotas:
        suma = suma + notai
        if (notai<5):
          numeroSuspensos+=1
      print ("El número de suspensos es",numeroSuspensos)
      print ("El número de aprobados es",len(listaNotas) - numeroSuspensos)
      print ("La media es",suma / len(listaNotas) )
    case 5:
      print ("5 Salir:")
    case _:
      print("Opción no válida. Inténtalo de nuevo.")
print ("fin del programa")
