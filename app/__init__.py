'''Application entry module'''
from flask import Flask

from app.api.v2 import AUTH_BLUEPRINT, API_BLUEPRINT

from instance.config import APP_CONFIG

def create_app(config_name):
    '''Instantiate the Flask application'''
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(APP_CONFIG[config_name])
    app.config.from_pyfile('config.py')


    app.register_blueprint(AUTH_BLUEPRINT)
    app.register_blueprint(API_BLUEPRINT)

    return app
