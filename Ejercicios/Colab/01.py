#bucle for que multiplique todos los numeros multiplos de 7 entre 1 y 49
producto_acumulado = 1
for i in range(1,50):
  if (i % 7 == 0):
    #print(i)
    producto_acumulado = producto_acumulado * i
print(producto_acumulado)


# WHILE LOGIN

usuario = input("Introduce usuario ")
clave = input("Introduce clave ")

#if usuario=="admin" and clave=="123":
#  print("Credenciales correctas, puedes entrar")
#else:
#  print("Credenciales incorrectas, fuera!!!!")

while not(usuario=="admin" and clave=="123"):
  print("Credenciales incorrectas, intenta de nuevo")
  usuario = input("Introduce usuario ")
  clave = input("Introduce clave ")
print("Credenciales correctas, puedes entrar")

#WHILE LOGIN CON LIMITE

usuario = input("Introduce usuario ")
clave = input("Introduce clave ")
max_intentos=5
n_intento=1
while (not(usuario=="admin" and clave=="123")) and (n_intento<max_intentos):
  print("Credenciales incorrectas, intenta de nuevo")
  usuario = input("Introduce usuario ")
  clave = input("Introduce clave ")
  n_intento=n_intento+1
if (usuario=="admin" and clave=="123"):
  print("Credenciales correctas, puedes entrar")
else:
  print("Credenciales incorrectas, superado el límite de intentos")


# hacer un bucle while que funcione como un for y recorra todos los números 
# entre 2 y 98 (ambos incluidos) y solo imprima los múltiplos de 3, de 6 y de 9.

i = 2
while (i<99):
  if (i % 9 == 0):
    print ("múltiplo de 9 ", i)
  elif (i % 6 == 0):
    print ("múltiplo de 6 ", i)
  elif (i % 3 == 0):
    print ("múltiplo de 3 ", i)
  i=i+1
