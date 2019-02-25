from flask_restful import Resource

from app.api.v2.models.getflags_model import Redflag

class Redflags(Resource):
    ''' Returns all redflags created by the user '''
    def get(self):
        redflags = Redflag.get_all()
        if redflags == []:
            return {'message': 'no red-flag has been added yet'}, 404
        return {
            "status": 200,
            "data": redflags
                }, 200