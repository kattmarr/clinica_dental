import tkinter as tk
from tkinter import ttk, messagebox
import db

def VentanaPacientes():
    ventana = tk.Toplevel()
    ventana.title("Gestion de Pacientes")
    ventana.geometry("700x400")

    # Campos
    tk.Label(ventana, text="Nombre:").grid(row=0, column=0, padx=10, pady=5)
    nombre = tk.Entry(ventana)
    nombre.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Apellido:").grid(row=1, column=0, padx=10, pady=5)
    apellido = tk.Entry(ventana)
    apellido.grid(row=1, column=1, padx=10, pady=5)

    tk.Label(ventana, text="Telefono:").grid(row=2, column=0, padx=10, pady=5)
    telefono = tk.Entry(ventana)
    telefono.grid(row=2, column=1, padx=10, pady=5)

    # Botón guardar
    def guardar():
        con = db.conectar()
        cur = con.cursor()
        sql = "INSERT INTO paciente (nombre, apellido, telefono) VALUES (%s, %s, %s)"
        cur.execute(sql, (nombre.get(), apellido.get(), telefono.get()))
        con.commit()
        con.close()
        messagebox.showinfo("Éxito", "Paciente guardado correctamente")
        cargar_datos()

    tk.Button(ventana, text="Guardar", command=guardar).grid(row=3, column=1, pady=10)

    # Tabla (Treeview)
    tabla = ttk.Treeview(ventana, columns=("ID","Nombre","Apellido","Telefono"), show="headings")
    tabla.heading("ID", text="ID")
    tabla.heading("Nombre", text="Nombre")
    tabla.heading("Apellido", text="Apellido")
    tabla.heading("Telefono", text="Telefono")
    tabla.grid(row=4, column=0, columnspan=4, padx=10, pady=10)

    def cargar_datos():
        for fila in tabla.get_children():
            tabla.delete(fila)
        con = db.conectar()
        cur = con.cursor()
        cur.execute("SELECT pac_id, nombre, apellido, telefono FROM paciente")
        for (id, nom, ape, tel) in cur.fetchall():
            tabla.insert("", "end", values=(id, nom, ape, tel))
        con.close()

    cargar_datos()
