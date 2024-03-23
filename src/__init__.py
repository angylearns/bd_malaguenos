from flask import Flask

from src.routes import ProductoRouter

app = Flask(__name__)

def init_app(conf):
    app.config.from_object(conf)

    app.register_blueprint(ProductoRouter.main, url_prefix='/producto')
    return app