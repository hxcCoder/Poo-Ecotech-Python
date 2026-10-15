import pymysql
from proyecto import Proyecto

class ProyectoRepositorio:
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
                CREATE TABLE IF NOT EXISTS proyectos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(100) NOT NULL,
                    descripcion TEXT NOT NULL
                )
            """)
            conexion.commit()
        finally:
            conexion.close()

    # 1. CREATE
    def guardar(self, proyecto: Proyecto) -> Proyecto:
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "INSERT INTO proyectos (nombre, descripcion) VALUES (%s, %s)",
                (proyecto.nombre, proyecto.descripcion)
            )
            conexion.commit()
            proyecto.id_proyecto = cursor.lastrowid
            return proyecto
        finally:
            conexion.close()

    # 2. READ (BUSCAR)
    def buscar_por_id(self, id_proyecto: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "SELECT id, nombre, descripcion FROM proyectos WHERE id=%s",
                (id_proyecto,)
            )
            fila = cursor.fetchone()
            if fila:
                return Proyecto(id_proyecto=fila[0], nombre=fila[1], descripcion=fila[2])
            return None
        finally:
            conexion.close()

    # 3. READ ALL (LISTAR)
    def listar(self):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("SELECT id, nombre, descripcion FROM proyectos")
            filas = cursor.fetchall()
            return [Proyecto(id_proyecto=f[0], nombre=f[1], descripcion=f[2]) for f in filas]
        finally:
            conexion.close()

    # 4. UPDATE
    def actualizar(self, proyecto: Proyecto):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute(
                "UPDATE proyectos SET nombre=%s, descripcion=%s WHERE id=%s",
                (proyecto.nombre, proyecto.descripcion, proyecto.id_proyecto)
            )
            conexion.commit()
        finally:
            conexion.close()

    # 5. DELETE
    def eliminar(self, id_proyecto: int):
        conexion = pymysql.connect(**self.config)
        try:
            cursor = conexion.cursor()
            cursor.execute("DELETE FROM proyectos WHERE id=%s", (id_proyecto,))
            conexion.commit()
        finally:
            conexion.close()