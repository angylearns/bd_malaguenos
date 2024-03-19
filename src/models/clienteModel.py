class Cliente():
    def __init__(self, id_cliente, nombre, apellido1, apellido2, direccion, localidad, pais, codigo_postal, email, telefono) -> None:
        self.id_cliente = id_cliente
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._direccion = direccion
        self._localidad = localidad
        self._pais = pais
        self._codigo_postal = codigo_postal
        self._email = email
        self._telefono = telefono