import tkinter as tk
from paciente_form import VentanaPacientes
from turno_form import VentanaTurnos

root = tk.Tk()
root.title("Clinica Dental - Sistema")
root.geometry("500x300")

tk.Label(root, text="Sistema de Clinica Dental", font=("Arial", 16)).pack(pady=20)

tk.Button(root, text="Pacientes", width=20, command=VentanaPacientes).pack(pady=10)
tk.Button(root, text="Turnos", width=20, command=VentanaTurnos).pack(pady=10)
tk.Button(root, text="Salir", width=20, command=root.destroy).pack(pady=10)

root.mainloop()
