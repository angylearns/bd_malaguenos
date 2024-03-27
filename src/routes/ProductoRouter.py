from flask import Blueprint, request
from src.services.ProductoService import ProductoService

from src.models.productoModel import Producto

main1 = Blueprint('producto_blu1', __name__)
main2 = Blueprint('producto_blu2', __name__)

# ruta raíz
@main1.route('/', methods=['GET', 'POST'])
def manage_productos():
    # capturamos los datos del json (1)
    idProd = request.json['idProd'] if 'idProd' in request.json else None
    nombreProd = request.json['nombreProd'] if 'nombreProd' in request.json else None
    descripcionProd = request.json['descripcionProd'] if 'descripcionProd' in request.json else None
    marcaProd = request.json['marcaProd'] if 'marcaProd' in request.json else None
    precioProd = request.json['precioProd'] if 'precioProd' in request.json else None
    stockProd = request.json['stockProd'] if 'stockProd' in request.json else None


    # para nuevo producto, instanciamos el objeto del nuevo producto (2)
    nuevoProducto = Producto(0, nombreProd, descripcionProd, marcaProd, precioProd, stockProd)

    if request.method == 'GET':
        ProductoService.get_productos()
        print("Productos:", ProductoService.get_productos())

    # le pasamos como parámetro el nuevoProducto al método post_productos() (3)
    elif request.method == 'POST':  
        ProductoService.post_productos(nuevoProducto)
        print('Producto insertado')

@main2.route('/<int:id_producto>', methods=['PATCH', 'DELETE'])
def manage_productos(id_producto):
    # capturamos los datos del json (1)
    idProd = request.json['idProd'] if 'idProd' in request.json else None
    nombreProd = request.json['nombreProd'] if 'nombreProd' in request.json else None
    descripcionProd = request.json['descripcionProd'] if 'descripcionProd' in request.json else None
    marcaProd = request.json['marcaProd'] if 'marcaProd' in request.json else None
    precioProd = request.json['precioProd'] if 'precioProd' in request.json else None
    stockProd = request.json['stockProd'] if 'stockProd' in request.json else None

    # Instanciamos el objeto productoActualizado con los datos capturados
    productoActualizado = Producto(idProd, nombreProd, descripcionProd, marcaProd, precioProd, stockProd)

    if request.method == 'PATCH':
        ProductoService.update_productos(productoActualizado)
        print('Producto actualizado', productoActualizado)

    elif request.method == 'DELETE':
        ProductoService.delete_productos(idProd) 
        print('Producto eliminado')
        
    return 'Esto se ve en la página'