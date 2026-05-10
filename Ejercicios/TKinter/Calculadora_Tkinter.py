
import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

# Configurar la ventana
ventana.title("Calculadora Simple")
ventana.geometry("400x200")

# Crear y colocar etiqueta de título
etiqueta = tk.Label(ventana, text="Calculadora:")
etiqueta.pack(pady=(15, 10))

# Crear un frame para alinear las dos entradas en la misma fila
frame_entradas = tk.Frame(ventana)
frame_entradas.pack(pady=10)

# Entradas de texto, una al lado de la otra
entrada1 = tk.Entry(frame_entradas, width=10)
entrada1.pack(side=tk.LEFT, padx=10)

entrada2 = tk.Entry(frame_entradas, width=10)
entrada2.pack(side=tk.LEFT, padx=10)

# Definir la función para sumar
def Sumar():
        valor1 = int(entrada1.get())
        valor2 = int(entrada2.get())
        resultado = valor1 + valor2
        etiqueta_resultado.config(text=f"El resultado es: {resultado}")

def Restar():
        valor1 = int(entrada1.get())
        valor2 = int(entrada2.get())
        resultado = valor1 - valor2
        etiqueta_resultado.config(text=f"El resultado es: {resultado}")

def Multiplicar():
        valor1 = int(entrada1.get())
        valor2 = int(entrada2.get())
        resultado = valor1 * valor2
        etiqueta_resultado.config(text=f"El resultado es: {resultado}")
def Dividir():
        valor1 = int(entrada1.get())
        valor2 = int(entrada2.get())
        if valor2 != 0:
            resultado = valor1 / valor2
            etiqueta_resultado.config(text=f"El resultado es: {resultado}")
        else:
            etiqueta_resultado.config(text="Error: No se puede dividir por cero.")


# Crear y colocar el botón (debajo de las entradas)
boton_sumar = tk.Button(ventana, text="+", command=Sumar, width=4, height=1, bg="lightyellow")
boton_sumar.pack(pady=20, padx=10, side=tk.LEFT)

boton_restar = tk.Button(ventana, text="-", command=Restar, width=4, height=1, bg="lightcoral")
boton_restar.pack(pady=20, padx=10, side=tk.LEFT)

boton_multiplicar = tk.Button(ventana, text="*", command=Multiplicar, width=4, height=1, bg="lightgreen")
boton_multiplicar.pack(pady=20, padx=10, side=tk.RIGHT)
#Boton dividir, color azul, con un espacio entre el boton multiplicar y el boton dividir.
boton_dividir = tk.Button(ventana, text="/", command=Dividir, width=4, height=1, bg="lightblue")
boton_dividir.pack(pady=20, padx=10, side=tk.RIGHT,)

# Crear y colocar una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=(10, 5))

# Iniciar el bucle principal de la ventana
ventana.mainloop()
