import pymysql
from empleado import Empleado

class EmpleadoRepositorio:
    def __init__(self, host, user, password, database):
        self.config = {
            "host": host,
            "port": 3306,
            "user": user,
            "password": password,
            "database": database
        }
        self._crear_tabla()

    def _crear_tabla(self):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS empleados (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    correo VARCHAR(100) NOT NULL,
                    telefono VARCHAR(20) NOT NULL,
                    salario DECIMAL(10,2) NOT NULL
                )
            """)
            conexion.commit()
        finally:
            conexion.close()

    # 1. CREATE
    def guardar(self, empleado: Empleado) -> Empleado:
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                INSERT INTO empleados (nombre, correo, telefono, salario)
                VALUES (%s, %s, %s, %s)
                """,
                (empleado.nombre, empleado.correo, empleado.telefono, empleado.salario)
            )
            conexion.commit()
            empleado.id_empleado = cursor.lastrowid
            return empleado
        finally:
            conexion.close()

    # 2. READ (BUSCAR)
    def buscar_por_id(self, id_empleado: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, correo, telefono, salario FROM empleados WHERE id=%s",
                (id_empleado,)
            )
            fila = cursor.fetchone()
            if fila:
                return Empleado(id_empleado=fila[0], nombre=fila[1], correo=fila[2], telefono=fila[3], salario=float(fila[4]))
            return None
        finally:
            conexion.close()

    # 3. READ ALL (LISTAR)
    def listar(self):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, correo, telefono, salario FROM empleados")
            filas = cursor.fetchall()
            return [Empleado(id_empleado=f[0], nombre=f[1], correo=f[2], telefono=f[3], salario=float(f[4])) for f in filas]
        finally:
            conexion.close()

    # 4. UPDATE
    def actualizar(self, empleado: Empleado):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                """
                UPDATE empleados
                SET nombre=%s, correo=%s, telefono=%s, salario=%s
                WHERE id=%s
                """,
                (empleado.nombre, empleado.correo, empleado.telefono, empleado.salario, empleado.id_empleado)
            )
            conexion.commit()
        finally:
            conexion.close()

    # 5. DELETE
    def eliminar(self, id_empleado: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM empleados WHERE id=%s", (id_empleado,))
            conexion.commit()
        finally:
            conexion.close()