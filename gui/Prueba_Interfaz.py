import tkinter as tk
from PIL import Image, ImageTk
from registro_socios import mostrar_registro

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

def limpiar_main():
    for widget in main_frame.winfo_children():
        widget.destroy()

# -----------------------------
# Ventana principal
# -----------------------------
ventana = tk.Tk()
ventana.title("Biblioteca CERP del Litoral")
ventana.geometry("1000x600")

# -----------------------------
# Frame superior (logo + título)
# -----------------------------
top_frame = tk.Frame(ventana, bg="#FFD39E", height=80)
top_frame.pack(side="top", fill="x")

# Logo Cerp
imagen = Image.open(r"resources\ElCerp.png").resize((80, 80))
logo_cerp = ImageTk.PhotoImage(imagen)
logo_label = tk.Label(top_frame, image=logo_cerp, bg="#FFD39E")
logo_label.pack(side="left", padx=25, pady=10)

# Título
titulo = tk.Label(top_frame, text="Biblioteca CERP del Litoral", font=("Arial", 20, "bold"), bg="#FFD39E")
titulo.pack(pady=10, anchor="center")

# -----------------------------
# Menú lateral
# -----------------------------
sidebar = tk.Frame(ventana, width=200, bg="#FFD39E")
sidebar.pack(side="left", fill="y")

tk.Label(sidebar, text="Menú", bg="#FFD39E", font=("Arial", 14, "bold")).pack(pady=10)

tk.Button(sidebar, text="Socios", width=15, height=2, command=mostrar_socios).pack(pady=10)
tk.Button(sidebar, text="Libros", width=15, height=2, command=mostrar_libros).pack(pady=10)
tk.Button(sidebar, text="Préstamos", width=15, height=2, command=mostrar_prestamos).pack(pady=10)
tk.Button(sidebar, text="Devoluciones", width=15, height=2, command=mostrar_devoluciones).pack(pady=10)

# Logo ANEP (abajo a la izquierda)
imagen_anep = Image.open(r"resources\Logo_ANEP.png").resize((135, 65))
logo_anep = ImageTk.PhotoImage(imagen_anep)
logo_anep_label = tk.Label(sidebar, image=logo_anep, bg="#FFD39E")
logo_anep_label.pack(side="bottom", pady=20)

# -----------------------------
# Área principal
# -----------------------------
main_frame = tk.Frame(ventana, bg="white")
main_frame.pack(side="right", fill="both", expand=True)

ventana.mainloop()
