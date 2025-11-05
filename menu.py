import customtkinter as ctk

def abrir_menu():
    app = ctk.CTk()
    app.title("OdontoSys - Menú principal")
    app.geometry("400x350")
    ctk.set_appearance_mode("light")

    ctk.CTkLabel(app, text="Sistema de Ventas Odontológicas", font=("Arial", 18, "bold")).pack(pady=20)

    ctk.CTkButton(app, text="Pacientes", width=200).pack(pady=10)
    ctk.CTkButton(app, text="Ventas", width=200).pack(pady=10)
    ctk.CTkButton(app, text="Inventario", width=200).pack(pady=10)
    ctk.CTkButton(app, text="Salir", width=200, command=app.destroy).pack(pady=20)

    app.mainloop()
