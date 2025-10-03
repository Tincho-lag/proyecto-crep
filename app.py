#  app.py 
from objetos.elemento import Libro
from objetos.elemento import Recursos
from objetos.usuario import Estudiante
from objetos.usuario import Profesor

recuso1 = Recursos("REF002","Control Aire",5,1)
print(f"Nuevo {recuso1}")
libro1 = Libro("REF001", "Libro",978, "Pepe", "El Pepe", 2020, 5,2)
print(f"Nuevo {libro1}")

revista1 = Libro("REF002","Revista",979,"The Pepe","Pepe Jr",2025,4,4)
print(f"Nuevo {revista1}")
    
estudiante1 = Estudiante("2024001", "Ana García", "Tacuarembó 123")
print(f"Estudiante creado: {estudiante1}")

profe2 = Profesor("2024001", "Ana García", "Tacuarembó 123")
print(f"Estudiante creado: {profe2}")

