import mysql.connector 
from mysql.connector import Error

def conexion_base():
    try:
        
        conexion = mysql.connector.connect(
            user = 'root', 
            password = '12345ADMIN',
            host = 'localhost',
            database = 'cuentas',
            port = '3306'
        )
        
        if conexion.is_connected():
            print("La conexion se ha establecido")
            return conexion

    except Error as ex:
        print("Error durante la conexion: ", ex)
        return None


def insertar_datos(conexion, nombre, apellido, edad, dni, nacionalidad, numero, descripcion, foto):
    try:
        # Crear un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Ejecutar la inserción de datos
        query = "INSERT INTO usuario (idusuario, nombre, apellido, nacionalidad, numero, descripcion, foto, edad) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)"
        datos = (dni,nombre, apellido,nacionalidad,numero,descripcion,foto,edad)
        cursor.execute(query, datos)

        # Confirmar la transacción
        conexion.commit()

        print("Datos insertados correctamente")
    except Exception as e:
        # Revertir la transacción en caso de error
        conexion.rollback()
        print(f"Error al insertar datos: {e}")
    finally:
        # Cerrar el cursor
        if cursor:
            cursor.close()

        # Cerrar la conexión
        if conexion.is_connected():
            conexion.close()
            print("Conexión cerrada")

def leer_dato_por_llave(conexion, valor):
    try:
        # Crea un cursor para ejecutar comandos SQL
        cursor = conexion.cursor()

        # Construye la consulta SQL con una cláusula WHERE
        consulta = f"SELECT * FROM usuario WHERE idusuario = %s;"
        valor_llave = (valor,)

        # Ejecuta la consulta
        cursor.execute(consulta, valor_llave)

        # Recupera el resultado
        resultado = cursor.fetchone()
        return resultado

    except Exception as e:
        print(f"Error al ejecutar la consulta: {e}")
        return None

    finally:
        # Cierra el cursor
        if cursor:
            cursor.close()