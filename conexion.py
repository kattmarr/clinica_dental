import mysql.connector

try:
    con = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # o tu contraseña real
        database="clinica_dental"
    )
    print("Conectado correctamente ✅")
except mysql.connector.Error as err:
    print("Error:", err)
