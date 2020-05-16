import json

from flask_restful_swagger_2 import swagger
from flask_restful import Resource

from backend_api.endpoints.user.assemble import Assembler
from backend_api.endpoints.user.model import UserResponseModel, TelephoneModel
from backend_api.manager.factory import ManagerSimplifiedFactory


class UserResponse(Resource):

    @swagger.doc({
        'tags': ['user'],
        'description': 'Returns a user',
        'parameters': [
            {
                'name': 'username',
                'description': 'Name of the user',
                'in': 'path',
                'type': 'string'
            }
        ],
        'responses': {
            '200': {
                'description': 'User',
                'schema': UserResponseModel,
                'examples': {
                    'application/json': {
                        'id': 1,
                        'name': 'somebody'
                    }
                }
            }
        }
     })
    def get(self, username):

        user_manager = ManagerSimplifiedFactory().get_user_manager()
        user_details, telephone_details = user_manager.get_user_data(user=username)

        out = Assembler(user_data=user_details, telephone_data=telephone_details).assemble()

        return out
