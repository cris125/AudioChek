import mysql.connector

# Establecer la conexión
connection = mysql.connector.connect(
    host="181.79.5.78",        # IP del servidor de base de datos
    user="root",               # Usuario de la base de datos
    password="P4ng0l1n854",     # Contraseña del usuario
    database="db1"             # Nombre de la base de datos
)

# Verificar si la conexión fue exitosa
if connection.is_connected():
    print("Conexión exitosa a la base de datos")

# Cerrar la conexión
connection.close()
