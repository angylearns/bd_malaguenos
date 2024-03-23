from src.database.db_mysql import get_connection

class ProductoService():

    @classmethod
    def get_productos(cls):
        try:
            connection = get_connection()
            if connection:
                print("Conexión establecida:", connection)
                with connection.cursor() as bd_malaguenos:
                    # este método cursor() permite ir por cada tabla. Se conecta a la conexión establecida (connection) y puede acceder a todas las tablas, permitiendo que luego ejecutemos cualquier consulta.
                    bd_malaguenos.execute("SELECT * FROM producto")
                    result = bd_malaguenos.fetchall()
                    print(result)
                    
                connection.close()
                return 'Lista mostrada.'
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Error al obtener la conexión:", ex)
