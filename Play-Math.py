import tkinter as tk
import random

def generar_numeros():
    global num1, num2, respuesta_correcta
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    respuesta_correcta = num1 * num2
    opciones = [respuesta_correcta, respuesta_correcta + random.randint(1, 3), respuesta_correcta - random.randint(1, 3)]
    random.shuffle(opciones)
    label_numeros.config(text=f"{num1} x {num2}")
    boton_opcion1.config(text=opciones[0], command=lambda: verificar_respuesta(opciones[0]))
    boton_opcion2.config(text=opciones[1], command=lambda: verificar_respuesta(opciones[1]))
    boton_opcion3.config(text=opciones[2], command=lambda: verificar_respuesta(opciones[2]))

def verificar_respuesta(respuesta):
    if respuesta == respuesta_correcta:
        label_resultado.config(text="Correcto", fg="green")
    else:
        label_resultado.config(text="Incorrecto", fg="red")

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Juego de Multiplicación")

label_numeros = tk.Label(ventana, text="", font=("Arial", 24))
label_numeros.pack(pady=20)

boton_opcion1 = tk.Button(ventana, text="", font=("Arial", 18))
boton_opcion1.pack(pady=10)

boton_opcion2 = tk.Button(ventana, text="", font=("Arial", 18))
boton_opcion2.pack(pady=10)

boton_opcion3 = tk.Button(ventana, text="", font=("Arial", 18))
boton_opcion3.pack(pady=10)

label_resultado = tk.Label(ventana, text="", font=("Arial", 18))
label_resultado.pack(pady=20)

boton_generar = tk.Button(ventana, text="Generar Números", command=generar_numeros, font=("Arial", 18))
boton_generar.pack(pady=20)

# Generar los primeros números al iniciar el programa
generar_numeros()

ventana.mainloop()