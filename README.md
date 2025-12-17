🦷 Sistema de Gestión Clínica Dental
📘 Descripción del Proyecto

El Sistema de Gestión Clínica Dental es una aplicación de escritorio desarrollada en Python, utilizando la librería CustomTkinter para la interfaz gráfica y MySQL como sistema gestor de base de datos.
El sistema está orientado a facilitar la administración clínica y administrativa de una clínica odontológica, permitiendo gestionar pacientes, odontólogos, turnos, tratamientos, pagos y fichas clínicas de manera ordenada, segura y eficiente.
La aplicación ofrece una interfaz moderna e intuitiva, pensada para un uso sencillo por parte del personal de la clínica.

🎯 Objetivos

Diseñar una aplicación de escritorio funcional para la gestión integral de una clínica dental.
Implementar una base de datos relacional que garantice la integridad y consistencia de la información.
Permitir el registro, consulta y actualización de datos clínicos y administrativos.
Facilitar la organización de pacientes, turnos, tratamientos y pagos mediante una interfaz amigable.
Aplicar buenas prácticas de programación y modularización del código.

🧩 Tecnologías Utilizadas

Lenguaje: Python
Interfaz gráfica: CustomTkinter
Base de datos: MySQL
Conector: mysql-connector-python
Calendario: tkcalendar
IDE recomendado: Visual Studio Code

🗄️ Estructura de la Base de Datos

Base de datos: clinica_dental
Tablas principales:
paciente: datos personales del paciente.
odontologo: información de los profesionales.
turno: citas médicas con fecha, hora, paciente y odontólogo.
tratamiento: catálogo de tratamientos odontológicos.
tratamiento_realizado: tratamientos aplicados a pacientes.
historia_medica: ficha clínica del paciente.
pago: registro de pagos asociados a pacientes y turnos.
presupuesto / presupuesto_detalle: presupuestos de tratamientos.
La base de datos utiliza claves primarias y foráneas para mantener la integridad referencial entre las tablas.

💻 Funcionalidades Principales

Gestión de pacientes: registro, visualización y edición de datos.
Gestión de odontólogos: administración de profesionales y especialidades.
Gestión de turnos: asignación de citas con fecha, hora y motivo.
Gestión de tratamientos: registro de tratamientos y precios.
Ficha clínica: historial médico del paciente (enfermedades, alergias, medicación).
Gestión de pagos: registro de pagos asociados a pacientes y turnos.
Historial del paciente: visualización de turnos, tratamientos, pagos y presupuestos.
Interfaz moderna: diseño limpio, botones personalizados y colores institucionales.

⚙️ Requisitos del Sistema

Python 3.10 o superior
MySQL Server 8.x
Librerías necesarias:
pip install customtkinter mysql-connector-python tkcalendar

🚀 Ejecución del Sistema

Crear la base de datos ejecutando el script SQL clinica_dental.sql en MySQL Workbench.
Configurar la conexión a la base de datos en el archivo principal:

host="localhost"
user="root"
password=""
database="clinica_dental"

Ejecutar el sistema:
python clinica_dental.py

📊 Reportes

El sistema permite la generación de reportes en Excel, centralizando en una sola hoja información de:
Pacientes
Turnos
Pagos
Esto facilita el análisis administrativo y la presentación de información.

👩‍💻 Autor

Kathia Martínez
Estudiante de Ingeniería Informática
Universidad del Norte – Sede Caacupé
📍 Paraguay
