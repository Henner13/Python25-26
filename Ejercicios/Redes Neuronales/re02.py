import math

def sigmoide(x):
    return 1 if x>= 0 else 0

def sigmoideReal(x):
    return 1/(1+math.exp(-x))

peso_nota = 1.0
peso_asistencia = 0.3
bias = -0.5 #Esto es la tendencia, pero lo va a ir cambiando.

#nota = 6.0
#asistencia = 80

datos = [
    [4.0,60,0],
    [4.5,80,0],
    [4.76,80,0],
    [5.0,80,1],
    [5.1,80,1],
    [6.5,80,1]
]
cont = 1
learning_rate = 0.1
epocas = 10000
for _ in range(epocas):
    for nota,asistencia,esperado in datos:
        print(f"INTERACCION: {cont}")
        nota_n = nota / 10
        asistencia_n = asistencia / 100
        z= nota_n * peso_nota + asistencia_n * peso_asistencia + bias
        salida = sigmoideReal(z)
        #print(f"z: {z} ")
        #print(f"salida: {salida} ")
        #if (salida >=0.5):
        #    print("APROBADO")
        #else:
        #    print("SUSPENSO")
        error = esperado - salida
        print(f"error: {error}")
        peso_nota += peso_nota + error * nota_n * learning_rate
        peso_asistencia += peso_asistencia +error * asistencia_n * learning_rate
        bias = bias + error * learning_rate
        cont += 1
print(f"peso_nota: {peso_nota}")
print(f"peso_asistencia: {peso_asistencia}")
print(f"bias: {bias}")

nota = 5.0
aistencia = 80
nota_n = nota /10
asistencia_n = asistencia /100
z= nota_n * peso_nota + asistencia_n * peso_asistencia + bias
salida = sigmoideReal(z)
print(f"nota: {nota}")
print(f"aistencia: {asistencia}")
if (salida >=0.5):
    print("APROBADO")
else:
    print("SUSPENSO")
