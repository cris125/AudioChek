import mysql.connector
from mysql.connector import Error

def crear_tabla():
    connection = None
    try:
        connection = mysql.connector.connect(
            host='181.79.5.78',
            user='root',
            password='P4ng0l1n854',
            port=33306,
            database='audicheck',  # Reemplaza con el nombre de tu base de datos
            charset='utf8mb4',
            collation='utf8mb4_general_ci'
        )

        if connection.is_connected():
            cursor = connection.cursor()
            # Consulta para crear la tabla con charset y collation especificados
            crear_tabla_query = """
            CREATE TABLE IF NOT EXISTS empleados (
                id INT AUTO_INCREMENT PRIMARY KEY,
                nombre VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                correo VARCHAR(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
                edad INT NOT NULL
            )
            """
            cursor.execute(crear_tabla_query)
            connection.commit()
            print("Tabla 'empleados' creada exitosamente.")

    except Error as e:
        print(f"Error al crear la tabla: {e}")
    
    finally:
        if connection and connection.is_connected():
            cursor.close()
            connection.close()

# Llamada para crear la tabla
crear_tabla()
