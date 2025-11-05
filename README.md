🦷 Sistema de Gestión Clínica Dental
📘 Descripción del Proyecto
El Sistema de Gestión Clínica Dental es una aplicación de escritorio desarrollada en Python utilizando la librería CustomTkinter para la interfaz gráfica y MySQL como base de datos.
Está diseñado para facilitar la administración de pacientes, odontólogos, tratamientos, turnos y pagos dentro de una clínica odontológica.
Este sistema permite almacenar, consultar y organizar la información clínica y administrativa de manera rápida, segura y moderna.

🎯 Objetivos
Diseñar una aplicación de escritorio funcional para la gestión de una clínica dental.
Implementar una base de datos relacional que garantice integridad y seguridad.
Permitir registrar, modificar, eliminar y consultar datos de pacientes, odontólogos, tratamientos y pagos.
Mejorar la organización de la información mediante una interfaz intuitiva.

🧩 Tecnologías Utilizadas
Lenguaje: Python
Interfaz gráfica: CustomTkinter
Base de datos: MySQL
Conector: mysql-connector-python
IDE recomendado: Visual Studio Code

🗄️ Estructura de la Base de Datos
Base de datos: clinica_dental
Tablas principales:
paciente: información personal de los pacientes.
odontologo: datos de los doctores.
turno: citas con paciente, odontólogo, fecha y motivo.
tratamiento y tratamiento_realizado: tratamientos registrados y aplicados.
pago: pagos realizados por los pacientes.
Cada tabla cuenta con claves primarias, foráneas y restricciones para mantener la integridad de los datos.

💻 Funcionalidades Principales
Gestión de pacientes: registrar, listar y editar datos.
Gestión de odontólogos: registrar especialistas y sus datos de contacto.
Gestión de turnos: asignar citas, registrar fecha, hora y motivo.
Gestión de tratamientos: registrar servicios odontológicos y precios.
Gestión de pagos: registrar y consultar los métodos de pago y montos.
Interfaz moderna: con diseño intuitivo, botones redondeados y colores suaves.

⚙️ Requisitos del Sistema
Python 3.10 o superior
MySQL Server 8.x
Librerías necesarias:
pip install customtkinter mysql-connector-python

🚀 Ejecución del Sistema
Crear la base de datos ejecutando el script SQL clinica_dental.sql en MySQL Workbench.
Configurar la conexión en el archivo principal:
host="localhost"
user="root"
password=""
database="clinica_dental"
Ejecutar el programa:
python clinica_dental.py


🧠 Posibles Mejoras Futuras
Módulo de login con niveles de acceso (administrador / asistente).
Generación de reportes PDF y exportación a Excel.
Función de respaldo automático de la base de datos.
Sistema de notificaciones o recordatorios de turnos.

👩‍💻 Autor
Kathia Martínez
Estudiante de Ingeniería Informática – Universidad del Norte, Sede Caacupé
📍 Paraguay
