import os
import sys
import tkinter as tk
from tkinter import messagebox, ttk
from PIL import Image, ImageTk

# --- Asegura que el proyecto pueda importar los módulos vecinos ---
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# --- Importa tus módulos del dominio ---
from objetos.biblioteca import SistemaBiblioteca
from objetos.elemento import Libro, Recursos
from objetos.usuario import Estudiante, Profesor
from objetos.utilidades import guardar_materiales, cargar_materiales, guardar_usuarios, cargar_usuarios

# Función opcional para mostrar registro de socios
try:
    from gui.registro_socios import mostrar_registro
except Exception:
    mostrar_registro = None


class BibliotecaApp:
    def __init__(self, ventana):
        self.sistema = SistemaBiblioteca()
        try:
            cargar_materiales(self.sistema)
            cargar_usuarios(self.sistema)
        except Exception as e:
            print("Aviso carga inicial:", e)

        self.ventana = ventana
        self.ventana.title("Biblioteca CERP del Litoral")
        self.ventana.geometry("1280x720")
        self.ventana.configure(bg="#E9ECEF")

        self.COLOR_PRINCIPAL = "#E3E6EA"
        self.COLOR_BOTONES = "#D0D4D9"
        self.COLOR_BOTON_HOVER = "#C1C6CC"
        self.COLOR_TEXTO = "#2C2C2C"
        self.COLOR_FONDO = "#F4F4F4"

        # --- Top Frame ---
        self.top_frame = tk.Frame(self.ventana, bg=self.COLOR_PRINCIPAL, height=90)
        self.top_frame.pack(side="top", fill="x")
        header_content = tk.Frame(self.top_frame, bg=self.COLOR_PRINCIPAL)
        header_content.pack(side="left", padx=25, pady=10)

        self.logo_cerp = None
        try:
            imagen = Image.open(r"resources/images/ElCerp.png").resize((70, 70))
            self.logo_cerp = ImageTk.PhotoImage(imagen)
            tk.Label(header_content, image=self.logo_cerp, bg=self.COLOR_PRINCIPAL).pack(side="left", padx=10)
        except Exception:
            tk.Label(header_content, text="[ElCerp]", bg=self.COLOR_PRINCIPAL, fg=self.COLOR_TEXTO,
                     font=("Segoe UI", 10, "bold")).pack(side="left", padx=10)

        tk.Label(header_content, text="Biblioteca CERP del Litoral",
                 font=("Segoe UI", 22, "bold"), bg=self.COLOR_PRINCIPAL, fg=self.COLOR_TEXTO).pack(side="left", padx=15)

        # --- Menú lateral ---
        self.left_frame = tk.Frame(self.ventana, width=220, bg=self.COLOR_PRINCIPAL)
        self.left_frame.pack(side="left", fill="y")

        tk.Label(self.left_frame, text="Menú", bg=self.COLOR_PRINCIPAL,
                 font=("Segoe UI", 14, "bold"), fg=self.COLOR_TEXTO).pack(pady=15)

        self.estilo_boton = {"width": 18, "height": 2, "bg": self.COLOR_BOTONES, "fg": self.COLOR_TEXTO,
                             "relief": "flat", "font": ("Segoe UI", 11)}

        botones_info = [
            ("Catálogo", self.mostrar_catalogo),
            ("Agregar Material", self.abrir_agregar_material),
            ("Usuarios", self.mostrar_usuarios),
            ("Agregar Usuario", self.abrir_agregar_usuario),
            ("Préstamos", self.abrir_prestamo),
            ("Devoluciones", self.abrir_devolucion),
        ]

        for text, cmd in botones_info:
            b = tk.Button(self.left_frame, text=text, command=cmd, **self.estilo_boton)
            b.pack(pady=8)
            self._añadir_hover(b)

        b_salir = tk.Button(self.left_frame, text="Guardar y Salir", bg="#ff6666", fg="white",
                            width=18, height=2, font=("Segoe UI", 11, "bold"), command=self.guardar_y_salir)
        b_salir.pack(pady=18)

        self.logo_anep = None
        try:
            imagen_anep = Image.open(r"resources/images/Logo_ANEP.png").resize((120, 60))
            self.logo_anep = ImageTk.PhotoImage(imagen_anep)
            tk.Label(self.left_frame, image=self.logo_anep, bg=self.COLOR_PRINCIPAL).pack(side="bottom", pady=20)
        except Exception:
            tk.Label(self.left_frame, text="[ANEP]", bg=self.COLOR_PRINCIPAL, fg=self.COLOR_TEXTO,
                     font=("Segoe UI", 10, "bold")).pack(side="bottom", pady=20)

        self.main_frame = tk.Frame(self.ventana, bg=self.COLOR_FONDO)
        self.main_frame.pack(side="right", fill="both", expand=True)

        self.mostrar_catalogo()

    # ---------------- utilidades ----------------
    def _añadir_hover(self, boton):
        def on_enter(e):
            try:
                boton.configure(bg=self.COLOR_BOTON_HOVER)
            except Exception:
                pass
        def on_leave(e):
            try:
                boton.configure(bg=self.COLOR_BOTONES)
            except Exception:
                pass
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

    def limpiar_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ---------------- funciones ----------------
    def mostrar_catalogo(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="Catálogo de Materiales",
                 font=("Segoe UI", 16, "bold"), bg=self.COLOR_FONDO).pack(pady=12)

        columnas = ("Referencia", "Tipo", "ISBN/Autor", "Título", "Año", "Ejemplares")
        tree = ttk.Treeview(self.main_frame, columns=columnas, show="headings", height=20)
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=130, anchor="center")
        tree.pack(padx=10, pady=10, fill="both", expand=True)

        for mat in self.sistema.listar_materiales():
            if isinstance(mat, Libro):
                tree.insert("", tk.END, values=(mat.referencia, mat.tipo, f"{mat.isbn}/{mat.autor}", mat.titulo, mat.ano, mat.ejemplares_disponibles))
            else:
                tree.insert("", tk.END, values=(mat.referencia, mat.tipo, "", mat.titulo, "", mat.ejemplares_disponibles))

    def mostrar_usuarios(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="Usuarios Registrados",
                 font=("Segoe UI", 16, "bold"), bg=self.COLOR_FONDO).pack(pady=12)

        columnas = ("ID", "Nombre", "Domicilio", "Tipo")
        tree = ttk.Treeview(self.main_frame, columns=columnas, show="headings", height=20)
        for col in columnas:
            tree.heading(col, text=col)
            tree.column(col, width=180, anchor="center")
        tree.pack(padx=10, pady=10, fill="both", expand=True)

        for usuario in self.sistema.usuarios.values():
            tipo = "Estudiante" if isinstance(usuario, Estudiante) else "Profesor"
            tree.insert("", tk.END, values=(usuario.id_usuario, usuario.nombre, usuario.domicilio, tipo))

    # --- El resto de tus funciones (agregar material/usuario, préstamo, devolución, guardar y salir) se mantienen idénticas ---
    # ... pegar aquí las funciones abrir_agregar_material, abrir_agregar_usuario, abrir_prestamo, abrir_devolucion, guardar_y_salir


        # Crear botones y enlazar acciones
        botones_info = [
            ("Catálogo", self.mostrar_catalogo),
            ("Agregar Material", self.abrir_agregar_material),
            ("Usuarios", self.mostrar_usuarios),
            ("Agregar Usuario", self.abrir_agregar_usuario),
            ("Préstamos", self.abrir_prestamo),
            ("Devoluciones", self.abrir_devolucion),
        ]

        for text, cmd in botones_info:
            b = tk.Button(self.left_frame, text=text, command=cmd, **self.estilo_boton)
            b.pack(pady=8)
            self._añadir_hover(b)

        # Botón Guardar y Salir (más visible)
        b_salir = tk.Button(self.left_frame, text="Guardar y Salir", bg="#ff6666", fg="white",
                            width=18, height=2, font=("Segoe UI", 11, "bold"), command=self.guardar_y_salir)
        b_salir.pack(pady=18)

        # Logo ANEP (al pie)
        self.logo_anep = None
        try:
            imagen_anep = Image.open(r"resources/images/Logo_ANEP.png").resize((120, 60))
            self.logo_anep = ImageTk.PhotoImage(imagen_anep)
            tk.Label(self.left_frame, image=self.logo_anep, bg=self.COLOR_PRINCIPAL).pack(side="bottom", pady=20)
        except Exception:
            tk.Label(self.left_frame, text="[ANEP]", bg=self.COLOR_PRINCIPAL, fg=self.COLOR_TEXTO,
                     font=("Segoe UI", 10, "bold")).pack(side="bottom", pady=20)

        # --- Área principal (dinámica) ---
        self.main_frame = tk.Frame(self.ventana, bg=self.COLOR_FONDO)
        self.main_frame.pack(side="right", fill="both", expand=True)

        # Muestra inicial: catálogo
        self.mostrar_catalogo()

    # ---------------- utilidades ----------------
    def _añadir_hover(self, boton):
        """Agrega efecto hover sutil a un botón"""
        def on_enter(e):
            try:
                boton.configure(bg=self.COLOR_BOTON_HOVER)
            except Exception:
                pass
        def on_leave(e):
            try:
                boton.configure(bg=self.COLOR_BOTONES)
            except Exception:
                pass
        boton.bind("<Enter>", on_enter)
        boton.bind("<Leave>", on_leave)

    def limpiar_main(self):
        for widget in self.main_frame.winfo_children():
            widget.destroy()

    # ---------------- funciones de UI / lógica ----------------
    def mostrar_catalogo(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="Catálogo de Materiales",
                 font=("Segoe UI", 16, "bold"), bg=self.COLOR_FONDO).pack(pady=12)

        texto = tk.Text(self.main_frame, font=("Segoe UI", 12), height=25, width=90)
        texto.pack(pady=10, padx=10)
        materiales = self.sistema.listar_materiales()
        if not materiales:
            texto.insert(tk.END, "No hay materiales registrados.")
        else:
            for mat in materiales:
                texto.insert(tk.END, f"{mat}\n")
        texto.config(state="disabled")

    def mostrar_socios(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="Registro de Socios",
                 font=("Segoe UI", 16, "bold"), bg=self.COLOR_FONDO).pack(pady=12)
        # Si dispones de una función mostrar_registro que dibuja en un frame, la usamos
        if mostrar_registro:
            try:
                mostrar_registro(self.main_frame)
            except Exception as e:
                tk.Label(self.main_frame, text=f"Error al mostrar registro: {e}", bg=self.COLOR_FONDO, fg="red").pack()
        else:
            # Fallback simple: listar usuarios
            texto = tk.Text(self.main_frame, font=("Segoe UI", 12), height=20, width=80)
            texto.pack(pady=10)
            if not self.sistema.usuarios:
                texto.insert(tk.END, "No hay usuarios registrados.")
            else:
                for usuario in self.sistema.usuarios.values():
                    texto.insert(tk.END, f"{usuario}\n")
            texto.config(state="disabled")

    def abrir_agregar_material(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Material")
        ventana.geometry("420x520")
        ventana.configure(bg=self.COLOR_FONDO)

        tk.Label(ventana, text="Tipo de Material:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        tipo_var = tk.StringVar(value="Libro")
        tk.Radiobutton(ventana, text="Libro", variable=tipo_var, value="Libro", bg=self.COLOR_FONDO).pack()
        tk.Radiobutton(ventana, text="Recurso", variable=tipo_var, value="Recurso", bg=self.COLOR_FONDO).pack()

        # entradas
        campos = {}
        for texto in ["Referencia", "ISBN (solo libros)", "Título", "Autor (solo libros)", "Año (solo libros)", "Ejemplares"]:
            tk.Label(ventana, text=texto + ":", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=4)
            e = tk.Entry(ventana, font=("Segoe UI", 12))
            e.pack()
            campos[texto] = e

        def agregar():
            try:
                ref = campos["Referencia"].get().strip()
                tipo = tipo_var.get()
                titulo = campos["Título"].get().strip()
                ejemplares = int(campos["Ejemplares"].get() or "0")
                if not ref or not titulo or ejemplares < 1:
                    raise ValueError("Referencia, título y ejemplares son obligatorios.")

                if tipo == "Libro":
                    isbn = campos["ISBN (solo libros)"].get().strip()
                    autor = campos["Autor (solo libros)"].get().strip()
                    ano_val = int(campos["Año (solo libros)"].get() or "0")
                    if not isbn or not autor or ano_val < 1500:
                        raise ValueError("ISBN, autor y año válidos son obligatorios para libros.")
                    material = Libro(ref, "Libro", isbn, titulo, autor, ano_val, ejemplares, ejemplares)
                else:
                    material = Recursos(ref, titulo, ejemplares, ejemplares)

                self.sistema.agregar_material(material)
                messagebox.showinfo("Éxito", f"Material '{titulo}' agregado.")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Agregar", width=16, height=2, font=("Segoe UI", 12),
                  bg="#C6E1C6", command=agregar).pack(pady=18)

    def abrir_agregar_usuario(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Agregar Usuario")
        ventana.geometry("420x360")
        ventana.configure(bg=self.COLOR_FONDO)

        tk.Label(ventana, text="Tipo de Usuario:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        tipo_var = tk.StringVar(value="Estudiante")
        tk.Radiobutton(ventana, text="Estudiante", variable=tipo_var, value="Estudiante", bg=self.COLOR_FONDO).pack()
        tk.Radiobutton(ventana, text="Profesor", variable=tipo_var, value="Profesor", bg=self.COLOR_FONDO).pack()

        tk.Label(ventana, text="ID:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Segoe UI", 12)); id_entry.pack()

        tk.Label(ventana, text="Nombre:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        nombre_entry = tk.Entry(ventana, font=("Segoe UI", 12)); nombre_entry.pack()

        tk.Label(ventana, text="Domicilio:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        domicilio_entry = tk.Entry(ventana, font=("Segoe UI", 12)); domicilio_entry.pack()

        def agregar():
            try:
                id_usuario = id_entry.get().strip()
                nombre = nombre_entry.get().strip()
                domicilio = domicilio_entry.get().strip()
                if not id_usuario or not nombre or not domicilio:
                    raise ValueError("ID, nombre y domicilio son obligatorios.")
                if id_usuario in self.sistema.usuarios:
                    raise ValueError("El ID ya está registrado.")

                usuario = Estudiante(id_usuario, nombre, domicilio) if tipo_var.get() == "Estudiante" else Profesor(id_usuario, nombre, domicilio)
                self.sistema.agregar_usuario(usuario)
                messagebox.showinfo("Éxito", f"Usuario '{nombre}' agregado.")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Agregar", width=16, height=2, font=("Segoe UI", 12),
                  bg="#C6E1C6", command=agregar).pack(pady=12)

    def abrir_prestamo(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Realizar Préstamo")
        ventana.geometry("420x220")
        ventana.configure(bg=self.COLOR_FONDO)

        tk.Label(ventana, text="ID del Usuario:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Segoe UI", 12)); id_entry.pack()

        tk.Label(ventana, text="Título del Material:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        titulo_entry = tk.Entry(ventana, font=("Segoe UI", 12)); titulo_entry.pack()

        def prestar():
            try:
                id_usuario = id_entry.get().strip()
                titulo = titulo_entry.get().strip()
                if not id_usuario or not titulo:
                    raise ValueError("ID y título son obligatorios.")
                exito, msg = self.sistema.realizar_prestamo(id_usuario, titulo)
                if exito:
                    messagebox.showinfo("Éxito", msg)
                else:
                    messagebox.showerror("Error", msg)
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Prestar", width=14, height=2, font=("Segoe UI", 12),
                  bg="#C1D4FF", command=prestar).pack(pady=14)

    def abrir_devolucion(self):
        ventana = tk.Toplevel(self.ventana)
        ventana.title("Realizar Devolución")
        ventana.geometry("420x220")
        ventana.configure(bg=self.COLOR_FONDO)

        tk.Label(ventana, text="ID del Usuario:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Segoe UI", 12)); id_entry.pack()

        tk.Label(ventana, text="Título del Material:", font=("Segoe UI", 12), bg=self.COLOR_FONDO).pack(pady=5)
        titulo_entry = tk.Entry(ventana, font=("Segoe UI", 12)); titulo_entry.pack()

        def devolver():
            try:
                id_usuario = id_entry.get().strip()
                titulo = titulo_entry.get().strip()
                if not id_usuario or not titulo:
                    raise ValueError("ID y título son obligatorios.")
                exito, msg = self.sistema.realizar_devolucion(id_usuario, titulo)
                if exito:
                    messagebox.showinfo("Éxito", msg)
                else:
                    messagebox.showerror("Error", msg)
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error: {e}")

        tk.Button(ventana, text="Devolver", width=14, height=2, font=("Segoe UI", 12),
                  bg="#C1D4FF", command=devolver).pack(pady=14)

    def mostrar_usuarios(self):
        self.limpiar_main()
        tk.Label(self.main_frame, text="Usuarios Registrados", font=("Segoe UI", 16, "bold"), bg=self.COLOR_FONDO).pack(pady=12)
        texto = tk.Text(self.main_frame, font=("Segoe UI", 12), height=25, width=90)
        texto.pack(pady=10, padx=10)
        if not self.sistema.usuarios:
            texto.insert(tk.END, "No hay usuarios registrados.")
        else:
            for usuario in self.sistema.usuarios.values():
                texto.insert(tk.END, f"{usuario}\n")
        texto.config(state="disabled")

    def guardar_y_salir(self):
        try:
            guardar_materiales(self.sistema)
            guardar_usuarios(self.sistema)
            messagebox.showinfo("Éxito", "Datos guardados. ¡Hasta luego!")
            self.ventana.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar datos: {str(e)}")


if __name__ == "__main__":
    root = tk.Tk()
    app = BibliotecaApp(root)
    root.mainloop()
