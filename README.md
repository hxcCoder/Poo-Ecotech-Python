# Poo-Ecotech-Python

Sistema de gestión orientado a objetos desarrollado en Python para EcoTech Solutions. Este proyecto implementa la lógica de negocio y la estructura de datos necesaria para administrar empleados, proyectos, departamentos y registros de tiempo.

## 🚀 Características Principales

*   **Gestión de Empleados:** Registro de datos personales, salarios y asignación de horas trabajadas.
*   **Administración de Departamentos y Proyectos:** Agrupación de empleados por departamento y asociación de personal a proyectos específicos.
*   **Seguridad Autenticada:** Módulo de validación de contraseñas mediante hashing simulado para el acceso de empleados.
*   **Generación de Reportes:** Servicios para exportar datos de proyectos en formatos PDF y Excel.
*   **Conexión a Base de Datos:** Integración con base de datos validando la persistencia de los registros.

## 🏗️ Arquitectura y Diseño

El proyecto está diseñado siguiendo los principios de la Programación Orientada a Objetos (POO):
*   **Encapsulamiento:** Atributos protegidos con acceso controlado mediante propiedades (`@property`).
*   **Modularidad:** Separación clara entre entidades de dominio (`Empleado`, `Proyecto`) y servicios operativos (`GeneradorReportes`, `GestorAutenticacion`).
*   **Asociaciones:** Implementación de relaciones 1..* (Un departamento tiene muchos empleados, un empleado tiene múltiples registros de tiempo).

## 🛠️ Tecnologías Utilizadas

*   **Lenguaje:** Python 3.x
*   **Base de Datos:** SQLite3 (Módulo `sqlite3`) / MySQL (Módulo `pymysql` para pruebas externas).
*   **Librerías Nativas:** `datetime`, `typing`.

## ⚙️ Cómo ejecutar el proyecto

1.  Asegúrate de tener Python 3.x instalado en tu sistema.
2.  Clona este repositorio o descarga los archivos.
3.  Abre una terminal y navega hasta el directorio `Poo-Ecotech-Python`.
4.  Ejecuta el archivo principal para ver la prueba de conexión y la instanciación del modelo:

    ```bash
    python UML_Ecotech.py
    ```

El script de prueba creará objetos de demostración, simulará asociaciones entre ellos y probará el acceso a la base de datos.