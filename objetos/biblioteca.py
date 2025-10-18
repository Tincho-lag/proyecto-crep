# objetos/biblioteca.py

from .nodo_arbol import ArbolBinario
from datetime import datetime, timedelta

class Prestamo:
    # representa un prestamo activo con fechas
    def __init__(self, id_prestamo, usuario, material, dias_prestamo):
        self.__id_prestamo = id_prestamo
        self.__usuario = usuario
        self.__material = material
        self.__dias_prestamo = dias_prestamo
        self.__activo = True
        
        # calcular fechas automaticamente
        self.__fecha_prestamo = datetime.now()
        self.__fecha_vencimiento = self.__fecha_prestamo + timedelta(days=dias_prestamo)
        self.__fecha_devolucion = None

    # getters
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
    
    def esta_activo(self):
        return self.__activo
    
    def finalizar(self):
        # marca el prestamo como finalizado y registra fecha de devolucion
        self.__activo = False
        self.__fecha_devolucion = datetime.now()


class SistemaBiblioteca:
    # clase principal que coordina toda la biblioteca
    def __init__(self):
        self.arbol_materiales = None  # arbol binario de materiales
        self.usuarios = {}            # diccionario id -> usuario
        self.prestamos = []           # lista de prestamos activos
        self.reservas = {}            # diccionario titulo -> cola de usuarios
        self.contador_prestamos = 1   # contador para generar ids unicos
    
    def agregar_material(self, material):
        # agrega un material al arbol binario
        if self.arbol_materiales is None:
            self.arbol_materiales = ArbolBinario()
        self.arbol_materiales.insertar(material)
    
    def buscar_material(self, titulo):
        # busca un material por titulo usando el arbol binario
        if self.arbol_materiales is None:
            return None
        return self.arbol_materiales.buscar_por_titulo(titulo)
    
    def agregar_usuario(self, usuario):
        # registra un nuevo usuario en el sistema 
        self.usuarios[usuario.get_id()] = usuario
    
    def realizar_prestamo(self, id_usuario, titulo_material):
        # procesa un prestamo verificando todas las condiciones
        # validar que el usuario existe
        if id_usuario not in self.usuarios:
            return False, "error: el usuario no existe.", None
        
        usuario = self.usuarios[id_usuario]
        
        # validar que el usuario no esta suspendido
        if not usuario.estado_activo():
            return False, "error: usuario suspendido.", None
        
        # buscar el material
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "error: material no encontrado.", None
        
        # validar disponibilidad
        if not material.hay_disponibles():
            return False, "error: material no disponible.", None
        
        # validar limite de prestamos del usuario
        if len(usuario.get_material_prestado()) >= usuario.get_limite_prestamos():
            return False, "error: limite de prestamos alcanzado.", None
        
        # realizar el prestamo
        if material.prestar():
            usuario.prestar_material(material.get_titulo())
            
            # crear objeto prestamo
            prestamo = Prestamo(
                f"P{self.contador_prestamos:04d}",
                usuario,
                material,
                usuario.get_dias_prestamo()
            )
            self.prestamos.append(prestamo)
            self.contador_prestamos += 1
            
            # registrar en transacciones
            self._registrar_transaccion("prestamo", usuario, material, prestamo)
            
            return True, "prestamo exitoso.", prestamo
        
        return False, "error al prestar.", None
    
    def realizar_devolucion(self, id_usuario, titulo_material):
        # procesa una devolucion y calcula sanciones si hay atraso
        usuario = self.usuarios.get(id_usuario)
        if usuario is None:
            return False, "error: usuario no encontrado."
        
        material = self.buscar_material(titulo_material)
        if material is None:
            return False, "error: material no encontrado."
        
        titulo_identificador = material.get_titulo()
        
        # buscar el prestamo activo
        for prestamo in self.prestamos:
            if (prestamo.esta_activo() and 
                prestamo.get_usuario().get_id() == id_usuario and
                prestamo.get_material().get_titulo() == titulo_material):
                
                # devolver el material
                material.devolver()
                usuario.devolver_material(titulo_identificador)
                prestamo.finalizar()
                
                # calcular si hay atraso
                fecha_dev = prestamo.get_fecha_devolucion()
                fecha_ven = prestamo.get_fecha_vencimiento()
                dias_retraso = (fecha_dev - fecha_ven).days
                
                mensaje = "devolucion exitosa."
                
                # aplicar sancion si hay atraso
                if dias_retraso > 0:
                    dias_suspension = min(30, dias_retraso * 2)  # 2 dias por cada dia de atraso, max 30
                    usuario.suspender(dias_suspension)
                    mensaje = f"devolucion con atraso de {dias_retraso} dias. suspension: {dias_suspension} dias."
                
                # procesar cola de reservas si existe
                if titulo_material in self.reservas and not self.reservas[titulo_material].estaVacia():
                    siguiente_id = self.reservas[titulo_material].desencolar()
                    exito, msg, nuevo_prestamo = self.realizar_prestamo(siguiente_id, titulo_material)
                    
                    if exito:
                        mensaje += f" material asignado a usuario {siguiente_id} de la cola."
                    
                    # eliminar cola si quedo vacia
                    if self.reservas[titulo_material].estaVacia():
                        del self.reservas[titulo_material]
                
                # registrar en transacciones
                self._registrar_transaccion("devolucion", usuario, material, prestamo, dias_retraso)
                
                return True, f"{mensaje} fecha: {fecha_dev.strftime('%d/%m/%Y %H:%M')}"
        
        return False, "error: prestamo no encontrado."
    
    def _registrar_transaccion(self, tipo, usuario, material, prestamo, dias_retraso=0):
        # registra transacciones en archivo txt
        try:
            with open("resources/data/transacciones.txt", "a") as f:
                timestamp = datetime.now().strftime('%d/%m/%Y %H:%M')
                id_prestamo = prestamo.get_id_prestamo()
                id_usuario = usuario.get_id()
                nombre_usuario = usuario.get_nombre()
                titulo_material = material.get_titulo()
                
                if tipo == "prestamo":
                    fecha_venc = prestamo.get_fecha_vencimiento().strftime('%d/%m/%Y')
                    linea = f"{timestamp} | PRESTAMO | {id_prestamo} | usuario: {nombre_usuario} ({id_usuario}) | material: {titulo_material} | vencimiento: {fecha_venc}\n"
                elif tipo == "devolucion":
                    if dias_retraso > 0:
                        linea = f"{timestamp} | DEVOLUCION (ATRASO: {dias_retraso} dias) | {id_prestamo} | usuario: {nombre_usuario} ({id_usuario}) | material: {titulo_material}\n"
                    else:
                        linea = f"{timestamp} | DEVOLUCION | {id_prestamo} | usuario: {nombre_usuario} ({id_usuario}) | material: {titulo_material}\n"
                
                f.write(linea)
        except Exception as e:
            print(f"error al registrar transaccion: {e}")
    
    def listar_materiales(self):
        # devuelve lista ordenada de todos los materiales
        if self.arbol_materiales is None:
            return []
        return self.arbol_materiales.listar_todos()