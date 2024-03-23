from flask import Blueprint, request
from src.services.ProductoService import ProductoService

main = Blueprint('producto_blu', __name__)

# ruta raíz
@main.route('/')
def get_productos():
    print(request)
    print(request.method)
    ProductoService.get_productos()

    print('Esto se imprime en consola')
    return 'Esto se ve en la página'