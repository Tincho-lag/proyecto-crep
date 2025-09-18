#  tests/test_biblioteca.py 
from objetos.elemento import Libro
from objetos.usuario import Usuario 
from objetos.usuario import Estudiante
from objetos.usuario import Profesor


libro1 = Libro("REF001", "978-123456", "El Principito", "Saint-Exupéry", 1943, 2)
print(f"Libro creado: {libro1}")
    
    # Crear estudiante
estudiante1 = Estudiante("2024001", "Ana García", "Tacuarembó 123", "Informática")
print(f"Estudiante creado: {estudiante1}")