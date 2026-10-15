class Empleado:
    def __init__(self, nombre: str, correo: str, telefono: str, salario: float, id_empleado: int = None):
        self.id_empleado = id_empleado
        self.nombre = nombre
        self.correo = correo
        self.telefono = telefono
        self.salario = salario

    def mostrar_datos(self) -> str:
        return f"ID: {self.id_empleado} | Nombre: {self.nombre} | Correo: {self.correo} | Teléfono: {self.telefono} | Salario: ${self.salario}"