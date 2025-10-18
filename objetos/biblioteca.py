from .nodo_arbol import ArbolBinario
from objetos.elemento import Libro, Recursos
# clase prestamo 
from datetime import datetime, timedelta
from objetos.utilidades import Cola

class Prestamo:
    def __init__(self, id_prestamo, usuario, material, dias_prestamo):
        self.__id_prestamo = id_prestamo
        self.__usuario = usuario
        self.__material = material
        self.__dias_prestamo = dias_prestamo
        self.__activo = True
        
        self.__fecha_prestamo = datetime.now()
        self.__fecha_vencimiento = self.__fecha_prestamo + timedelta(days=dias_prestamo)
        self.__fecha_devolucion = None

    def get_id_prestamo(self):
        return self.__id_prestamo
    
    def get_usuario(self):
        return self.__usuario 
    
    def get_material(self):
        return self.__material 
    
    def get_dias_prestamo(self):
        return self.__dias_prestamo
    
    def get_fecha_prestamo(self):
        return self.__fecha_prestamo
    
    def get_fecha_vencimiento(self):
        return self.__fecha_vencimiento
    
    def get_fecha_devolucion(self):
        return self.__fecha_devolucion 
    
    def finalizar(self):
        self.__activo = False
        self.__fecha_devolucion = datetime.now()
    
    def esta_activo(self):
        return self.__activo

# clase sistema gestor
class SistemaBiblioteca:
    def __init__(self):
        self.arbol_materiales = None
        self.usuarios = {}
        self.prestamos = []
        self.reservas = {}
        self.contador_prestamos = 1
    
    def agregar_material(self, material):
        if self.arbol_materiales is None:
            self.arbol_materiales = ArbolBinario()
        self.arbol_materiales.insertar(material)
    
    def buscar_material(self, titulo):
        if self.arbol_materiales is None:
            return None
        return self.arbol_materiales.buscar_por_titulo(titulo)
    
    def agregar_usuario(self, usuario):
        self.usuarios[usuario.get_id()] = usuario
    
    def realizar_prestamo(self, id_usuario, titulo_material):
        if id_usuario not in self.usuarios:
            return False, "error en los datos ingresados. el usuario no existe.", None
        
        usuario = self.usuarios[id_usuario]
        
        if not usuario.estado_activo():
            return False, "usuario suspendido. no puede realizar prestamos.", None
        
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "material no encontrado.", None
        
        if not material.hay_disponibles():
            return False, "material no disponible para prestamo.", None
        
        if len(usuario.get_material_prestado()) >= usuario.get_limite_prestamos():
            return False, "limite de prestamos alcanzado para este tipo de usuario.", None
        
        if material.prestar():
            usuario.prestar_material(material.get_titulo())
            
            prestamo = Prestamo(
                f"P{self.contador_prestamos:04d}",
                usuario,
                material,
                usuario.get_dias_prestamo()
            )
            self.prestamos.append(prestamo)
            self.contador_prestamos += 1
            return True, "prestamo exitoso.", prestamo
        
        return False, "error al prestar el material.", None
    
    def realizar_devolucion(self, id_usuario, titulo_material):
        usuario = self.usuarios.get(id_usuario)
        if usuario is None:
            return False, "usuario no encontrado."
        
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "material no encontrado."
        
        titulo_identificador = material.get_titulo()
        
        for prestamo in self.prestamos:
            if (prestamo.esta_activo() and 
                prestamo.get_usuario().get_id() == id_usuario and
                prestamo.get_material().get_titulo() == titulo_material):
                
                material.devolver()
                usuario.devolver_material(titulo_identificador)
                prestamo.finalizar()
                
                fecha_dev = prestamo.get_fecha_devolucion()
                fecha_ven = prestamo.get_fecha_vencimiento()
                dias_retraso = (fecha_dev - fecha_ven).days
                
                if dias_retraso > 0:
                    dias_suspension = min(30, dias_retraso * 2)
                    usuario.suspender(dias_suspension)
                    return True, f"devolucion exitosa. hubo un retraso de {dias_retraso} dias. el usuario sera suspendido por {dias_suspension} dias. fecha de devolucion: {fecha_dev.strftime('%d/%m/%Y %H:%M')}"
                
                mensaje = "devolucion exitosa."
                
                if titulo_material in self.reservas and not self.reservas[titulo_material].estaVacia():
                    siguiente_id_usuario = self.reservas[titulo_material].desencolar()
                    exito_prestamo, msg_prestamo, nuevo_prestamo = self.realizar_prestamo(siguiente_id_usuario, titulo_material)

                    if exito_prestamo:
                        mensaje = f"devolucion exitosa. el material fue asignado automaticamente al usuario {siguiente_id_usuario} de la cola de espera."
                    else:
                        mensaje = f"devolucion exitosa, pero no se pudo asignar el material al siguiente usuario. motivo: {msg_prestamo}"
                    
                    if self.reservas[titulo_material].estaVacia():
                        del self.reservas[titulo_material]
                
                return True, f"{mensaje} fecha de devolucion: {fecha_dev.strftime('%d/%m/%Y %H:%M')}"
            
        return False, "no se encontro prestamo activo para este usuario y material."
            
    def listar_materiales(self):
        if self.arbol_materiales is None:
            return []
        return self.arbol_materiales.listar_todos()