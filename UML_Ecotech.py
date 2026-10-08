import sqlite3
from datetime import date
from typing import List, Optional

# ==========================================
# 1. INTEGRACIÓN CON BASE DE DATOS (Criterios 2.1.3.G.5 y 2.1.3.G.6)
# ==========================================

class ConexionBD:
    """Clase gestora de la conexión a la base de datos usando la librería oficial sqlite3."""
    
    def __init__(self, db_name: str = "ecotech_solutions.db"):
        self._db_name: str = db_name

    def obtener_conexion(self) -> sqlite3.Connection:
        """Crea y retorna un objeto de conexión."""
        return sqlite3.connect(self._db_name)

    def probar_conexion(self) -> bool:
        """Realiza una prueba de conexión exitosa a la base de datos."""
        try:
            conn = self.obtener_conexion()
            cursor = conn.cursor()
            cursor.execute("SELECT 1;")
            conn.close()
            print("✓ Conexión exitosa a la base de datos.")
            return True
        except sqlite3.Error as e:
            print(f"✗ Error al conectar a la base de datos: {e}")
            return False


# ==========================================
# 2. MÓDULO ORGANIZACIONAL Y OPERATIVO (Criterios 2.1.1.G.1 y 2.1.2.G.3)
# ==========================================

class RegistroTiempo:
    def __init__(self, id_registro: int, fecha: date, horas_trabajadas: float, descripcion_tareas: str):
        self._id_registro: int = id_registro
        self._fecha: date = fecha
        self._horas_trabajadas: float = horas_trabajadas
        self._descripcion_tareas: str = descripcion_tareas

    @property
    def id_registro(self) -> int:
        return self._id_registro

    @property
    def horas_trabajadas(self) -> float:
        return self._horas_trabajadas

    def vincular_horas(self) -> None:
        """Vincular o procesar horas registradas."""
        print(f"Horas ({self._horas_trabajadas} hrs) vinculadas al registro N°{self._id_registro}.")


class Empleado:
    def __init__(
        self, 
        id_empleado: int, 
        nombre: str, 
        direccion: str, 
        telefono: str, 
        email: str, 
        fecha_inicio: date, 
        salario: float, 
        password_hash: str
    ):
        self._id_empleado: int = id_empleado
        self._nombre: str = nombre
        self._direccion: str = direccion
        self._telefono: str = telefono
        self._email: str = email
        self._fecha_inicio: date = fecha_inicio
        self._salario: float = salario
        self._password_hash: str = password_hash
        # Relación: Empleado registra 0..* RegistroTiempo
        self._registros_tiempo: List[RegistroTiempo] = []

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def password_hash(self) -> str:
        return self._password_hash

    def registrar_horas(self, registro: RegistroTiempo) -> None:
        """Asocia un registro de tiempo al empleado."""
        self._registros_tiempo.append(registro)
        print(f"Registro N°{registro.id_registro} asignado a {self._nombre}.")

    def mantener_datos_actualizados(self, nueva_direccion: Optional[str] = None, nuevo_telefono: Optional[str] = None) -> None:
        """Actualiza la información del empleado."""
        if nueva_direccion:
            self._direccion = nueva_direccion
        if nuevo_telefono:
            self._telefono = nuevo_telefono
        print(f"Datos del empleado {self._nombre} actualizados correctamente.")


class Proyecto:
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: date):
        self._id_proyecto: int = id_proyecto
        self._nombre: str = nombre
        self._descripcion: str = descripcion
        self._fecha_inicio: date = fecha_inicio
        # Relación: Proyecto asociado a 0..* RegistroTiempo
        self._registros_tiempo: List[RegistroTiempo] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    def gestionar_asignaciones_personal(self, registro: RegistroTiempo) -> None:
        """Asocia registros de tiempo de empleados al proyecto."""
        self._registros_tiempo.append(registro)
        print(f"Registro N°{registro.id_registro} asociado al proyecto '{self._nombre}'.")


class Departamento:
    def __init__(self, id_departamento: int, nombre: str, gerente: Optional[Empleado] = None):
        self._id_departamento: int = id_departamento
        self._nombre: str = nombre
        self._gerente: Optional[Empleado] = gerente
        # Relación: Departamento agrupa 0..* Empleado
        self._empleados: List[Empleado] = []

    def administrar_coleccion_empleados(self, empleado: Empleado) -> None:
        """Añade empleados al departamento."""
        self._empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al departamento {self._nombre}.")


# ==========================================
# 3. MÓDULO DE SEGURIDAD (Criterios 2.1.1.G.1 y 2.1.1.G.2)
# ==========================================

class GestorAutenticacion:
    def validar_password(self, empleado: Empleado, password_plano: str) -> bool:
        """Valida el acceso del empleado comparando la credencial."""
        es_valido = empleado.password_hash == password_plano
        estado = "exitoso" if es_valido else "fallido"
        print(f"Intento de autenticación para {empleado.nombre}: {estado}.")
        return es_valido


# ==========================================
# 4. MÓDULO DE SERVICIOS (Criterios 2.1.1.G.1 y 2.1.2.G.4)
# ==========================================

class GeneradorReportes:
    def exportar_pdf(self, proyecto: Proyecto) -> str:
        """Genera un reporte PDF del proyecto indicado."""
        nombre_archivo = f"reporte_{proyecto.nombre.lower().replace(' ', '_')}.pdf"
        print(f"Generando reporte PDF: {nombre_archivo}")
        return nombre_archivo

    def exportar_excel(self, proyecto: Proyecto) -> str:
        """Genera un reporte Excel del proyecto indicado."""
        nombre_archivo = f"reporte_{proyecto.nombre.lower().replace(' ', '_')}.xlsx"
        print(f"Generando reporte Excel: {nombre_archivo}")
        return nombre_archivo


# ==========================================
# 5. PRUEBA DE EJECUCIÓN (Verificación de la Pauta)
# ==========================================

if __name__ == "__main__":
    print("=== PRUEBA DE CONEXIÓN A BASE DE DATOS ===")
    db = ConexionBD()
    db.probar_conexion()

    print("\n=== INSTANCIACIÓN Y PRUEBA DEL MODELO ===")
    # Instanciación de entidades
    emp1 = Empleado(1, "Carlos Pérez", "Av. Central 123", "+56911112222", "carlos@ecotech.cl", date(2023, 1, 15), 1200000.0, "hash_pass_123")
    depto = Departamento(101, "Desarrollo de Software", gerente=emp1)
    depto.administrar_coleccion_empleados(emp1)

    proy = Proyecto(501, "Optimización EcoTech", "Sistema POO en Python", date(2024, 3, 1))
    reg = RegistroTiempo(1001, date.today(), 8.5, "Desarrollo del esqueleto POO")

    # Prueba de relaciones
    emp1.registrar_horas(reg)
    proy.gestionar_asignaciones_personal(reg)

    # Prueba de seguridad y servicios
    auth = GestorAutenticacion()
    auth.validar_password(emp1, "hash_pass_123")

    reportes = GeneradorReportes()
    reportes.exportar_pdf(proy)