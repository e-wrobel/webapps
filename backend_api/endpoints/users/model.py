from flask_restful_swagger_2 import Schema


class TelephoneModel(Schema):
    type = 'object'
    properties = {
        'model': {
            'type': 'string',
        },
        'number': {
            'type': 'string'
        }
    }


class UserResponseModel(Schema):
    produces = 'application/json'
    type = 'object'
    properties = {
        'id': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'telephone': TelephoneModel.array()
    }
    required = ['name']


class UserInputModel(Schema):
    produces = 'application/json'
    type = 'object'
    properties = {
        'Name': {
            'type': 'string',
            'description': "User name in body"
        },
        'SurName': {
            'type': 'string',
            'description': "User surname in body"
        }
    }
    required = ['name']