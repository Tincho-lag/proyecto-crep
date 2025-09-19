#  tests/test_biblioteca.py 
from objetos.elemento import Libro
from objetos.usuario import Estudiante
from objetos.usuario import Profesor

libro1 = Libro("REF001", "Libro", "978-3-16-148410-0", "Introducción a Python", "Juan Pérez", 2020, 5)
print(f"Libro creado: {libro1}")
    
estudiante1 = Estudiante("2024001", "Ana García", "Tacuarembó 123")
print(f"Estudiante creado: {estudiante1}")

profe2 = Profesor("2024001", "Ana García", "Tacuarembó 123")
print(f"Estudiante creado: {profe2}")