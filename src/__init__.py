from flask import Flask

from src.routes import ProductoRouter

app = Flask(__name__)

def init_app(conf):
    app.config.from_object(conf)

    app.register_blueprint(ProductoRouter.getR, url_prefix='/get')
    app.register_blueprint(ProductoRouter.postR, url_prefix='/post')
    app.register_blueprint(ProductoRouter.patchR, url_prefix='/patch/')
    app.register_blueprint(ProductoRouter.deleteR, url_prefix='/delete/')
    return app