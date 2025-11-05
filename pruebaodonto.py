import customtkinter as ctk
from tkinter import ttk, messagebox
import mysql.connector
from datetime import date

# ---------- CONEXION A MYSQL ----------
def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="clinica_dental"
    )

# ---------- FUNCIONES GENERALES ----------
def ejecutar_sql(sql, params=(), commit=False):
    con = conectar()
    cur = con.cursor()
    cur.execute(sql, params)
    if commit:
        con.commit()
    res = cur.fetchall() if cur.description else None
    con.close()
    return res

# ---------- MODULO PACIENTES ----------
def ventana_pacientes():
    v = ctk.CTkToplevel()
    v.title("Pacientes")
    v.geometry("700x400")

    ctk.CTkLabel(v, text="Gestión de Pacientes", font=("Arial", 20, "bold")).pack(pady=10)
    frame = ctk.CTkFrame(v)
    frame.pack(pady=10)

    campos = {}
    for i, campo in enumerate(["Nombre", "Apellido", "Teléfono", "Dirección", "Email"]):
        ctk.CTkLabel(frame, text=campo+":").grid(row=i, column=0, padx=10, pady=5, sticky="e")
        entrada = ctk.CTkEntry(frame, width=250)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        campos[campo.lower()] = entrada

    def guardar():
        sql = """INSERT INTO paciente (nombre, apellido, telefono, direccion, email)
                 VALUES (%s,%s,%s,%s,%s)"""
        datos = tuple(campos[c].get() for c in campos)
        ejecutar_sql(sql, datos, commit=True)
        messagebox.showinfo("Éxito", "Paciente guardado correctamente")
        cargar_tabla()

    ctk.CTkButton(frame, text="Guardar", command=guardar).grid(row=6, column=0, columnspan=2, pady=10)

    # Tabla
    tabla = ttk.Treeview(v, columns=("ID","Nombre","Apellido","Teléfono"), show="headings")
    for col in ("ID","Nombre","Apellido","Teléfono"):
        tabla.heading(col, text=col)
        tabla.column(col, width=150)
    tabla.pack(pady=10, fill="x")

    def cargar_tabla():
        for f in tabla.get_children():
            tabla.delete(f)
        filas = ejecutar_sql("SELECT pac_id, nombre, apellido, telefono FROM paciente")
        for fila in filas:
            tabla.insert("", "end", values=fila)

    cargar_tabla()

# ---------- MODULO ODONTOLOGOS ----------
def ventana_odontologos():
    v = ctk.CTkToplevel()
    v.title("Odontólogos")
    v.geometry("600x400")
    ctk.CTkLabel(v, text="Gestión de Odontólogos", font=("Arial", 20, "bold")).pack(pady=10)
    frame = ctk.CTkFrame(v)
    frame.pack(pady=10)

    campos = {}
    for i, campo in enumerate(["Nombre","Apellido","Especialidad","Teléfono","Email"]):
        ctk.CTkLabel(frame, text=campo+":").grid(row=i, column=0, padx=10, pady=5)
        entrada = ctk.CTkEntry(frame, width=250)
        entrada.grid(row=i, column=1, padx=10, pady=5)
        campos[campo.lower()] = entrada

    def guardar():
        sql = """INSERT INTO odontologo (nombre, apellido, especialidad, telefono, email)
                 VALUES (%s,%s,%s,%s,%s)"""
        datos = tuple(campos[c].get() for c in campos)
        ejecutar_sql(sql, datos, commit=True)
        messagebox.showinfo("Éxito", "Odontólogo guardado correctamente")
        cargar_tabla()

    ctk.CTkButton(frame, text="Guardar", command=guardar).grid(row=6, column=0, columnspan=2, pady=10)

    tabla = ttk.Treeview(v, columns=("ID","Nombre","Apellido","Especialidad"), show="headings")
    for col in ("ID","Nombre","Apellido","Especialidad"):
        tabla.heading(col, text=col)
    tabla.pack(pady=10, fill="x")

    def cargar_tabla():
        for f in tabla.get_children():
            tabla.delete(f)
        filas = ejecutar_sql("SELECT odo_id, nombre, apellido, especialidad FROM odontologo")
        for fila in filas:
            tabla.insert("", "end", values=fila)

    cargar_tabla()

