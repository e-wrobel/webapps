from backend_api.endpoints.user.model import UserResponseModel, TelephoneModel


class Assembler(object):

    def __init__(self, user_data, telephone_data):

        self.user_data = user_data
        self.telephone_data = telephone_data

    def assemble(self):

        telephone_model = TelephoneModel(**self.telephone_data)

        user_model = UserResponseModel(telephone=telephone_model, **self.user_data)

        return user_model
