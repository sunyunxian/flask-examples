from flask import Flask
from app.api import api_bp


def creat_app():
    print('create_app')
    app = Flask(__name__)
    register_api_blueprint(app)
    return app


def register_api_blueprint(app):
    app.register_blueprint(api_bp, url_prefix='/api')
