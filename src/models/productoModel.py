class Producto():
    def __init__(self, id_producto, nombre, descripcion, marca, precio, stock) -> None:
        self._id_producto = id_producto
        self._nombre = nombre
        self._descripcion = descripcion
        self._marca = marca
        self._precio = precio
        self._stock = stock