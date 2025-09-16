# registro_socios.py
import tkinter as tk
from tkinter import ttk, messagebox
from socio import Estudiante, Profesor, GestorSocios


def mostrar_registro(main_frame):
    # Limpiar lo que había antes en el frame principal
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Frame contenedor
    frame = tk.Frame(main_frame, bg="#e6f2ff")  
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # ------------------ Formulario ------------------
    tk.Label(frame, text="Tipo de Socio:", font=("Arial", 12), bg="#e6f2ff").pack(pady=5)

    tipo_var = tk.StringVar(master=frame, value="Estudiante")
    combo_tipo = ttk.Combobox(frame, textvariable=tipo_var, values=["Estudiante", "Profesor"], state="readonly")
    combo_tipo.pack()

    tk.Label(frame, text="Nombre:", bg="#e6f2ff").pack(pady=5)
    entry_nombre = tk.Entry(frame)
    entry_nombre.pack()

    tk.Label(frame, text="Cédula:", bg="#e6f2ff").pack(pady=5)
    # 🔹 Validación para solo números
    vcmd = (frame.register(lambda P: P.isdigit() or P == ""), "%P")
    entry_ci = tk.Entry(frame, validate="key", validatecommand=vcmd)
    entry_ci.pack()

    tk.Label(frame, text="Correo:", bg="#e6f2ff").pack(pady=5)
    entry_correo = tk.Entry(frame)
    entry_correo.pack()

    extra_label = tk.Label(frame, text="Carrera:", bg="#e6f2ff")
    extra_label.pack(pady=5)
    entry_extra = tk.Entry(frame)
    entry_extra.pack()

    def actualizar_extra(event):
        extra_label.config(text="Carrera:" if tipo_var.get() == "Estudiante" else "Materia:")

    combo_tipo.bind("<<ComboboxSelected>>", actualizar_extra)

    gestor = GestorSocios()

    # ------------------ Tabla de socios ------------------
    tabla = ttk.Treeview(frame, columns=("tipo", "nombre", "ci", "correo", "extra"), show="headings", height=6)
    tabla.pack(pady=15, fill="x")

    for col in ("tipo", "nombre", "ci", "correo", "extra"):
        tabla.heading(col, text=col.capitalize())
        tabla.column(col, width=100)

    # Cargar socios existentes al iniciar
    for s in gestor.leer_todos():
        tabla.insert("", "end", values=s)

    # ------------------ Funciones ------------------
    def registrar():
        nombre = entry_nombre.get().strip()
        ci = entry_ci.get().strip()
        correo = entry_correo.get().strip()
        extra = entry_extra.get().strip()
        tipo = tipo_var.get()

        if not nombre or not ci or not correo or not extra:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        try:
            if tipo == "Estudiante":
                socio = Estudiante(nombre, ci, correo, extra)
            else:
                socio = Profesor(nombre, ci, correo, extra)

            gestor.guardar(socio)
            tabla.insert("", "end", values=socio.to_line().strip().split(","))
            messagebox.showinfo("Éxito", f"{tipo} registrado correctamente")

            # Limpiar entradas
            entry_nombre.delete(0, tk.END)
            entry_ci.delete(0, tk.END)
            entry_correo.delete(0, tk.END)
            entry_extra.delete(0, tk.END)

        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(frame, text="Registrar", command=registrar).pack(pady=10)
