from flask import Flask
from flask_restful_swagger_2 import Api
from flask_swagger_ui import get_swaggerui_blueprint

# Import resources
from backend_api.endpoints.user.views import UserResponse
from backend_api.endpoints.users.views import UsersResponse

# Initialize flask

app = Flask(__name__)
api = Api(app, api_version='1.0')

# Initialize swagger UI (blueprint)
SWAGGER_URL = '/api/docs'
API_URL = '../swagger.json'

swaggerui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "TEST API",
        'validatorUrl': None,
        "enableCORS": False,
    },
)

app.register_blueprint(swaggerui_blueprint, url_prefix=SWAGGER_URL)

# Add resources
api.add_resource(UserResponse, '/user/<string:username>')
api.add_resource(UsersResponse, '/users')

if __name__ == '__main__':
    app.run()
