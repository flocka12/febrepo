from flask import abort
from flask_jwt_extended import jwt_required, get_jwt_identity
from flask_restful import Resource

from app.api.v2.models.getflags_model import RedflagModel
from app.api.v2.models.user_model import UserModel

class Redflags(Resource):
    ''' Returns all redflags created by the user '''
    @jwt_required
    def get(self):
        user_obj = UserModel()
        current_user = get_jwt_identity()
        user = user_obj.find_user_by_username('username', current_user)
        redflags = RedflagModel.get_all(self)
        if not user:
            abort(401, {
                "error": "This action required loggin in!",
                "status": 401
        })
        else:
            if redflags == []:
                return {'message': 'no red-flag has been added yet'}, 404
            return {
                "status": 200,
                "data": redflags
                    }, 200