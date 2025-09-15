import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# ------------------- Ventana principal -------------------
ventana = tk.Tk()
ventana.title("Biblioteca CERP del Litoral")
ventana.geometry("1280x720")
ventana.configure(bg="#FAFAFA")

# ------------------- Frame superior (para logos y título) -------------------
top_frame = tk.Frame(ventana, bg="#FAFAFA", height=100)
top_frame.pack(side="top", fill="x")

# Logo Cerp
imagen_cerp = Image.open(r"resources\ElCerp.png").resize((80, 80))
logo_cerp = ImageTk.PhotoImage(imagen_cerp)
tk.Label(top_frame, image=logo_cerp, bg="#FAFAFA").pack(side="right", padx=20, pady=10)

# Logo ANEP
imagen_anep = Image.open(r"resources\Logo_ANEP.png").resize((130, 65))
logo_anep = ImageTk.PhotoImage(imagen_anep)
tk.Label(top_frame, image=logo_anep, bg="#FAFAFA").pack(side="left", padx=20, pady=10)

# Título principal
titulo_principal = tk.Label(
    top_frame,
    text="Biblioteca Cerp del Litoral",
    font=("Arial", 24, "bold"),
    bg="#FAFAFA"
)
titulo_principal.pack(expand=True)

# ------------------- Frame lateral izquierdo -------------------
sidebar = tk.Frame(ventana, bg="#A0A0A0", width=200)
sidebar.pack(side="left", fill="y")

# Botones del menú lateral
botones = ["Libros", "Préstamos", "Devoluciones", "Socios"]
for texto in botones:
    tk.Button(sidebar, text=texto, width=15, height=2).pack(pady=20)

# ------------------- Frame principal -------------------
main_frame = tk.Frame(ventana, bg="#ECECEC")
main_frame.pack(side="right", expand=True, fill="both")

# Título de sección
titulo_seccion = tk.Label(
    main_frame,
    text="Libros",
    font=("Arial", 20, "bold"),
    bg="white"
)
titulo_seccion.pack(pady=10, fill="x")

# ------------------- Barra de búsqueda -------------------
search_frame = tk.Frame(main_frame, bg="#B0B0B0")
search_frame.pack(pady=10)

tk.Label(search_frame, text="🔍", bg="#A0A0A0", font=("Arial", 14)).pack(side="left", padx=5)
search_entry = tk.Entry(search_frame, width=40)
search_entry.pack(side="left", padx=5)

# ------------------- Tabla de libros -------------------
tabla_frame = tk.Frame(main_frame, bg="white")
tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

columnas = ("nombre", "autor", "año", "cantidad", "estado")
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=15)

# Encabezados
for col, ancho in zip(columnas, [200, 150, 60, 80, 100]):
    tabla.heading(col, text=col.capitalize())
    tabla.column(col, width=ancho)

tabla.pack(fill="both", expand=True)

# ------------------- Estilo de la tabla -------------------
style = ttk.Style()
style.theme_use("clam")
style.configure(
    "Custom.Treeview",
    rowheight=25,
    background="white",
    fieldbackground="white",
    bordercolor="gray",
    borderwidth=1
)
style.configure("Custom.Treeview.Heading", font=("Arial", 11, "bold"))
style.map("Custom.Treeview", background=[("selected", "#D0E7FF")])

tabla.tag_configure("disponible", foreground="green")
tabla.tag_configure("prestado", foreground="red")

# Filas de ejemplo
tabla.insert("", "end", values=("El Quijote", "Cervantes", "1605", 3, "Disponible"), tags=("disponible",))
tabla.insert("", "end", values=("1984", "George Orwell", "1949", 1, "Prestado"), tags=("prestado",))

# ------------------- Ejecutar ventana -------------------
ventana.mainloop()
