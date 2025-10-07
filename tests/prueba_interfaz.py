import os
import sys
# Calcula la ruta del directorio raíz del proyecto dinámicamente
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import tkinter as tk
from tkinter import messagebox
from objetos.biblioteca import SistemaBiblioteca
from objetos.elemento import Libro, Recursos
from objetos.usuario import Estudiante, Profesor
from objetos.utilidades import guardar_materiales, cargar_materiales, guardar_usuarios, cargar_usuarios

class TestGUI:
    def __init__(self, root):
        self.sistema = SistemaBiblioteca()
        cargar_materiales(self.sistema)
        cargar_usuarios(self.sistema)
        self.root = root
        self.root.title("Sistema Biblioteca CeRP")
        self.root.geometry("600x400")
        self.root.configure(bg="#f0f0f0")

        # Título
        tk.Label(root, text="Biblioteca CeRP del Litoral", font=("Arial", 20, "bold"), bg="#f0f0f0").pack(pady=20)

        # Marco para botones
        self.frame = tk.Frame(root, bg="#f0f0f0")
        self.frame.pack(pady=10)

        # Botones principales
        tk.Button(self.frame, text="Ver Catálogo", width=20, height=2, font=("Arial", 12), command=self.mostrar_catalogo).pack(pady=10)
        tk.Button(self.frame, text="Admin", width=20, height=2, font=("Arial", 12), bg="#ffcc00", command=self.abrir_admin).pack(pady=10)

    def abrir_admin(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Panel de Administración")
        ventana.geometry("600x400")
        ventana.configure(bg="#f0f0f0")

        tk.Label(ventana, text="Panel de Administración", font=("Arial", 16, "bold"), bg="#f0f0f0").pack(pady=20)

        frame = tk.Frame(ventana, bg="#f0f0f0")
        frame.pack(pady=10)

        tk.Button(frame, text="Agregar Material", width=20, height=2, font=("Arial", 12), command=self.abrir_agregar_material).pack(pady=5)
        tk.Button(frame, text="Agregar Usuario", width=20, height=2, font=("Arial", 12), command=self.abrir_agregar_usuario).pack(pady=5)
        tk.Button(frame, text="Realizar Préstamo", width=20, height=2, font=("Arial", 12), command=self.abrir_prestamo).pack(pady=5)
        tk.Button(frame, text="Realizar Devolución", width=20, height=2, font=("Arial", 12), command=self.abrir_devolucion).pack(pady=5)
        tk.Button(frame, text="Mostrar Usuarios", width=20, height=2, font=("Arial", 12), command=self.mostrar_usuarios).pack(pady=5)
        tk.Button(frame, text="Guardar y Salir", width=20, height=2, font=("Arial", 12), bg="#ff6666", command=self.guardar_y_salir).pack(pady=5)

    def abrir_agregar_material(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Material")
        ventana.geometry("400x400")
        ventana.configure(bg="#f0f0f0")

        tk.Label(ventana, text="Tipo de Material:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tipo_var = tk.StringVar(value="Libro")
        tk.Radiobutton(ventana, text="Libro", variable=tipo_var, value="Libro", bg="#f0f0f0").pack()
        tk.Radiobutton(ventana, text="Recurso", variable=tipo_var, value="Recurso", bg="#f0f0f0").pack()

        tk.Label(ventana, text="Referencia:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        ref_entry = tk.Entry(ventana, font=("Arial", 12))
        ref_entry.pack()

        tk.Label(ventana, text="ISBN (solo para libros):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        isbn_entry = tk.Entry(ventana, font=("Arial", 12))
        isbn_entry.pack()

        tk.Label(ventana, text="Título:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        titulo_entry = tk.Entry(ventana, font=("Arial", 12))
        titulo_entry.pack()

        tk.Label(ventana, text="Autor (solo para libros):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        autor_entry = tk.Entry(ventana, font=("Arial", 12))
        autor_entry.pack()

        tk.Label(ventana, text="Año Publicación (solo para libros):", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        ano_entry = tk.Entry(ventana, font=("Arial", 12))
        ano_entry.pack()

        tk.Label(ventana, text="Ejemplares:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        ejemplares_entry = tk.Entry(ventana, font=("Arial", 12))
        ejemplares_entry.pack()

        def agregar():
            try:
                ref = ref_entry.get().strip()
                tipo = tipo_var.get()
                titulo = titulo_entry.get().strip()
                ejemplares = int(ejemplares_entry.get())
                if not ref or not titulo or ejemplares < 1:
                    raise ValueError("Referencia, título y ejemplares son obligatorios.")

                if tipo == "Libro":
                    isbn = isbn_entry.get().strip()
                    autor = autor_entry.get().strip()
                    ano = int(ano_entry.get())
                    if not isbn or not autor or ano < 1500:
                        raise ValueError("ISBN, autor y año son obligatorios para libros.")
                    material = Libro(ref, "Libro", isbn, titulo, autor, ano, ejemplares, ejemplares)
                else:
                    material = Recursos(ref, titulo, ejemplares, ejemplares)

                self.sistema.agregar_material(material)
                messagebox.showinfo("Éxito", f"Material '{titulo}' agregado.")
                ventana.destroy()
            except ValueError as e:
                messagebox.showerror("Error", str(e))

        tk.Button(ventana, text="Agregar", width=15, height=2, font=("Arial", 12), command=agregar).pack(pady=20)

    def abrir_agregar_usuario(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Agregar Usuario")
        ventana.geometry("400x300")
        ventana.configure(bg="#f0f0f0")

        tk.Label(ventana, text="Tipo de Usuario:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        tipo_var = tk.StringVar(value="Estudiante")
        tk.Radiobutton(ventana, text="Estudiante", variable=tipo_var, value="Estudiante", bg="#f0f0f0").pack()
        tk.Radiobutton(ventana, text="Profesor", variable=tipo_var, value="Profesor", bg="#f0f0f0").pack()

        tk.Label(ventana, text="ID:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Arial", 12))
        id_entry.pack()

        tk.Label(ventana, text="Nombre:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        nombre_entry = tk.Entry(ventana, font=("Arial", 12))
        nombre_entry.pack()

        tk.Label(ventana, text="Domicilio:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        domicilio_entry = tk.Entry(ventana, font=("Arial", 12))
        domicilio_entry.pack()

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

        tk.Button(ventana, text="Agregar", width=15, height=2, font=("Arial", 12), command=agregar).pack(pady=20)

    def abrir_prestamo(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Realizar Préstamo")
        ventana.geometry("400x200")
        ventana.configure(bg="#f0f0f0")

        tk.Label(ventana, text="ID del Usuario:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Arial", 12))
        id_entry.pack()

        tk.Label(ventana, text="Título del Material:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        titulo_entry = tk.Entry(ventana, font=("Arial", 12))
        titulo_entry.pack()

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

        tk.Button(ventana, text="Prestar", width=15, height=2, font=("Arial", 12), command=prestar).pack(pady=20)

    def abrir_devolucion(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Realizar Devolución")
        ventana.geometry("400x200")
        ventana.configure(bg="#f0f0f0")

        tk.Label(ventana, text="ID del Usuario:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        id_entry = tk.Entry(ventana, font=("Arial", 12))
        id_entry.pack()

        tk.Label(ventana, text="Título del Material:", font=("Arial", 12), bg="#f0f0f0").pack(pady=5)
        titulo_entry = tk.Entry(ventana, font=("Arial", 12))
        titulo_entry.pack()

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

        tk.Button(ventana, text="Devolver", width=15, height=2, font=("Arial", 12), command=devolver).pack(pady=20)

    def mostrar_catalogo(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Catálogo de Materiales")
        ventana.geometry("600x400")
        ventana.configure(bg="#f0f0f0")

        texto = tk.Text(ventana, font=("Arial", 12), height=15, width=60)
        texto.pack(pady=10)
        materiales = self.sistema.listar_materiales()
        if not materiales:
            texto.insert(tk.END, "No hay materiales registrados.")
        else:
            for mat in materiales:
                texto.insert(tk.END, f"{mat}\n")
        texto.config(state="disabled")

    def mostrar_usuarios(self):
        ventana = tk.Toplevel(self.root)
        ventana.title("Usuarios Registrados")
        ventana.geometry("600x400")
        ventana.configure(bg="#f0f0f0")

        texto = tk.Text(ventana, font=("Arial", 12), height=15, width=60)
        texto.pack(pady=10)
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
            self.root.destroy()
        except Exception as e:
            messagebox.showerror("Error", f"Error al guardar datos: {str(e)}")

if __name__ == "__main__":
    root = tk.Tk()
    app = TestGUI(root)
    root.mainloop()