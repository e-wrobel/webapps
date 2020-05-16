from backend_api.dao.telephone_dao import TelephoneDao
from backend_api.dao.user_dao import UserDao

# TODO: It should be Singleton
class DaoSimplifiedFactory(object):

    def get_user_dao(self):

        return UserDao()

    def get_telephone_dao(self):

        return TelephoneDao()
