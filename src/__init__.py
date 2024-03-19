from flask import Flask;

app = Flask(__name__)

def init_app(conf):
    app.config.from_object(conf)
    return app