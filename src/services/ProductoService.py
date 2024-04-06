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
                    # llamamos a procedimiento almacenado
                    bd_malaguenos.execute("CALL sp_getAllProducts()")
                    # sp_getAllProducts() es el nombre del procedimiento almacenado que se encuentra en la base de datos: "SELECT * FROM producto;"
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

            nombreProd = nuevoProducto._nombre
            descripcionProd = nuevoProducto._descripcion
            marcaProd = nuevoProducto._marca
            precioProd = nuevoProducto._precio
            stockProd = nuevoProducto._stock

            if connection:

                print("Método post", connection)
                with connection.cursor() as cursor:
                # Pasar los parámetros al método execute
                    cursor.execute("CALL sp_postProduct(%s, %s, %s, %s, %s)", (nombreProd, descripcionProd, marcaProd, precioProd, stockProd))
                connection.commit()

                connection.close()
                return 'Producto creado.'
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Errorsito al obtener la aplicación:", ex)
            
    @classmethod
    def update_productos(cls, productoActualizado: Producto):
        try:
            connection = get_connection()
            
            if connection:
                print("Método update", connection)
                with connection.cursor() as bd_malaguenos:
                    sp_update_query = "CALL sp_updateProduct(%s, %s, %s, %s, %s, %s)"

                    valores_actualizados = (productoActualizado._id_producto, productoActualizado._nombre, productoActualizado._descripcion, productoActualizado._marca, productoActualizado._precio, productoActualizado._stock)

                    bd_malaguenos.execute(sp_update_query, valores_actualizados)
                    connection.commit()
                connection.close()
                return 'Producto actualizado.'
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Error al actualizar el producto:", ex)


    @classmethod
    def delete_productos(cls, idProd):
        try:
            connection = get_connection()
            
            if connection:
                print("Método delete", connection)
                with connection.cursor() as bd_malaguenos:
                    # Llamada al procedimiento almacenado sp_deleteProduct
                    bd_malaguenos.callproc('sp_deleteProduct', [idProd])
                    connection.commit()
                connection.close()
                return 'Producto eliminado.'
            else:
                print("No se pudo establecer la aplicación.")
        except Exception as ex:
            print("Error al eliminar el producto:", ex)