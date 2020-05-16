class UserManager(object):

    def __init__(self, user_dao, telephone_dao):
        self.user_dao = user_dao
        self.telephone_dao = telephone_dao

    def get_user_data(self, user):
        """
        Returns data for given user.

        :param user: given user

        :return: user data including telephone data
        :rtype (dict, dict)
        """

        telephone_details = self.telephone_dao.get_telephone_data(user=user)
        user_details = self.user_dao.get_user_data(user=user)

        return user_details, telephone_details
