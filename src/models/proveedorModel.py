class Proveedor():
    def __init__(self, id_proveedor, nombre, apellido1, apellido2, direccion, localidad, pais, codigo_postal, telefono) -> None:
        self.id_proveedor = id_proveedor
        self._nombre = nombre
        self._apellido1 = apellido1
        self._apellido2 = apellido2
        self._direccion = direccion
        self._localidad = localidad
        self._pais = pais
        self._codigo_postal = codigo_postal
        self._telefono = telefono