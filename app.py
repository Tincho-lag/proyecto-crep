# app.py
from models.elemento import Libro

libro1 = Libro("978-0743273565", "El Gran Gatsby", "F. Scott Fitzgerald", 1925, 3)
libro2 = Libro("978-0451524935", "1984", "George Orwell", 1949, 2)
libro3 = Libro("978-0061120084", "Matar un ruiseñor", "Harper Lee", 1960, 1)

print("=== PRUEBA DE LA CLASE  Libro ===")
print(f"Libro creado: {libro1}")
print(f"Libro creado: {libro2}")

    # Probar préstamo
print(f"¿Se puede prestar? {libro1.prestar()}")
print(f"Después del préstamo: {libro1}")
    
    # Prestar todos los ejemplares
libro1.prestar()
print(f"Después de prestar todo: {libro1}")

    # Intentar prestar cuando no hay disponibles
print(f"¿Se puede prestar más? {libro1.prestar()}")
    
    # Devolver uno
libro1.devolver()
print(f"Después de devolver uno: {libro1}")
   
# Probar getters
print(f"Título: {libro1.get_titulo()}")
print(f"Autor: {libro1.get_autor()}")
print(f"ISBN: {libro1.get_isbn()}")