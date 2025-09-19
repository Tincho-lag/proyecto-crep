#  tests/test_biblioteca.py
from objetos.elemento import Libro
from objetos.usuario import Usuario, Estudiante, Profesor

libro1 = Libro("REF001", "Libro", "978-3-16-148410-0", "Introducción a Python", "Juan Pérez", 2020, 5)
print(f"Libro creado: {libro1}")


