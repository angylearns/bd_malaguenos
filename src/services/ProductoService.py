from src.database.db_mysql import get_connection

from src.models.productoModel import Producto

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
    
    @classmethod
    def post_productos(cls, nuevoProducto: Producto):
        try:
            connection = get_connection()
            idProd = None
            nombreProd = nuevoProducto._nombre
            descripcionProd = nuevoProducto._descripcion
            marcaProd = nuevoProducto._marca
            precioProd = nuevoProducto._precio
            stockProd = nuevoProducto._stock

            if connection:

                print("Método post", connection)
                with connection.cursor() as bd_malaguenos:
                    bd_malaguenos.execute("INSERT INTO producto (id_producto, nombre, descripcion, marca, precio, stock) VALUES (%s, %s, %s, %s, %s, %s)", (idProd, nombreProd, descripcionProd, marcaProd, precioProd, stockProd))
                    connection.commit()
                connection.close()
                return 'Lista mostrada.'
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Error al obtener la aplicación:", ex)
            