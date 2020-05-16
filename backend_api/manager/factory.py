from backend_api.dao.factory import DaoSimplifiedFactory
from backend_api.manager.user import UserManager

# TODO: It should be Singleton
class ManagerSimplifiedFactory(object):

    def get_user_manager(self):

        user_dao = DaoSimplifiedFactory().get_user_dao()
        telephone_dao = DaoSimplifiedFactory().get_telephone_dao()

        return UserManager(user_dao=user_dao, telephone_dao=telephone_dao)
