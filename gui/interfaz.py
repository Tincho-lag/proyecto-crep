import tkinter as tk
from PIL import Image, ImageTk
from gui.registro_socios import mostrar_registro  

def limpiar_main():
    for widget in main_frame.winfo_children():
        widget.destroy()

def mostrar_socios():
    mostrar_registro(main_frame)

def mostrar_libros():
    limpiar_main()
    tk.Label(main_frame, text="Gestión de Libros", font=("Arial", 16)).pack(pady=20)

def mostrar_prestamos():
    limpiar_main()
    tk.Label(main_frame, text="Gestión de Préstamos", font=("Arial", 16)).pack(pady=20)

def mostrar_devoluciones():
    limpiar_main()
    tk.Label(main_frame, text="Gestión de Devoluciones", font=("Arial", 16)).pack(pady=20)

# _________________Se crea la ventana principal_________________ # 
ventana = tk.Tk()
ventana.title("Biblioteca CERP del Litoral")
ventana.geometry("1280x720")

# ____________________Frame superior_____________________ #
top_frame = tk.Frame(ventana, bg="#FFD39E", height=80)
top_frame.pack(side="top", fill="x")

#_________________Logos y título_________________#
imagen = Image.open(r"resources/images/ElCerp.png").resize((80, 80))
logo_cerp = ImageTk.PhotoImage(imagen)
tk.Label(top_frame, image=logo_cerp, bg="#FFD39E").pack(side="left", padx=25, pady=10)

tk.Label(top_frame, text="Biblioteca CERP del Litoral", font=("Arial", 20, "bold"), bg="#FFD39E").pack(pady=10)

#______________Frame principal__________________#
main_frame = tk.Frame(ventana, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

#__________frame izquierdo (menú)__________#
left_frame = tk.Frame(ventana, width=200, bg="#FFD39E")
left_frame.pack(side="left", fill="y")

tk.Label(left_frame, text="Menú", bg="#FFD39E", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(left_frame, text="Socios", width=15, height=2, command=mostrar_socios).pack(pady=10)
tk.Button(left_frame, text="Libros", width=15, height=2, command=mostrar_libros).pack(pady=10)
tk.Button(left_frame, text="Préstamos", width=15, height=2, command=mostrar_prestamos).pack(pady=10)
tk.Button(left_frame, text="Devoluciones", width=15, height=2, command=mostrar_devoluciones).pack(pady=10)

# Logo ANEP
imagen_anep = Image.open(r"resources/images/Logo_ANEP.png").resize((135, 65))
logo_anep = ImageTk.PhotoImage(imagen_anep)
tk.Label(left_frame, image=logo_anep, bg="#FFD39E").pack(side="bottom", pady=20)

# ___ Ejecutar ventana______________#
ventana.mainloop()
