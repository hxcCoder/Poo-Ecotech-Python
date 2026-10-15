class Departamento:
    def __init__(self, nombre: str, id_departamento: int = None):
        self.id_departamento = id_departamento
        self.nombre = nombre

    def mostrar_datos(self) -> str:
        return f"ID: {self.id_departamento} | Nombre: {self.nombre}"