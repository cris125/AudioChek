import mysql.connector
from mysql.connector import Error

def insertar_usuario(nombre):
    connection=None
    try:
        connection = mysql.connector.connect(
            host='181.79.5.78',
            user='root',
            password='P4ng0l1n854',
            port=33306,
            database='audicheck'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            query = "INSERT INTO 'usuarios' ('nombre') VALUES (%s)"
            values = (nombre)
            cursor.execute(query, values)
            connection.commit()
            print(f"Usuario '{nombre}' insertado correctamente")

    except Error as e:
        print(f"Error al insertar usuario: {e}")
    
    finally:
        if connection:
            if connection.is_connected():
                cursor.close()
                connection.close()

# Llamada al método para insertar un usuario
insertar_usuario("J")
