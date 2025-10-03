# objetos/usuario.py
class Administrador:  
# hacer despues (no usado por ahora) se supone que  
# solo esta clase puede agregar o eliminar usuarios 
    def __init__(self, id, nombre, ):
        self.__id = id
        self.__nombre = nombre

class Usuario: 
    def __init__(self, id, nombre, domicilio):
        self.__id = id
        self.__nombre = nombre
        self.__domicilio = domicilio
        self.__material_prestado = []  #lista para rastrear materiales prestados
        self.__estado = "activo" # puede ser activo o suspendido
        self.__fecha_fin_suspension = None

# setters usuario modificar datos
    def set_nombre(self, nombre):
        self.__nombre = nombre

    def set_domicilio(self, domicilio):
        self.__domicilio = domicilio
        
# getters usuario
    def get_id(self):
        return self.__id 
    
    def get_nombre(self):
        return self.__nombre
 
    def get_domicilio(self):
        return self.__domicilio

    def get_material_prestado(self):
        return self.__material_prestado

    def get_estado(self):
        return self.__estado  

# métodos para gestionar préstamos
    def prestar_material(self, isbn):
        self.__material_prestado.append(isbn)
    
    def devolver_material(self, isbn):
        if isbn in self.__material_prestado:
            self.__material_prestado.remove(isbn)
    
    def estado_activo(self):
        return self.__estado == "activo"
    
    def suspender(self, dias):
        self.__estado = "suspendido" 

    def reactivar(self):
        self.__estado = "activo"
        self.__fecha_fin_suspension = None

    def __str__(self):
        estado_texto = "ACTIVO" if self.estado_activo() else "SUSPENDIDO"
        return f"{self.get_nombre()} (ID: {self.get_id()}) - {estado_texto}"

class Estudiante(Usuario): # hereda de usuario puede ver libros y socilitar prestamos
    def __init__(self, id, nombre, domicilio):
        super().__init__(id, nombre, domicilio,)
        self.__tipo = "Estudiante" 

class Profesor(Usuario): # hereda de usuario puede ver libros y solicitar prestamos
    def __init__(self, id, nombre, domicilio,):
        super().__init__(id , nombre, domicilio)
        self.__tipo = "Profesor"

    


#biblioteca_sistema 

# estructura del actual proyecto
# proyecto- crep:
#├── objetos/                # Carpeta para las clases principales
#│   ├────── elemento.py          # Clase base para materiales # Libro, Cables, DVD etc
#│   ├────── utilidades.py     # Funciones auxiliares validaciones, etc.
#│   ├────── usuario.py         # Clases de usuarios Estudiante Profesor 
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

