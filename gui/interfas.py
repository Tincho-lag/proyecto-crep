import tkinter as tk
from PIL import Image, ImageTk

ventana = tk.Tk()
ventana.title("Biblioteca Cerp del Litoral")
ventana.geometry("1280x720")

#___________Logo Cerp_____________________________________________________
imagen = Image.open(r"C:\ProyectoCrep\proyecto-crep\clases\ElCerp.png")
imagen = imagen.resize((80, 80))  
logo = ImageTk.PhotoImage(imagen)

# Mostrar logo en la esquina superior derecha
logo_label = tk.Label(ventana, image=logo)
logo_label.image = logo  # evitar que Python lo elimine de memoria
logo_label.place(x=1150, y=10)


#_____________Logo anep____________________________________________________
imagen2 = Image.open(r"C:\ProyectoCrep\proyecto-crep\clases\Logo_ANEP.png")
imagen2 = imagen2.resize((65, 130))
logo2 = ImageTk.PhotoImage(imagen2)

# Ponerla en la esquina superior izquierda
logo_label2 = tk.Label(ventana, image=logo2)
logo_label2.image = logo2
logo_label2.place(x=10, y=10)


#___________ Muestra el formulario, lo mueve hacia la drecha _____________________________________________
form_frame = tk.Frame(ventana)
form_frame.place(x=150, y=50)
#___________Isbn_____________________________________________________

tk.Label(ventana, text="Isbn:").grid(row=6, column=0, padx=10, pady=10, sticky="e")
entrada_isbn = tk.Entry(ventana, bd=3, width=30)
entrada_isbn.grid(row=7, column=2, pady=10)

#___________Socios_____________________________________________________
tk.Label(ventana, text="Socios:").grid(row=7, column=0, padx=10, pady=10, sticky="e")
entrada_socios = tk.Entry(ventana, bd=3, width=30)  
entrada_socios.grid(row=8, column=2, pady=10)



# Frame para el formulario
ventana.mainloop()