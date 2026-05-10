import tkinter as tk

# Crear la ventana principal
ventana = tk.Tk()

esCara = tk.BooleanVar()
mi_check = tk.Checkbutton(ventana,text="nivel 1", variable=esCara, value=True)


# Definir la función para sumar
def Sumar():
        valor1 = int(entrada1.get())
        valor2 = int(entrada2.get())
        resultado = valor1 + valor2
        etiqueta_resultado.config(text=f"El resultado es: {resultado}")

# Crear y colocar el botón (debajo de las entradas)
boton = tk.Button(ventana, text="+", command=Sumar, width=4, height=1)
boton.pack(pady=20)

# Crear y colocar una etiqueta para mostrar el resultado
etiqueta_resultado = tk.Label(ventana, text="")
etiqueta_resultado.pack(pady=(10, 5))

# Iniciar el bucle principal de la ventana
ventana.mainloop()