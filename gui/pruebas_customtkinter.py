# interfas.py
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

# Colores
color_naranja = "#FF6200"
color_azul = "#0057B8"
color_fondo = "#F0F4F8"
color_texto = "#333333"

# Ventana principal
ventana = ctk.CTk()
ventana.title("Biblioteca Cerp del Litoral")
ventana.geometry("900x600")
ventana.resizable(False, False)

# Panel lateral
panel_lateral = ctk.CTkFrame(ventana, fg_color=color_azul, width=200)
panel_lateral.pack(side="left", fill="y")

# Marco principal
marco_principal = ctk.CTkFrame(ventana, fg_color=color_fondo)
marco_principal.pack(side="right", fill="both", expand=True, padx=20, pady=20)

# Carga logo
try:
    logo_img = Image.open("resources/crep.jpg")
    logo_ctk = ctk.CTkImage(light_image=logo_img, size=(50, 50))
    logo_label = ctk.CTkLabel(panel_lateral, image=logo_ctk, text="")
    logo_label.pack(side="bottom", pady=10)
except Exception as e:
    print(f"Error al cargar el logo: {e}")
    logo_label = ctk.CTkLabel(panel_lateral, text="Logo no disponible", text_color="white")
    logo_label.pack(side="bottom", pady=10)

# Función para limpiar el marco
def limpiar_marco():
    for widget in marco_principal.winfo_children():
        widget.destroy()

# Sección Inicio
def mostrar_inicio():
    limpiar_marco()
    etiqueta_titulo = ctk.CTkLabel(marco_principal, text="Biblioteca Cerp del Litoral", font=("Helvetica", 20, "bold"))
    etiqueta_titulo.pack(pady=20)
    try:
        imagen_inicio = Image.open("resources/crep.jpg")
        imagen_ctk = ctk.CTkImage(light_image=imagen_inicio, size=(200, 200))
        etiqueta_imagen = ctk.CTkLabel(marco_principal, image=imagen_ctk, text="")
        etiqueta_imagen.pack(pady=20)
    except Exception as e:
        print(f"Error al cargar la imagen de inicio: {e}")
        etiqueta_error = ctk.CTkLabel(marco_principal, text="Imagen no disponible")
        etiqueta_error.pack(pady=20)

# Sección Socios
def mostrar_socios():
    limpiar_marco()
    etiqueta = ctk.CTkLabel(marco_principal, text="Gestión de Socios", font=("Helvetica", 16, "bold"))
    etiqueta.pack(pady=10)
    etiqueta_nombre = ctk.CTkLabel(marco_principal, text="Nombre del Socio:")
    etiqueta_nombre.pack(pady=5)
    entrada_nombre = ctk.CTkEntry(marco_principal, width=200, placeholder_text="Ingresa nombre")
    entrada_nombre.pack(pady=5)
    def saludar():
        nombre = entrada_nombre.get()
        resultado.configure(text=f"¡Hola, {nombre}!" if nombre else "Por favor, ingrese un nombre.")
    boton_saludar = ctk.CTkButton(marco_principal, text="Saludar", command=saludar, fg_color=color_naranja)
    boton_saludar.pack(pady=10)
    resultado = ctk.CTkLabel(marco_principal, text="")
    resultado.pack(pady=10)

# Sección Libros
def mostrar_libros():
    limpiar_marco()
    etiqueta = ctk.CTkLabel(marco_principal, text="Gestión de Libros", font=("Helvetica", 16, "bold"))
    etiqueta.pack(pady=10)
    etiqueta_material = ctk.CTkLabel(marco_principal, text="Material:")
    etiqueta_material.pack(pady=5)
    entrada_material = ctk.CTkEntry(marco_principal, width=200, placeholder_text="Ingresa material")
    entrada_material.pack(pady=5)
    def buscar():
        material = entrada_material.get()
        resultado.configure(text=f"El {material} se encuentra disponible." if material else "Por favor, ingrese un material.")
    boton_buscar = ctk.CTkButton(marco_principal, text="Buscar", command=buscar, fg_color=color_naranja)
    boton_buscar.pack(pady=10)
    resultado = ctk.CTkLabel(marco_principal, text="")
    resultado.pack(pady=10)

# Sección Admin
def mostrar_admin():
    limpiar_marco()
    etiqueta = ctk.CTkLabel(marco_principal, text="Panel de Administración", font=("Helvetica", 16, "bold"))
    etiqueta.pack(pady=10)
    ctk.CTkLabel(marco_principal, text="Aquí puedes gestionar configuraciones avanzadas.").pack(pady=10)

# Botones del panel lateral
boton_inicio = ctk.CTkButton(panel_lateral, text="Inicio", command=mostrar_inicio, width=180, fg_color=color_naranja)
boton_inicio.pack(pady=10, padx=10)
boton_socios = ctk.CTkButton(panel_lateral, text="Socios", command=mostrar_socios, width=180, fg_color=color_naranja)
boton_socios.pack(pady=10, padx=10)
boton_libros = ctk.CTkButton(panel_lateral, text="Libros", command=mostrar_libros, width=180, fg_color=color_naranja)
boton_libros.pack(pady=10, padx=10)
boton_admin = ctk.CTkButton(panel_lateral, text="Admin", command=mostrar_admin, width=180, fg_color=color_naranja)
boton_admin.pack(pady=10, padx=10)

# Mostrar Inicio por defecto
mostrar_inicio()

ventana.mainloop()