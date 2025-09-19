# objetos/usuario.py
class Administrador:  
# desarrollar luego (no usado por ahora) se supone que  
# solo esta clase puede agregar o eliminar usuarios
    def __init__(self, id, nombre, ):
        self.__id = id
        self.__nombre = nombre

class Usuario: # clase base
    def __init__(self, id, nombre, domicilio, material_prestado , estado):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  #lista para rastrear materiales prestados
        self.__estado = "activo" # puede ser activo o suspendido

# setters usuario modificar datos

    def set_nombre(self, nombre):
        self.__nombre = nombre
    
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio
        
# getters usuario
    def get_id_socio(self):
        return self.__id 
    
    def get_nombre(self):
        return self.__nombre
 
    def get_domicilio(self, domicilio):
        self.__domicilio = domicilio

    def get_material_prestado(self, material_prestado):
        self.__material_prestado = material_prestado

    def get_estado(self, estado):
        self.__estado = estado        
# setters
    def set_nombre(self, nombre):
        self.__nombre = nombre
    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio

# prestamos del usuario
    def prestar_material(self, material):
    




#biblioteca_sistema 

# Estructura del proyecto:
#├── objetos/                # Carpeta para las clases principales
#│   ├────── elemento.py          # Clase base para materiales # Libro, Cables, DVD etc
#│   ├────── utilidades.py     # Funciones auxiliares validaciones, etc.
#│   ├────── usuario.py         # Clases de usuarios #  Usuario(Clase base),Estudiante, Profesor 
#│   ├────── biblioteca.py    # Clase principal del sistema # Gestión de materiales y usuarios
#├── app.py                      # Archivo principal para ejecutar la aplicación
#├── resources/              # Carpeta para recursos estáticos # Imágenes, íconos, etc.
#│   ├────── data/                 # Carpeta para almacenar archivos de datos
#│   ├────── images/               # Carpeta para imágenes e iconos
#├── gui/                    # Carpeta para la interfaz gráfica # Tkinter  Parte Martin 
#├── notas                 # Carpeta para notas y documentación 
#│   ├── diagramas/              # Carpeta para diagramas UML y otros
#│   ├── notas.txt              # Notas del proyecto
#├── tests/                  # Carpeta para pruebas unitarias
#│   ├── test_biblioteca.py      # Pruebas para la clase
#└── README.TXT               # Documentación del proyecto
#└── requirements.txt        # Dependencias del proyecto
