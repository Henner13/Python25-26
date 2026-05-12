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
    [4.9,80,0],
    [5.0,80,1],
    [5.1,80,1],
    [6.5,80,1]
]

# parada temprana iteligente
mejor_error = float('inf')
paciencia = 20 #número de veces que no cambie el error para parar
contador = 0
min_delta = 0.001 #mínimo cambio en el error para considerarlo una mejora


learning_rate = 0.1
epocas = 10000
cont_n_interaciones = 0
parar = False #para poder salir del bucle externo

for _ in range(epocas):
    if parar:
        break
    error_total = 0

    for nota,asistencia,esperado in datos:
        nota_n = nota / 10
        asistencia_n = asistencia / 100
        z= nota_n * peso_nota + asistencia_n * peso_asistencia + bias
        salida = sigmoideReal(z)
        error = esperado - salida
        print(f"error: {error}")

        error_total = error_total + abs(error)
        if (mejor_error - error_total) > min_delta:
            mejor_error = error_total
            contador = 0
        else:
            contador += 1
        
        if contador >= paciencia:
            print(f"Parada temprana en {cont_n_interaciones} interaciones.")
            parar = True
            break

        peso_nota += peso_nota + error * nota_n * learning_rate
        peso_asistencia += peso_asistencia +error * asistencia_n * learning_rate
        bias = bias + error * learning_rate
        cont_n_interaciones +=1


print(f"peso_nota: {peso_nota}")
print(f"peso_asistencia: {peso_asistencia}")
print(f"bias: {bias}")

nota = 4.96
asistencia = 80
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
