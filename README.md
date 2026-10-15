## Poo-Ecotech-Python

Sistema de gestión orientado a objetos desarrollado en Python para EcoTech Solutions. Este proyecto implementa la lógica de negocio, persistencia en base de datos y un menú interactivo para administrar empleados, proyectos, departamentos y registros de tiempo.

*Nota: Para más información sobre el entorno y parámetros de este desarrollo, puedes consultar el archivo contexto-ia.txt.*

## Características Principales

*   **Menú Interactivo (CLI):** Interfaz de consola centralizada (`menu.py`) para interactuar fácilmente con los distintos módulos del sistema.
*   **Gestión de Empleados:** Registro de datos personales, datos de contacto (correo, teléfono) y salarios.
*   **Administración de Departamentos y Proyectos:** Agrupación de empleados por departamento y asociación de personal a proyectos con operaciones CRUD completas.
*   **Persistencia de Datos Automática:** Uso del patrón Repositorio (`pymysql`) que crea automáticamente las tablas necesarias (`empleados`, `departamentos`, `proyectos`) si no existen en la base de datos.
*   **Servicios Adicionales:** Clases dedicadas a la generación de reportes simulados (PDF y Excel) y validación de contraseñas[cite: 1].
*   **Registro de Tiempos:** Estructura preparada para el registro y vinculación de horas trabajadas[cite: 1].

## Arquitectura y Diseño

El proyecto está diseñado siguiendo los principios de la Programación Orientada a Objetos (POO)[cite: 1]:
*   **Patrón Repositorio:** Separación entre las clases de modelo (`Empleado`, `Departamento`, `Proyecto`) y la lógica de acceso a datos (`EmpleadoRepositorio`, etc.)[cite: 1].
*   **Modularidad:** Separación clara entre entidades de dominio y servicios operativos (`GeneradorReportes`, `GestorAutenticacion`)[cite: 1].

## Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x[cite: 1]
*   **Base de Datos:** MySQL Server[cite: 1]
*   **Librerías:** `pymysql` (para conexión a base de datos), `datetime`[cite: 1].

## Requisitos Previos

1. Asegúrate de tener instalado Python y el motor de base de datos MySQL.
2. Instala la dependencia de conexión a MySQL:
   ```bash
   pip install pymysql