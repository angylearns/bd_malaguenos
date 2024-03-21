from src.database.db_mysql import get_connection

class ProductoService():
    def get_productos():
        try:
            connection = get_connection()
            if connection:
                print("Conexión establecida:", connection)
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Error al obtener la conexión:", ex)
