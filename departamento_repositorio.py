import pymysql
from departamento import Departamento

class DepartamentoRepositorio:
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
                CREATE TABLE IF NOT EXISTS departamentos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL
                )
            """)
            conexion.commit()
        finally:
            conexion.close()

    # 1. CREATE
    def guardar(self, departamento: Departamento) -> Departamento:
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO departamentos (nombre) VALUES (%s)",
                (departamento.nombre,)
            )
            conexion.commit()
            departamento.id_departamento = cursor.lastrowid
            return departamento
        finally:
            conexion.close()

    # 2. READ (BUSCAR)
    def buscar_por_id(self, id_departamento: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre FROM departamentos WHERE id=%s",
                (id_departamento,)
            )
            fila = cursor.fetchone()
            if fila:
                return Departamento(id_departamento=fila[0], nombre=fila[1])
            return None
        finally:
            conexion.close()

    # 3. READ ALL (LISTAR)
    def listar(self):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre FROM departamentos")
            filas = cursor.fetchall()
            return [Departamento(id_departamento=f[0], nombre=f[1]) for f in filas]
        finally:
            conexion.close()

    # 4. UPDATE
    def actualizar(self, departamento: Departamento):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE departamentos SET nombre=%s WHERE id=%s",
                (departamento.nombre, departamento.id_departamento)
            )
            conexion.commit()
        finally:
            conexion.close()

    # 5. DELETE
    def eliminar(self, id_departamento: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM departamentos WHERE id=%s", (id_departamento,))
            conexion.commit()
        finally:
            conexion.close()