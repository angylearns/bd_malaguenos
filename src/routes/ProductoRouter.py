from flask import Blueprint, request
from src.services.ProductoService import ProductoService

from src.models.productoModel import Producto

main = Blueprint('producto_blu', __name__)

# ruta raíz
@main.route('/', methods=['GET', 'POST'])
def manage_productos():
    # capturamos los datos del json (1)
    idProd = None
    nombreProd = request.json['nombreProd']
    descripcionProd = request.json['descripcionProd']
    marcaProd = request.json['marcaProd']
    precioProd = request.json['precioProd']
    stockProd = request.json['stockProd']

    # instanciamos el objeto (2)
    nuevoProducto = Producto(0, nombreProd, descripcionProd, marcaProd, precioProd, stockProd)

    if request.method == 'GET':
        ProductoService.get_productos()
        print("Productos:", ProductoService.get_productos())

    # le pasamos como parámetro el nuevoProducto al método post_productos() (3)
    elif request.method == 'POST':  
        ProductoService.post_productos(nuevoProducto)
        print('Producto insertado')
    
    return 'Esto se ve en la página'