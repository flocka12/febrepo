from flask import Flask, Blueprint

from app.api.v2 import version_two as v2

def appCreate():
    app = Flask(__name__)
    app.register_blueprint(v2)
    return app
    