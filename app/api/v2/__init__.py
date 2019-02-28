from flask_restful import Api
from flask import Blueprint

from app.api.v2.getflags_view import Redflags
from app.api.v2.user_view import UserRegistration


AUTH_BLUEPRINT = Blueprint("auth", __name__, url_prefix='/api/v2/auth')
API_BLUEPRINT = Blueprint("api", __name__, url_prefix='/api/v2')

AUTH = Api(AUTH_BLUEPRINT)
API = Api(API_BLUEPRINT)

AUTH.add_resource(UserRegistration, '/signup')

API.add_resource(Redflags, '/Redflags')
