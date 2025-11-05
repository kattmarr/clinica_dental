import customtkinter as ctk
from conexion import conectar
from menu import abrir_menu

def abrir_login():
    ventana = ctk.CTk()
    ventana.title("Login - OdontoSys")
    ventana.geometry("350x250")
    ctk.set_appearance_mode("light")

    ctk.CTkLabel(ventana, text="Inicio de sesión", font=("Arial", 18, "bold")).pack(pady=10)

    usuario = ctk.CTkEntry(ventana, placeholder_text="Usuario")
    usuario.pack(pady=5)

    contrasena = ctk.CTkEntry(ventana, placeholder_text="Contraseña", show="*")
    contrasena.pack(pady=5)

    mensaje = ctk.CTkLabel(ventana, text="", text_color="red")
    mensaje.pack()

    def ingresar():
        user = usuario.get()
        passw = contrasena.get()
        conexion = conectar()
        if conexion:
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM usuarios WHERE usuario=%s AND contrasena=%s", (user, passw))
            datos = cursor.fetchone()
            conexion.close()
            if datos:
                ventana.destroy()
                abrir_menu()
            else:
                mensaje.configure(text="Usuario o contraseña incorrecta")
        else:
            mensaje.configure(text="Error al conectar con la base de datos")

    ctk.CTkButton(ventana, text="Ingresar", command=ingresar).pack(pady=15)

    ventana.mainloop()
