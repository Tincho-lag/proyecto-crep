# registro_socios.py
import tkinter as tk
from tkinter import ttk, messagebox
from socio import Estudiante, Profesor, GestorSocios


def ventana_registro():
    reg = tk.Toplevel()
    reg.title("Registro de Socios")
    reg.geometry("500x400")

    # ----------- Campos básicos -----------
    tk.Label(reg, text="Nombre").pack(pady=5)
    entry_nombre = tk.Entry(reg)
    entry_nombre.pack()

    tk.Label(reg, text="Cédula").pack(pady=5)
    entry_ci = tk.Entry(reg)
    entry_ci.pack()

    tk.Label(reg, text="Correo").pack(pady=5)
    entry_correo = tk.Entry(reg)
    entry_correo.pack()

    # ----------- Tipo de socio -----------
    tk.Label(reg, text="Tipo de socio").pack(pady=5)
    tipo_var = tk.StringVar(value="Estudiante")
    combo_tipo = ttk.Combobox(
        reg,
        textvariable=tipo_var,
        values=["Estudiante", "Profesor"],
        state="readonly"
    )
    combo_tipo.pack()

    # Campo adicional (Carrera/Materia)
    extra_label = tk.Label(reg, text="Carrera")
    extra_label.pack(pady=5)
    entry_extra = tk.Entry(reg)
    entry_extra.pack()

    # Cambia el label según el tipo
    def actualizar_extra(event):
        if tipo_var.get() == "Estudiante":
            extra_label.config(text="Carrera")
        else:
            extra_label.config(text="Materia")

    combo_tipo.bind("<<ComboboxSelected>>", actualizar_extra)

    # ----------- Botón Registrar -----------
    def registrar():
        nombre = entry_nombre.get()
        ci = entry_ci.get()
        correo = entry_correo.get()
        extra = entry_extra.get()
        tipo = tipo_var.get()

        # Validación
        if not nombre or not ci or not correo or not extra:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Crear socio según el tipo
        if tipo == "Estudiante":
            socio = Estudiante(nombre, ci, correo, extra)
        else:
            socio = Profesor(nombre, ci, correo, extra)

        # Guardar socio en archivo
        GestorSocios.guardar(socio)
        messagebox.showinfo("Éxito", f"{tipo} registrado correctamente")
        reg.destroy()

    tk.Button(reg, text="Registrar", command=registrar).pack(pady=20)