# ---------- MODULO TURNOS ----------
def ventana_turnos():
    v = ctk.CTkToplevel()
    v.title("Turnos")
    v.geometry("700x400")
    ctk.CTkLabel(v, text="Gestión de Turnos", font=("Arial", 20, "bold")).pack(pady=10)
    frame = ctk.CTkFrame(v)
    frame.pack(pady=10)

    pacientes = ejecutar_sql("SELECT pac_id, CONCAT(nombre,' ',apellido) FROM paciente")
    odontologos = ejecutar_sql("SELECT odo_id, CONCAT(nombre,' ',apellido) FROM odontologo")

    lista_pac = {f"{n}": i for i,n in pacientes}
    lista_odo = {f"{n}": i for i,n in odontologos}

    cb_pac = ctk.CTkComboBox(frame, values=list(lista_pac.keys()), width=250)
    cb_odo = ctk.CTkComboBox(frame, values=list(lista_odo.keys()), width=250)
    fecha = ctk.CTkEntry(frame, placeholder_text="YYYY-MM-DD")
    hora = ctk.CTkEntry(frame, placeholder_text="HH:MM")
    motivo = ctk.CTkEntry(frame, placeholder_text="Motivo de la consulta", width=250)

    ctk.CTkLabel(frame, text="Paciente:").grid(row=0, column=0, pady=5)
    cb_pac.grid(row=0, column=1)
    ctk.CTkLabel(frame, text="Odontólogo:").grid(row=1, column=0, pady=5)
    cb_odo.grid(row=1, column=1)
    ctk.CTkLabel(frame, text="Fecha:").grid(row=2, column=0)
    fecha.grid(row=2, column=1)
    ctk.CTkLabel(frame, text="Hora:").grid(row=3, column=0)
    hora.grid(row=3, column=1)
    ctk.CTkLabel(frame, text="Motivo:").grid(row=4, column=0)
    motivo.grid(row=4, column=1)

    def guardar_turno():
        sql = """INSERT INTO turno (pac_id, odo_id, fecha, hora, motivo)
                 VALUES (%s,%s,%s,%s,%s)"""
        datos = (lista_pac[cb_pac.get()], lista_odo[cb_odo.get()], fecha.get(), hora.get(), motivo.get())
        ejecutar_sql(sql, datos, commit=True)
        messagebox.showinfo("Éxito", "Turno registrado correctamente")
        cargar_tabla()

    ctk.CTkButton(frame, text="Guardar", command=guardar_turno).grid(row=5, column=0, columnspan=2, pady=10)

    tabla = ttk.Treeview(v, columns=("ID","Paciente","Odontólogo","Fecha","Hora"), show="headings")
    for col in ("ID","Paciente","Odontólogo","Fecha","Hora"):
        tabla.heading(col, text=col)
    tabla.pack(fill="x", pady=10)

    def cargar_tabla():
        for f in tabla.get_children():
            tabla.delete(f)
        filas = ejecutar_sql("""SELECT t.tur_id, p.nombre, o.nombre, t.fecha, t.hora
                             FROM turno t
                             JOIN paciente p ON p.pac_id=t.pac_id
                             JOIN odontologo o ON o.odo_id=t.odo_id""")
        for fila in filas:
            tabla.insert("", "end", values=fila)

    cargar_tabla()

# ---------- MODULO TRATAMIENTOS ----------
def ventana_tratamientos():
    v = ctk.CTkToplevel()
    v.title("Tratamientos")
    v.geometry("600x400")
    ctk.CTkLabel(v, text="Gestión de Tratamientos", font=("Arial", 20, "bold")).pack(pady=10)
    frame = ctk.CTkFrame(v)
    frame.pack(pady=10)

    nombre = ctk.CTkEntry(frame, width=250, placeholder_text="Nombre del tratamiento")
    desc = ctk.CTkEntry(frame, width=250, placeholder_text="Descripción")
    precio = ctk.CTkEntry(frame, width=150, placeholder_text="Precio")

    ctk.CTkLabel(frame, text="Nombre:").grid(row=0, column=0)
    nombre.grid(row=0, column=1)
    ctk.CTkLabel(frame, text="Descripción:").grid(row=1, column=0)
    desc.grid(row=1, column=1)
    ctk.CTkLabel(frame, text="Precio:").grid(row=2, column=0)
    precio.grid(row=2, column=1)

    def guardar():
        ejecutar_sql("INSERT INTO tratamiento (nombre, descripcion, precio) VALUES (%s,%s,%s)",
                     (nombre.get(), desc.get(), precio.get()), commit=True)
        messagebox.showinfo("Éxito", "Tratamiento guardado")
        cargar_tabla()

    ctk.CTkButton(frame, text="Guardar", command=guardar).grid(row=3, column=0, columnspan=2, pady=10)

    tabla = ttk.Treeview(v, columns=("ID","Nombre","Precio"), show="headings")
    for col in ("ID","Nombre","Precio"):
        tabla.heading(col, text=col)
    tabla.pack(fill="x", pady=10)

    def cargar_tabla():
        for f in tabla.get_children():
            tabla.delete(f)
        filas = ejecutar_sql("SELECT tra_id, nombre, precio FROM tratamiento")
        for fila in filas:
            tabla.insert("", "end", values=fila)

    cargar_tabla()

