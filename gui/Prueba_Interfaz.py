import tkinter as tk
from tkinter import ttk

imagen = Image.open(r"resources\ElCerp.png").resize((80, 80))
logo = ImageTk.PhotoImage(imagen)
tk.Label(ventana, image=logo).place(x=1150, y=10)

imagen2 = Image.open(r"resources\Logo_ANEP.png").resize((130, 65))
logo2 = ImageTk.PhotoImage(imagen2)
tk.Label(ventana, image=logo2).place(x=10, y=10)

# _____________Título_____________
titulo = tk.Label(ventana, text="Biblioteca Cerp del Litoral", font=("Arial", 24, "bold"))
titulo.place(x=450, y=30)

#__________________Frame del formularios____________________
form_frame = tk.Frame(ventana)
form_frame.place(x=100, y=150)

# --- Ventana principal ---
ventana = tk.Tk()
ventana.title("Biblioteca CERP del Litoral")
ventana.geometry("1280x720")
ventana.configure(bg="#68A1FC")



# --- Frame lateral izquierdo ---
sidebar = tk.Frame(ventana, bg="#68A1FC", width=200)
sidebar.pack(side="left", fill="y")

# Botones del menú lateral
btn_libros = tk.Button(sidebar, text="Libros", width=15, height=2)
btn_libros.pack(pady=20)

btn_prestamos = tk.Button(sidebar, text="Préstamos", width=15, height=2)
btn_prestamos.pack(pady=20)

btn_devoluciones = tk.Button(sidebar, text="Devoluciones", width=15, height=2)
btn_devoluciones.pack(pady=20)

btn_socios = tk.Button(sidebar, text="Socios", width=15, height=2)
btn_socios.pack(pady=20)

# --- Frame principal ---
main_frame = tk.Frame(ventana, bg="#FCB168")
main_frame.pack(side="right", expand=True, fill="both")

# --- Título de sección ---
titulo = tk.Label(main_frame, text="Libros", font=("Arial", 20, "bold"), bg="white")
titulo.pack(pady=10)

# --- Barra de búsqueda ---
search_frame = tk.Frame(main_frame, bg="#FCB168")
search_frame.pack(pady=10)

tk.Label(search_frame, text="🔍", bg="white", font=("Arial", 14)).pack(side="left", padx=5)
search_entry = tk.Entry(search_frame, width=40)
search_entry.pack(side="left", padx=5)

# --- Tabla de libros ---
tabla_frame = tk.Frame(main_frame, bg="white")
tabla_frame.pack(padx=20, pady=10, fill="both", expand=True)

# Definimos columnas
columnas = ("nombre", "autor", "anio", "cantidad", "estado")
tabla = ttk.Treeview(tabla_frame, columns=columnas, show="headings", height=15)

# Encabezados
tabla.heading("nombre", text="Nombre")
tabla.heading("autor", text="Autor")
tabla.heading("anio", text="Año")
tabla.heading("cantidad", text="Cantidad")
tabla.heading("estado", text="Disponible")

# Ancho de columnas
tabla.column("nombre", width=200)
tabla.column("autor", width=150)
tabla.column("anio", width=60)
tabla.column("cantidad", width=80)
tabla.column("estado", width=100)

tabla.pack(fill="both", expand=True)

style = ttk.Style()
style.theme_use("clam")  # Tema que permite personalizar
style.configure(
    "Custom.Treeview",
    rowheight=25,  # Alto de cada fila
    background="white",
    fieldbackground="white",
    bordercolor="gray",
    borderwidth=1
)
style.configure("Custom.Treeview.Heading", font=("Arial", 11, "bold"))
style.map("Custom.Treeview", background=[("selected", "#D0E7FF")])

tabla.tag_configure("disponible", foreground="green")
tabla.tag_configure("prestado", foreground="red")

# Ejemplo de filas (de prueba)
tabla.insert("", "end", values=("El Quijote", "Cervantes", "1605", 3, "Disponible"),tags=("disponible",))
tabla.insert("", "end", values=("1984", "George Orwell", "1949", 1, "Prestado"),tags=("prestado",))

ventana.mainloop()
