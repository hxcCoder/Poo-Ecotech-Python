import pymysql
from datetime import date
from typing import List, Optional

# ==========================================
# 1. INTEGRACIÓN CON BASE DE DATOS (Criterios 2.1.3.G.5 y 2.1.3.G.6)
# ==========================================

class ConexionBD:
    """Clase gestora de la conexión a la base de datos MySQL usando PyMySQL."""
    
    def __init__(self, host='localhost', port=3306, user='root', password='Inacap2026', database='test'):
        self.config = {
            'host': host,
            'port': port,
            'user': user,
            'password': password,
            'database': database
        }

    def obtener_conexion(self):
        """Crea y retorna un objeto de conexión."""
        return pymysql.connect(**self.config)

    def probar_conexion(self) -> bool:
        """Realiza una prueba de conexión exitosa a la base de datos."""
        try:
            with self.obtener_conexion() as conexion:
                cursor = conexion.cursor()
                cursor.execute("SELECT 1;")
                print("✓ Conexión exitosa a la base de datos MySQL.")
                return True
        except pymysql.Error as e:
            print(f"✗ Error al conectar a la base de datos: {e}")
            return False


# ==========================================
# 2. CAPA DE ACCESO A DATOS - REPOSITORIOS (Sección 2.4 y 2.6 del Material)
# ==========================================

class EmpleadoRepositorio:
    """Clase encargada de la persistencia de la entidad Empleado en la BD."""
    
    def __init__(self, conexion_bd: ConexionBD):
        self.conexion_bd = conexion_bd

    def crear_tabla(self):
        """Crea la tabla empleados si no existe."""
        with self.conexion_bd.obtener_conexion() as conexion:
            cursor = conexion.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS empleados (
                    id INT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    correo VARCHAR(100) NOT NULL,
                    telefono VARCHAR(20) NOT NULL
                )
            ''')
            conexion.commit()

    def guardar(self, empleado) -> None:
        """Inserta un empleado usando consultas parametrizadas por seguridad."""
        try:
            with self.conexion_bd.obtener_conexion() as conexion:
                cursor = conexion.cursor()
                # Consulta parametrizada con %s
                cursor.execute('''
                    INSERT INTO empleados (id, nombre, correo, telefono)
                    VALUES (%s, %s, %s, %s)
                ''', (empleado.id_empleado, empleado.nombre, empleado.email, empleado.telefono))
                conexion.commit()
                print(f"✓ Empleado '{empleado.nombre}' guardado en la base de datos de forma persistente.")
        except pymysql.err.IntegrityError:
            print(f"⚠ El empleado con ID {empleado.id_empleado} ya existe en la base de datos.")
        except pymysql.Error as e:
            print(f"✗ Error al guardar el empleado: {e}")


# ==========================================
# 3. CAPA DE DOMINIO - ENTIDADES (Criterios 2.1.1.G.1 y 2.1.2.G.3)
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


class Empleado:
    """Clase del dominio. No contiene código de acceso a la base de datos."""
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
        self._registros_tiempo: List[RegistroTiempo] = []

    @property
    def id_empleado(self) -> int:
        return self._id_empleado

    @property
    def nombre(self) -> str:
        return self._nombre

    @property
    def email(self) -> str:
        return self._email
        
    @property
    def telefono(self) -> str:
        return self._telefono

    @property
    def password_hash(self) -> str:
        return self._password_hash

    def registrar_horas(self, registro: RegistroTiempo) -> None:
        self._registros_tiempo.append(registro)
        print(f"Registro N°{registro.id_registro} asignado a {self._nombre}.")


class Proyecto:
    def __init__(self, id_proyecto: int, nombre: str, descripcion: str, fecha_inicio: date):
        self._id_proyecto: int = id_proyecto
        self._nombre: str = nombre
        self._descripcion: str = descripcion
        self._fecha_inicio: date = fecha_inicio
        self._registros_tiempo: List[RegistroTiempo] = []

    @property
    def nombre(self) -> str:
        return self._nombre

    def gestionar_asignaciones_personal(self, registro: RegistroTiempo) -> None:
        self._registros_tiempo.append(registro)
        print(f"Registro N°{registro.id_registro} asociado al proyecto '{self._nombre}'.")


class Departamento:
    def __init__(self, id_departamento: int, nombre: str, gerente: Optional[Empleado] = None):
        self._id_departamento: int = id_departamento
        self._nombre: str = nombre
        self._gerente: Optional[Empleado] = gerente
        self._empleados: List[Empleado] = []

    def administrar_coleccion_empleados(self, empleado: Empleado) -> None:
        self._empleados.append(empleado)
        print(f"Empleado {empleado.nombre} agregado al departamento {self._nombre}.")


# ==========================================
# 4. MÓDULO DE SEGURIDAD Y SERVICIOS (Criterios 2.1.2.G.4)
# ==========================================

class GestorAutenticacion:
    def validar_password(self, empleado: Empleado, password_plano: str) -> bool:
        es_valido = empleado.password_hash == password_plano
        estado = "exitoso" if es_valido else "fallido"
        print(f"Intento de autenticación para {empleado.nombre}: {estado}.")
        return es_valido

class GeneradorReportes:
    def exportar_pdf(self, proyecto: Proyecto) -> str:
        nombre_archivo = f"reporte_{proyecto.nombre.lower().replace(' ', '_')}.pdf"
        print(f"Generando reporte PDF: {nombre_archivo}")
        return nombre_archivo


# ==========================================
# 5. PRUEBA DE EJECUCIÓN 
# ==========================================

if __name__ == "__main__":
    print("=== 1. PRUEBA DE CONEXIÓN A BASE DE DATOS ===")
    db = ConexionBD()
    if db.probar_conexion():
        
        # Preparar la base de datos (Crear tabla si no existe)
        repo_empleados = EmpleadoRepositorio(db)
        repo_empleados.crear_tabla()

        print("\n=== 2. INSTANCIACIÓN Y PRUEBA DEL MODELO ===")
        # Instanciar en memoria (Capa de Dominio)
        emp1 = Empleado(1, "Carlos Pérez", "Av. Central 123", "+56911112222", "carlos@ecotech.cl", date(2023, 1, 15), 1200000.0, "hash_pass_123")
        depto = Departamento(101, "Desarrollo de Software", gerente=emp1)
        depto.administrar_coleccion_empleados(emp1)

        proy = Proyecto(501, "Optimización EcoTech", "Sistema POO en Python", date(2024, 3, 1))
        reg = RegistroTiempo(1001, date.today(), 8.5, "Desarrollo del esqueleto POO")

        # Prueba de relaciones
        emp1.registrar_horas(reg)
        proy.gestionar_asignaciones_personal(reg)

        print("\n=== 3. PRUEBA DE PERSISTENCIA (CRUD: CREATE) ===")
        # Guardar en la base de datos (Capa de Acceso a Datos)
        repo_empleados.guardar(emp1)

        print("\n=== 4. PRUEBA DE SERVICIOS ===")