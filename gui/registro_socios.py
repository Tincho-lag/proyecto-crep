# registro_socios.py
import os
import tkinter as tk
from tkinter import ttk, messagebox

# ---------------- RUTA DEL ARCHIVO DE DATOS ---------------- #
DATA_DIR = os.path.join(os.path.dirname(__file__), "../resources/data")
os.makedirs(DATA_DIR, exist_ok=True)
ARCHIVO_SOCIOS = os.path.join(DATA_DIR, "socios.txt")

# ---------------- Clases de socios ---------------- #
class Estudiante:
    def __init__(self, id_, nombre, ci, correo, carrera, domicilio, observaciones):
        self.id = id_
        self.nombre = nombre
        self.ci = ci
        self.correo = correo
        self.extra = carrera
        self.domicilio = domicilio
        self.observaciones = observaciones

    def to_list(self):
        return [self.id, "Estudiante", self.nombre, self.ci, self.correo, self.extra, self.domicilio, self.observaciones]

class Profesor:
    def __init__(self, id_, nombre, ci, correo, materia, domicilio, observaciones):
        self.id = id_
        self.nombre = nombre
        self.ci = ci
        self.correo = correo
        self.extra = materia
        self.domicilio = domicilio
        self.observaciones = observaciones

    def to_list(self):
        return [self.id, "Profesor", self.nombre, self.ci, self.correo, self.extra, self.domicilio, self.observaciones]

# ---------------- Gestor de socios ---------------- #
class GestorSocios:
    def __init__(self, archivo=ARCHIVO_SOCIOS):
        self.archivo = archivo
        self.socios = self.leer_todos()

    def leer_todos(self):
        socios = []
        if os.path.exists(self.archivo):
            with open(self.archivo, "r", encoding="utf-8") as f:
                for linea in f:
                    linea = linea.strip()
                    if linea:
                        socios.append(linea.split(","))
        return socios

    def guardar(self, socio):
        self.socios.append(socio.to_list())
        self.guardar_todos()

    def guardar_todos(self):
        with open(self.archivo, "w", encoding="utf-8") as f:
            for s in self.socios:
                f.write(",".join(s) + "\n")

    def eliminar_por_id(self, id_):
        self.socios = [s for s in self.socios if s[0] != id_]
        self.guardar_todos()

# ---------------- Generar ID automático ---------------- #
def generar_id_simple(archivo=ARCHIVO_SOCIOS):
    if not os.path.exists(archivo):
        return "001"
    with open(archivo, "r", encoding="utf-8") as f:
        lineas = [line.strip() for line in f if line.strip()]
        if not lineas:
            return "001"
        ultimo_id = lineas[-1].split(",")[0]
        return f"{int(ultimo_id)+1:03}"

# ---------------- GUI para registrar socios ---------------- #
def mostrar_registro(main_frame):
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
    combo_tipo = ttk.Combobox(form_frame, textvariable=tipo_var, values=["Estudiante", "Profesor"], state="readonly")
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

    # --- TABLA ---
    cols = ("ID", "Tipo de socio", "Nombre", "CI", "Correo", "Extra", "Domicilio", "Observaciones")
    tabla = ttk.Treeview(frame, columns=cols, show="headings", height=8)
    tabla.pack(fill="both", expand=True, pady=10)

    for col in cols:
        tabla.heading(col, text=col, anchor="center")
        tabla.column(col, width=120, anchor="center")

    # --- FUNCIONES ---
    def actualizar_tabla():
        tabla.delete(*tabla.get_children())
        for socio in gestor.leer_todos():
            tabla.insert("", "end", values=socio)

    def limpiar_campos():
        for entry in entries.values():
            if entry.cget("state") == "normal":
                entry.delete(0, tk.END)
        entry_obs.delete("1.0", tk.END)
        asignar_id()

    def asignar_id():
        nuevo_id = generar_id_simple(gestor.archivo)
        entries["ID:"].config(state="normal")
        entries["ID:"].delete(0, tk.END)
        entries["ID:"].insert(0, nuevo_id)
        entries["ID:"].config(state="readonly")

    def registrar():
        id_ = entries["ID:"].get()
        nombre = entries["Nombre:"].get()
        ci = entries["Cédula:"].get()
        correo = entries["Correo:"].get()
        carrera = entries["Carrera/Materia:"].get()
        domicilio = entries["Domicilio:"].get()
        observaciones = entry_obs.get("1.0", tk.END).strip()
        tipo = tipo_var.get()

        if not nombre or not ci or not correo or not carrera or not domicilio:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        if tipo == "Estudiante":
            socio = Estudiante(id_, nombre, ci, correo, carrera, domicilio, observaciones)
        else:
            socio = Profesor(id_, nombre, ci, correo, carrera, domicilio, observaciones)

        gestor.guardar(socio)
        actualizar_tabla()
        limpiar_campos()
        messagebox.showinfo("Éxito", f"{tipo} registrado correctamente")

    def eliminar():
        item = tabla.selection()
        if not item:
            messagebox.showerror("Error", "Seleccione un socio para eliminar")
            return
        valores = tabla.item(item, "values")
        id_borrar = valores[0]
        gestor.eliminar_por_id(id_borrar)
        actualizar_tabla()
        limpiar_campos()
        messagebox.showinfo("Éxito", "Socio eliminado")

    # --- BOTONES ---
    botones = tk.Frame(frame, bg="#e6f2ff")
    botones.pack(fill="x", pady=10)

    tk.Button(botones, text="Registrar", command=registrar, bg="#4CAF50", fg="white").pack(side="left", padx=5)
    tk.Button(botones, text="Eliminar", command=eliminar, bg="#f44336", fg="white").pack(side="left", padx=5)
    tk.Button(botones, text="Limpiar", command=limpiar_campos, bg="#9E9E9E", fg="white").pack(side="left", padx=5)

    # --- Inicializar ---
    asignar_id()
    actualizar_tabla()
