# registro_socios.py
import tkinter as tk
from tkinter import ttk, messagebox
from socio import Estudiante, Profesor, GestorSocios


def mostrar_registro(main_frame):
    # Limpiar lo que había antes en el frame principal
    for widget in main_frame.winfo_children():
        widget.destroy()

    # Frame contenedor con color de fondo
    frame = tk.Frame(main_frame, bg="#e6f2ff")  # 💡 color celeste claro
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    # Tipo de socio
    tk.Label(frame, text="Tipo de Socio:", font=("Arial", 12), bg="#e6f2ff").pack(pady=5)

    # 🔹 StringVar con master=frame para evitar errores
    tipo_var = tk.StringVar(master=frame, value="Estudiante")

    combo_tipo = ttk.Combobox(
        frame, textvariable=tipo_var, values=["Estudiante", "Profesor"], state="readonly"
    )
    combo_tipo.pack()

    # Nombre
    tk.Label(frame, text="Nombre:", bg="#e6f2ff").pack(pady=5)
    entry_nombre = tk.Entry(frame)
    entry_nombre.pack()

    # Cédula
    tk.Label(frame, text="Cédula:", bg="#e6f2ff").pack(pady=5)
    entry_ci = tk.Entry(frame)
    entry_ci.pack()

    # Correo
    tk.Label(frame, text="Correo:", bg="#e6f2ff").pack(pady=5)
    entry_correo = tk.Entry(frame)
    entry_correo.pack()

    # Carrera/Materia
    extra_label = tk.Label(frame, text="Carrera:", bg="#e6f2ff")
    extra_label.pack(pady=5)
    entry_extra = tk.Entry(frame)
    entry_extra.pack()

    def actualizar_extra(event):
        if tipo_var.get() == "Estudiante":
            extra_label.config(text="Carrera:")
        else:
            extra_label.config(text="Materia:")

    combo_tipo.bind("<<ComboboxSelected>>", actualizar_extra)

    gestor = GestorSocios()

    # Botón para registrar socio
    def registrar():
        nombre = entry_nombre.get()
        ci = entry_ci.get()
        correo = entry_correo.get()
        extra = entry_extra.get()
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
            messagebox.showinfo("Éxito", f"{tipo} registrado correctamente")
        except ValueError as e:
            messagebox.showerror("Error", str(e))

    tk.Button(frame, text="Registrar", command=registrar).pack(pady=10)

    # Botón para ver todos los socios
    def ver_socios():
        socios = gestor.leer_todos()
        if not socios:
            messagebox.showinfo("Socios", "No hay socios registrados aún.")
        else:
            listado = "\n".join([", ".join(s) for s in socios])
            messagebox.showinfo("Socios registrados", listado)

    tk.Button(frame, text="Ver socios", command=ver_socios).pack(pady=5)
