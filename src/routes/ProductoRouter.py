from flask import Blueprint, request, jsonify
from src.services.ProductoService import ProductoService
from src.models.productoModel import Producto

getR = Blueprint('producto_blu_get', __name__)
postR = Blueprint('producto_blu_post', __name__)
patchR = Blueprint('producto_blu_patch', __name__)
deleteR = Blueprint('producto_blu_delete', __name__)

@getR.route('/', methods=['GET'])
def manage_productos_getR():
    ProductoService.get_productos()
    print("Consola: Productos obtenidos.")

    return 'Página: Productos obtenidos.'

@postR.route('/', methods=['POST'])
def manage_productos_postR():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # capturamos los datos del json (1)
    nombreProd = request.json['nombreProd'] if 'nombreProd' in request.json else None
    descripcionProd = request.json['descripcionProd'] if 'descripcionProd' in request.json else None
    marcaProd = request.json['marcaProd'] if 'marcaProd' in request.json else None
    precioProd = request.json['precioProd'] if 'precioProd' in request.json else None
    stockProd = request.json['stockProd'] if 'stockProd' in request.json else None
    
    # para nuevo producto, instanciamos el objeto del nuevo producto (2)
    nuevoProducto = Producto(0, nombreProd, descripcionProd, marcaProd, precioProd, stockProd)

    # le pasamos como parámetro el nuevoProducto al método post_productos() (3)    
    if ProductoService.post_productos(nuevoProducto):
        print('Consola:Producto insertado: ', nuevoProducto)
        return 'Producto creado.'
    
    return 'Página: Ok'

@patchR.route('/<int:id_producto>', methods=['PATCH'])
def manage_productos_patchR(id_producto):
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    # capturamos los datos del json (1)
    nombreProd = request.json['nombreProd'] if 'nombreProd' in request.json else None
    descripcionProd = request.json['descripcionProd'] if 'descripcionProd' in request.json else None
    marcaProd = request.json['marcaProd'] if 'marcaProd' in request.json else None
    precioProd = request.json['precioProd'] if 'precioProd' in request.json else None
    stockProd = request.json['stockProd'] if 'stockProd' in request.json else None

    # Instanciamos el objeto productoActualizado con los datos capturados
    productoActualizado = Producto(id_producto, nombreProd, descripcionProd, marcaProd, precioProd, stockProd)

    ProductoService.update_productos(productoActualizado)
    print('Consola: Producto actualizado: ', productoActualizado)

    return 'Página: Producto actualizado.'


@deleteR.route('/<int:idProd>', methods=['DELETE'])
def manage_productos_deleteR(idProd):
    
    ProductoService.delete_productos(idProd) 
    print('Consola: Producto eliminado.')

    return 'Página: Producto eliminado.'