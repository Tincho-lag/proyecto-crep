# registro_socios.py
import tkinter as tk
from tkinter import ttk, messagebox
from socio import Estudiante, Profesor, GestorSocios, generar_id

def mostrar_registro(main_frame):
    # Limpiar frame principal
    for widget in main_frame.winfo_children():
        widget.destroy()

    frame = tk.Frame(main_frame, bg="#e6f2ff")
    frame.pack(fill="both", expand=True, padx=20, pady=20)

    gestor = GestorSocios()

    # --- FORMULARIO ---
    form_frame = tk.Frame(frame, bg="#e6f2ff")
    form_frame.pack(fill="x", pady=5)

    tipo_var = tk.StringVar(value="Estudiante")
    entries = {}

    tk.Label(form_frame, text="Tipo de Socio:", bg="#e6f2ff").grid(row=0, column=0, sticky="e", pady=2)
    combo_tipo = ttk.Combobox(form_frame, textvariable=tipo_var, values=["Estudiante","Profesor"], state="readonly")
    combo_tipo.grid(row=0, column=1, sticky="w", pady=2)

    labels = ["ID:", "Nombre:", "Cédula:", "Correo:", "Carrera/Materia:", "Domicilio:"]
    for i, label in enumerate(labels, start=1):
        tk.Label(form_frame, text=label, bg="#e6f2ff").grid(row=i, column=0, sticky="e", pady=2)
        entry = tk.Entry(form_frame, width=40)
        entry.grid(row=i, column=1, sticky="w", pady=2)
        entries[label] = entry

    entries["ID:"].config(state="readonly")

    tk.Label(form_frame, text="Observaciones:", bg="#e6f2ff").grid(row=len(labels)+1, column=0, sticky="ne", pady=2)
    entry_obs = tk.Text(form_frame, width=40, height=3)
    entry_obs.grid(row=len(labels)+1, column=1, sticky="w", pady=2)

    # --- TREEVIEW ---
    tabla_frame = tk.Frame(frame)
    tabla_frame.pack(fill="both", expand=True, pady=10)

    cols = ("ID","Tipo","Nombre","CI","Correo","Extra","Domicilio","Observaciones")
    tabla = ttk.Treeview(tabla_frame, columns=cols, show="headings", height=8)
    scroll_y = ttk.Scrollbar(tabla_frame, orient="vertical", command=tabla.yview)
    tabla.configure(yscrollcommand=scroll_y.set)
    scroll_y.pack(side="right", fill="y")
    tabla.pack(fill="both", expand=True)

    for col in cols:
        tabla.heading(col, text=col, anchor="center")
        if col == "Observaciones":
            tabla.column(col, width=200, anchor="center")
        elif col == "ID":
            tabla.column(col, width=50, anchor="center")
        else:
            tabla.column(col, width=120, anchor="center")

    # --- FUNCIONES ---
    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        for socio in gestor.leer_todos():
            tabla.insert("", "end", values=(
                socio[1],  # ID
                socio[0],  # Tipo
                socio[2],  # Nombre
                socio[3],  # CI
                socio[4],  # Correo
                socio[5],  # Carrera/Materia o Materia
                socio[6],  # Domicilio
                socio[7]   # Observaciones
            ))

    def limpiar_campos():
        for entry in entries.values():
            if entry.cget("state")=="normal":
                entry.delete(0, tk.END)
        entry_obs.delete("1.0", tk.END)

    def asignar_id():
        nuevo_id = generar_id(gestor.archivo)
        entries["ID:"].config(state="normal")
        entries["ID:"].delete(0, tk.END)
        entries["ID:"].insert(0, nuevo_id)
        entries["ID:"].config(state="readonly")

    def registrar():
        nombre = entries["Nombre:"].get()
        ci = entries["Cédula:"].get()
        correo = entries["Correo:"].get()
        extra = entries["Carrera/Materia:"].get()
        domicilio = entries["Domicilio:"].get()
        observaciones = entry_obs.get("1.0", tk.END).strip()
        tipo = tipo_var.get()
        id_ = entries["ID:"].get()

        if not nombre or not ci or not correo or not extra or not domicilio:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if tipo=="Estudiante":
            socio = Estudiante(id_, nombre, ci, correo, extra, domicilio, observaciones)
        else:
            socio = Profesor(id_, nombre, ci, correo, extra, domicilio, observaciones)

        gestor.guardar(socio)
        actualizar_tabla()       # <--- actualizar antes de limpiar
        limpiar_campos()
        asignar_id()
        messagebox.showinfo("Éxito", f"{tipo} registrado correctamente")

    def seleccionar(event):
        item = tabla.selection()
        if not item: return
        valores = tabla.item(item,"values")
        entries["ID:"].config(state="normal")
        entries["ID:"].delete(0, tk.END)
        entries["ID:"].insert(0, valores[0])
        entries["ID:"].config(state="readonly")
        tipo_var.set(valores[1])
        entries["Nombre:"].delete(0, tk.END)
        entries["Nombre:"].insert(0, valores[2])
        entries["Cédula:"].delete(0, tk.END)
        entries["Cédula:"].insert(0, valores[3])
        entries["Correo:"].delete(0, tk.END)
        entries["Correo:"].insert(0, valores[4])
        entries["Carrera/Materia:"].delete(0, tk.END)
        entries["Carrera/Materia:"].insert(0, valores[5])
        entries["Domicilio:"].delete(0, tk.END)
        entries["Domicilio:"].insert(0, valores[6])
        entry_obs.delete("1.0", tk.END)
        entry_obs.insert("1.0", valores[7])

    tabla.bind("<<TreeviewSelect>>", seleccionar)

    def eliminar():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error","Seleccione un socio para eliminar")
            return
        valores = tabla.item(item,"values")
        id_borrar = valores[0]
        nuevos = [s for s in gestor.leer_todos() if s[1]!=id_borrar]
        with open(gestor.archivo,"w",encoding="utf-8") as f:
            for s in nuevos:
                f.write(",".join(s)+"\n")
        actualizar_tabla()
        limpiar_campos()
        asignar_id()
        messagebox.showinfo("Éxito","Socio eliminado")

    def editar():
        eliminar()
        registrar()

    # --- BOTONES ---
    botones_frame = tk.Frame(frame, bg="#e6f2ff")
    botones_frame.pack(side="bottom", fill="x", pady=10)

    def crear_boton(texto, comando, bg, fg, width):
        btn = tk.Button(botones_frame, text=texto, command=comando, bg=bg, fg=fg, width=width)
        btn.pack(side="left", padx=5)
        return btn

    crear_boton("Registrar", registrar, "#4CAF50","white",12)
    crear_boton("Editar", editar, "#2196F3","white",12)
    crear_boton("Eliminar", eliminar, "#f44336","white",12)
    crear_boton("Limpiar", limpiar_campos, "#9E9E9E","white",12)
    crear_boton("Actualizar Tabla", actualizar_tabla, "#FF9800","white",15)

    # --- Generar primer ID y actualizar tabla ---
    asignar_id()
    actualizar_tabla()
