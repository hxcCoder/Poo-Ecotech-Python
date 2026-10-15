from departamento import Departamento
from departamento_repositorio import DepartamentoRepositorio
from empleado import Empleado
from empleado_repositorio import EmpleadoRepositorio
from proyecto import Proyecto
from proyecto_repositorio import ProyectoRepositorio

CONFIG_BD = {
    "host": "localhost",
    "user": "root",
    "password": "Inacap2026",
    "database": "practica"
}

repo_depto = DepartamentoRepositorio(**CONFIG_BD)
repo_emp = EmpleadoRepositorio(**CONFIG_BD)
repo_proy = ProyectoRepositorio(**CONFIG_BD)

def menu_submodulo(titulo: str, repo, crear_obj, actualizar_obj):
    while True:
        print(f"\n--- GESTIÓN DE {titulo.upper()} ---")
        print("1. Agregar")
        print("2. Buscar por ID")
        print("3. Listar todos")
        print("4. Actualizar")
        print("5. Eliminar")
        print("6. Volver al Menú Principal")

        opc = input("Seleccione opción: ")

        if opc == "1":
            obj = crear_obj()
            repo.guardar(obj)
            print(f"✓ {titulo} registrado con éxito.")

        elif opc == "2":
            idx = int(input(f"ID de {titulo}: "))
            obj = repo.buscar_por_id(idx)
            if obj:
                print(f"-> {obj.mostrar_datos()}")
            else:
                print(f"✗ {titulo} no encontrado.")

        elif opc == "3":
            lista = repo.listar()
            if not lista:
                print(f"No hay registros de {titulo}.")
            else:
                for elem in lista:
                    print(elem.mostrar_datos())

        elif opc == "4":
            idx = int(input(f"ID de {titulo} a actualizar: "))
            obj = repo.buscar_por_id(idx)
            if obj:
                actualizar_obj(obj)
                repo.actualizar(obj)
                print(f"✓ {titulo} actualizado con éxito.")
            else:
                print(f"✗ {titulo} no encontrado.")

        elif opc == "5":
            idx = int(input(f"ID de {titulo} a eliminar: "))
            repo.eliminar(idx)
            print(f"✓ {titulo} eliminado.")

        elif opc == "6":
            break
        else:
            print("Opción inválida.")

# Funciones aux para Departamento
def crear_depto():
    nombre = input("Nombre Departamento: ")
    return Departamento(nombre)

def act_depto(d):
    d.nombre = input("Nuevo Nombre: ")

# Funciones aux para Empleado
def crear_emp():
    nombre = input("Nombre: ")
    correo = input("Correo: ")
    telefono = input("Teléfono: ")
    salario = float(input("Salario: "))
    return Empleado(nombre, correo, telefono, salario)

def act_emp(e):
    e.nombre = input("Nuevo Nombre: ")
    e.correo = input("Nuevo Correo: ")
    e.telefono = input("Nuevo Teléfono: ")
    e.salario = float(input("Nuevo Salario: "))

# Funciones aux para Proyecto
def crear_proy():
    nombre = input("Nombre Proyecto: ")
    desc = input("Descripción: ")
    return Proyecto(nombre, desc)

def act_proy(p):
    p.nombre = input("Nuevo Nombre: ")
    p.descripcion = input("Nueva Descripción: ")

# --- MENÚ PRINCIPAL ---
while True:
    print("\n==================================")
    print("   SISTEMA DE GESTIÓN ECOTECH")
    print("==================================")
    print("1. Gestionar Departamentos")
    print("2. Gestionar Empleados")
    print("3. Gestionar Proyectos")
    print("4. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        menu_submodulo("Departamento", repo_depto, crear_depto, act_depto)
    elif opcion == "2":
        menu_submodulo("Empleado", repo_emp, crear_emp, act_emp)
    elif opcion == "3":
        menu_submodulo("Proyecto", repo_proy, crear_proy, act_proy)
    elif opcion == "4":
        print("Saliendo del sistema...")
        break
    else:
        print("Opción no válida.")