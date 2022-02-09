import os
from flask import Flask
from app.web import web
from app.models.movies import db


def create_app():
    app = Flask('__name__', template_folder='app/templates', static_folder='app/static')
    # register blueprit
    register_blueprint(app)
    # load config, later will use env load
    load_config(app)
    init_databases(app)
    return app


def register_blueprint(app):
    app.register_blueprint(web)


def load_config(app):
    app.config.from_object('app.config.base.Base')  # load base config
    if os.environ['FLASK_ENV'] == 'development':
        app.config.from_object('app.config.development_config.DevelopmentConfig')
    elif os.environ['FLASK_ENV'] == 'testing':
        app.config.from_object('app.config.testing_config.TestingConfig')
    elif os.environ['FLASK_ENV'] == 'production':
        app.config.from_object('app.config.production_config.ProductionConfig')
    else:
        raise KeyError('Not found FLASK_ENV')


def init_databases(app):
    db.init_app(app)
    db.create_all(app=app)
