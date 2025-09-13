import tkinter as tk

ventana = tk.Tk()
ventana.title("Mi primera GUI")
ventana.geometry("300x200")

etiqueta = tk.Label(ventana, text="Escribe tu nombre:")
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


