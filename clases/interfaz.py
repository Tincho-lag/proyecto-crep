import tkinter as tk

ventana = tk.Tk()
ventana.title("Biblioteca Cerp del Litoral")
ventana.geometry("1280x720")

etiqueta_material = tk.Label(ventana, text="Material:")
etiqueta_material.pack(pady=10)
entrada_material = tk.Entry(ventana)
entrada_material.pack(pady=5)

def mostrar_material():
    material = entrada_material.get()  # Obtiene el texto escrito
    resultado_material.config(text=f"El {material} se encuentra disponible.")

boton_material = tk.Button(ventana, text="Buscar", command=mostrar_material)
boton_material.pack(pady=10)

resultado_material = tk.Label(ventana, text="")
resultado_material.pack(pady=10)

#___________Socios_____________________________________________________
etiqueta_socio = tk.Label(ventana, text="Socios:")
etiqueta_socio.pack(pady=10)
entrada_socio = tk.Entry(ventana)
entrada_socio.pack(pady=5)

def mostrar_socio():
    nombre = entrada_socio.get()  # Obtiene el texto escrito
    resultado_socio.config(text=f"¡Hola, {nombre}!")

boton_socio = tk.Button(ventana, text="Saludar", command=mostrar_socio)
boton_socio.pack(pady=10)


resultado_socio = tk.Label(ventana, text="")
resultado_socio.pack(pady=10)
ventana.mainloop()
