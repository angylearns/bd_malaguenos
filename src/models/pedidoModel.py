class Pedido():
    def __init__(self, id_pedido, fecha_pedido, cliente) -> None:
        self.id_pedido = id_pedido
        self._fecha_pedido = fecha_pedido
        self._cliente = cliente