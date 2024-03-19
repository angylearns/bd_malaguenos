class Detalle_Pedido():
    def __init__(self, id_detalle, cantidad, precio_unitario, precio_total, pedido, producto) -> None:
        self.id_detalle = id_detalle
        self.cantidad = cantidad
        self.precio_unitario = precio_unitario
        self.precio_total = precio_total
        self.pedido = pedido
        self.producto = producto