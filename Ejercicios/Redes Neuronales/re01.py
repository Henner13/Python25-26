import math

def sigmoide(x):
    return 1 if x>= 0 else 0

def sigmoideReal(x):
    return 1/(1+math.exp(-x))

peso_nota = 1.0
peso_asistencia = 0.3
bias = -0.5

nota = 6.0
asistencia = 80

#5.4 70 APROBADo
#4.6 60 SUSPENSO
#7.8 80 APROBADO
#10 100 APROBADO
#3 30 SUSPENSO

#9.1 SOBRE
#8.5 NO SOBRE
#7.5 NO SOBRE
#9.5 SOBRE
#10 SOBRE
#9.7 SOBRE
#8.9 NO SOBRE

nota_n = nota / 10
asistencia_n = asistencia / 100

z= nota_n * peso_nota + asistencia_n * peso_asistencia + bias

salida = sigmoideReal(z)

print(f"z:{z}")
print(f"salida:{salida}")
if (salida >=0.5):
    print("Aprobado")
else:
    print("Suspenso")
