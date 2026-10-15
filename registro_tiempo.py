from datetime import date

class RegistroTiempo:
    def __init__(self, id_registro: int, fecha: date, horas_trabajadas: float, descripcion_tareas: str):
        self.id_registro = id_registro
        self.fecha = fecha
        self.horas_trabajadas = horas_trabajadas
        self.descripcion_tareas = descripcion_tareas

    def vincular_horas(self) -> None:
        """Vincular o procesar horas registradas."""
        print(f"Horas ({self.horas_trabajadas} hrs) vinculadas al registro N°{self.id_registro}.")