from empleado import Empleado
from proyecto import Proyecto

class GestorAutenticacion:
    def validar_password(self, empleado: Empleado, password_plano: str) -> bool:
        """Valida el acceso del empleado."""
        # Nota: Asegúrate de añadir el atributo 'password_hash' a tu clase Empleado
        # si vas a utilizar este servicio en el menú.
        if hasattr(empleado, 'password_hash'):
            es_valido = empleado.password_hash == password_plano
            estado = "exitoso" if es_valido else "fallido"
            print(f"Intento de autenticación para {empleado.nombre}: {estado}.")
            return es_valido
        print(f"El empleado {empleado.nombre} no tiene contraseña configurada.")
        return False


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