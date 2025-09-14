# pruebas_costumtkinter.py
# archivo de prueba para customtkinter
# pip install customtkinter Pillow
import customtkinter as ctk
from PIL import Image

ctk.set_appearance_mode("light")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Proyecto Crep")
root.geometry("400x300")

# Carga imagen
try:
    img = Image.open("resources/crep.jpg")
    ctk_img = ctk.CTkImage(light_image=img, size=(200, 150))
    label_img = ctk.CTkLabel(root, image=ctk_img, text="")
    label_img.pack(pady=10)
except FileNotFoundError:
    print("Error: No se encontró resources/crep.jpg")
except Exception as e:
    print(f"Error: {e}")

label = ctk.CTkLabel(root, text="¡Bienvenido al Proyecto Crep!", font=("Arial", 14))
label.pack(pady=10)
entry = ctk.CTkEntry(root, placeholder_text="Ingresa tu nombre")
entry.pack(pady=10)
button = ctk.CTkButton(root, text="Enviar", command=lambda: print(f"Entrada: {entry.get()}"))
button.pack(pady=10)

root.mainloop()