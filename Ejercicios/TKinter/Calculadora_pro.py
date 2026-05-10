import tkinter as tk
from tkinter import messagebox

# --- Funciones Lógicas ---
def sumar(a, b):  
    return a + b

def restar(a, b):  
    return a - b

def multiplicar(a, b):  
    return a * b

def dividir(a, b):  
    if b == 0:  
        return "Error"  
    return a / b

def potencia(base, exponente):  
    return base ** exponente

def raiz_cuadrada(x):  
    if x < 0:  
        return "Error"  
    return x ** 0.5

# --- Interfaz Gráfica ---
class Calculadora(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculadora Python")
        self.geometry("300x400")
        self.configure(bg="#2c3e50")
        
        self.expresion = ""
        self.pantalla_var = tk.StringVar()
        self.crear_interfaz()

    def crear_interfaz(self):
        # Pantalla de visualización
        pantalla = tk.Entry(self, textvariable=self.pantalla_var, font=("Arial", 24), bd=10, insertwidth=4, bg="#34495e", fg="white", justify='right')
        pantalla.pack(fill="both", padx=10, pady=20)

        # Contenedor de botones
        contenedor_botones = tk.Frame(self)
        contenedor_botones.pack()

        botones = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('C', 4, 2), ('+', 4, 3),
            ('^', 5, 0), ('√', 5, 1), ('=', 5, 2, 2)
        ]

        for boton in botones:
            texto = boton[0]
            fila = boton[1]
            columna = boton[2]
            ancho_col = boton[3] if len(boton) > 3 else 1
            
            comando = lambda t=texto: self.al_presionar(t)
            tk.Button(contenedor_botones, text=texto, width=5, height=2, font=("Arial", 14),
                      command=comando).grid(row=fila, column=columna, columnspan=ancho_col, sticky="nsew", padx=2, pady=2)

    def al_presionar(self, tecla):
        if tecla == 'C':
            self.expresion = ""
        elif tecla == '=':
            self.calcular_resultado()
            return
        elif tecla == '√':
            try:
                val = float(self.pantalla_var.get())
                self.expresion = str(raiz_cuadrada(val))
            except:
                self.expresion = "Error"
        else:
            self.expresion += str(tecla)
        
        self.pantalla_var.set(self.expresion)

    def calcular_resultado(self):
        try:
            # Manejo de la potencia para que use nuestra función
            if '^' in self.expresion:
                base, exp = map(float, self.expresion.split('^'))
                resultado = potencia(base, exp)
            else:
                # El resto de operaciones básicas
                # Nota: eval es seguro aquí ya que el input está controlado por botones
                resultado = eval(self.expresion.replace('/', '/'))
                
                # Validación manual para división por cero detectada por eval o lógica
                if resultado == float('inf') or resultado == float('-inf'):
                    resultado = "Error"

            self.expresion = str(resultado)
            self.pantalla_var.set(self.expresion)
        except Exception:
            messagebox.showerror("Error", "Operación inválida")
            self.expresion = ""
            self.pantalla_var.set("")

if __name__ == "__main__":
    app = Calculadora()
    app.mainloop()