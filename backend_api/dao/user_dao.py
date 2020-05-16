import uuid


class UserDao(object):

    def __init__(self):
        pass

    def get_user_data(self, user):
        """
        Get some basic data for given user.

        :param user: given user

        :return: user data
        :rtype dict
        """

        data = {
            'name' : user,
            'id': str(uuid.uuid4())
        }

        return data
