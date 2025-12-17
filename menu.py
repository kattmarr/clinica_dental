app = ctk.CTk()
app.title("Clínica Dental - Sistema")
app.geometry("700x800")
app.minsize(650, 750)
ctk.set_appearance_mode("light")
ctk.set_default_color_theme("green")
# logo
logo_img = ctk.CTkImage(
    light_image=Image.open("logo.png.jpeg"),
    size=(280, 120)
)

logo = ctk.CTkLabel(app, image=logo_img, text="")
logo.pack(pady=(20, 10))

titulo = ctk.CTkLabel(
    app,
    text="Sistema de Gestión Odontológica",
    font=("Segoe UI", 20, "bold"),
    text_color="#1C7CB8"
)
titulo.pack(pady=(0, 25))

def boton_principal(texto, comando):
    return ctk.CTkButton(
        app,
        text=texto,
        width=320,
        height=45,
        corner_radius=12,
        font=("Segoe UI", 15, "bold"),
        fg_color="#2EA8E5",
        hover_color="#1C7CB8",
        command=comando
    )
boton_principal("Pacientes", ventana_pacientes).pack(pady=8)
boton_principal("Odontólogos", ventana_odontologos).pack(pady=8)
boton_principal("Turnos", ventana_turnos).pack(pady=8)
boton_principal("Tratamientos", ventana_tratamientos).pack(pady=8)
boton_principal("Pagos", ventana_pagos).pack(pady=8)
boton_principal("Ficha clínica", ventana_ficha_clinica).pack(pady=8)
boton_principal("Presupuestos", ventana_presupuestos).pack(pady=8)
boton_principal(
    "Reporte General (Excel)",
    reporte_general_excel
).pack(pady=8)

