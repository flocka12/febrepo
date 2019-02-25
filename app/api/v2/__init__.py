from flask_restful import Resource, Api

from app.api.v2.getflags_view import Redflags
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')

api = Api(version_two)

api.add_resource(Redflags, '/Redflags')
