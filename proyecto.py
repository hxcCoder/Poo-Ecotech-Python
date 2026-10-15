class Proyecto:
    def __init__(self, nombre: str, descripcion: str, id_proyecto: int = None):
        self.id_proyecto = id_proyecto
        self.nombre = nombre
        self.descripcion = descripcion

    def mostrar_datos(self) -> str:
        return f"ID: {self.id_proyecto} | Nombre: {self.nombre} | Descripción: {self.descripcion}"