# interfas.py
# interfas parte del repositorio martin 
# sabado 13 septiembre 
import tkinter as tk

# Configuración de la ventana principal
ventana = tk.Tk()
ventana.title("Biblioteca Cerp del Litoral")
ventana.geometry("1280x720")

etiqueta = tk.Label(ventana, text="Material:")
etiqueta.pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def mostrar_texto():
    material = entrada.get()  # Obtiene el texto escrito
    resultado.config(text=f"El {material} se encuentra disponible.")

boton = tk.Button(ventana, text="Buscar", command=mostrar_texto)
boton.pack(pady=10)

resultado_material = tk.Label(ventana, text="")
resultado_material.pack(pady=10)

#___________Socios_____________________________________________________
etiqueta = tk.Label(ventana, text="Socios:")
etiqueta.pack(pady=10)
entrada = tk.Entry(ventana)
entrada.pack(pady=5)

def mostrar_texto():
    nombre = entrada.get()  # Obtiene el texto escrito
    resultado.config(text=f"¡Hola, {nombre}!")

boton = tk.Button(ventana, text="Saludar", command=mostrar_texto)
boton.pack(pady=10)


resultado = tk.Label(ventana, text="")
resultado.pack(pady=10)
ventana.mainloop()
