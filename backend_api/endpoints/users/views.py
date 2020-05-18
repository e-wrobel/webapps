from flask_restful_swagger_2 import swagger
from flask_restful import Resource

from backend_api.endpoints.user.assemble import Assembler
from backend_api.endpoints.user.model import UserResponseModel, TelephoneModel, UserInputModel
from backend_api.manager.factory import ManagerSimplifiedFactory
from flask import request

class UsersResponse(Resource):

    @swagger.doc({
        'tags': ['users-post'],
        'description': 'Returns a user',
        'parameters': [
            {
                'name': 'body',
                'description': 'The cluster create operation parameters.',
                'in': 'body',
                'schema': UserInputModel,
                'required': True,
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
    def post(self):

        body = request.get_json()
        username = body['Name']
        surename = body['SurName']

        username = "{}-{}".format(username, surename)
        user_manager = ManagerSimplifiedFactory().get_user_manager()
        user_details, telephone_details = user_manager.get_user_data(user=username)

        out = Assembler(user_data=user_details, telephone_data=telephone_details).assemble()

        return out