# ---------- MODULO PAGOS ----------
def ventana_pagos():
    v = ctk.CTkToplevel()
    v.title("Pagos")
    v.geometry("600x400")
    ctk.CTkLabel(v, text="Registro de Pagos", font=("Arial", 20, "bold")).pack(pady=10)

    frame = ctk.CTkFrame(v)
    frame.pack(pady=10)

    pacientes = ejecutar_sql("SELECT pac_id, CONCAT(nombre,' ',apellido) FROM paciente")
    lista_pac = {f"{n}": i for i,n in pacientes}

    cb_pac = ctk.CTkComboBox(frame, values=list(lista_pac.keys()), width=250)
    monto = ctk.CTkEntry(frame, width=150, placeholder_text="Monto")
    metodo = ctk.CTkComboBox(frame, values=["Efectivo","Tarjeta","Transferencia"], width=150)

    ctk.CTkLabel(frame, text="Paciente:").grid(row=0, column=0)
    cb_pac.grid(row=0, column=1)
    ctk.CTkLabel(frame, text="Monto:").grid(row=1, column=0)
    monto.grid(row=1, column=1)
    ctk.CTkLabel(frame, text="Método:").grid(row=2, column=0)
    metodo.grid(row=2, column=1)

    def guardar_pago():
        sql = "INSERT INTO pago (pac_id, fecha, monto, metodo) VALUES (%s,%s,%s,%s)"
        datos = (lista_pac[cb_pac.get()], date.today(), monto.get(), metodo.get())
        ejecutar_sql(sql, datos, commit=True)
        messagebox.showinfo("Éxito", "Pago registrado correctamente")
        cargar_tabla()

    ctk.CTkButton(frame, text="Guardar", command=guardar_pago).grid(row=3, column=0, columnspan=2, pady=10)

    tabla = ttk.Treeview(v, columns=("ID","Paciente","Monto","Método","Fecha"), show="headings")
    for col in ("ID","Paciente","Monto","Método","Fecha"):
        tabla.heading(col, text=col)
    tabla.pack(fill="x", pady=10)

    def cargar_tabla():
        for f in tabla.get_children():
            tabla.delete(f)
        filas = ejecutar_sql("""SELECT p.pag_id, pa.nombre, p.monto, p.metodo, p.fecha
                             FROM pago p JOIN paciente pa ON p.pac_id=pa.pac_id""")
        for fila in filas:
            tabla.insert("", "end", values=fila)

    cargar_tabla()

# ---------- VENTANA PRINCIPAL ----------
app = ctk.CTk()
app.title("Clínica Dental - Sistema")
app.geometry("500x550")
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")

titulo = ctk.CTkLabel(app, text="Clínica Dental", font=("Arial", 26, "bold"))
titulo.pack(pady=30)

ctk.CTkButton(app, text="Pacientes", width=250, height=40, command=ventana_pacientes).pack(pady=10)
ctk.CTkButton(app, text="Odontólogos", width=250, height=40, command=ventana_odontologos).pack(pady=10)
ctk.CTkButton(app, text="Turnos", width=250, height=40, command=ventana_turnos).pack(pady=10)
ctk.CTkButton(app, text="Tratamientos", width=250, height=40, command=ventana_tratamientos).pack(pady=10)
ctk.CTkButton(app, text="Pagos", width=250, height=40, command=ventana_pagos).pack(pady=10)
ctk.CTkButton(app, text="Salir", width=250, height=40, fg_color="red", hover_color="#b80000", command=app.destroy).pack(pady=20)

app.mainloop()
