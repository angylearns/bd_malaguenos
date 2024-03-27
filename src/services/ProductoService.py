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
                return 'Producto creado.'
            else:
                print("No se pudo establecer la conexión.")
        except Exception as ex:
            print("Error al obtener la aplicación:", ex)
            
    @classmethod
    def update_productos(cls, productoActualizado: Producto):
        try:
            connection = get_connection()
            
            if connection:
                print("Método update", connection)
                with connection.cursor() as bd_malaguenos:
                    # Preparar la consulta SQL UPDATE
                    sql_update_query = """UPDATE producto SET nombre = %s, descripcion = %s, marca = %s, precio = %s, stock = %s WHERE id_producto = %s"""
                    # Valores actualizados del producto
                    valores_actualizados = (productoActualizado._nombre, productoActualizado._descripcion, productoActualizado._marca, productoActualizado._precio, productoActualizado._stock, productoActualizado._id_producto)
                    # Ejecutar la consulta de actualización
                    bd_malaguenos.execute(sql_update_query, valores_actualizados)
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
                    sql_delete_query = """DELETE FROM producto WHERE id_producto = %s"""
                    bd_malaguenos.execute(sql_delete_query, (idProd,))
                    connection.commit()
                connection.close()
                return 'Producto eliminado.'
            else:
                print("No se pudo establecer la aplicación.")
        except Exception as ex:
            print("Error al eliminar el producto:", ex)