import random


class TelephoneDao(object):

    def __init__(self):
        pass

    def get_telephone_data(self, user):
        """
        Get telephone details at the basis of username.

        :param user: given user

        :return: telephone data for given user
        :rtype dict
        """

        data = {
            'model' : 'Samsung',
            'number': self.get_number()
        }

        return data

    def get_number(self):
        """
        Simulates telephone number.

        :return: telephone number
        :rtype str
        """

        first = str(random.randint(100, 999))
        second = str(random.randint(1, 888)).zfill(3)

        last = (str(random.randint(1, 9998)).zfill(4))
        while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
            last = (str(random.randint(1, 9998)).zfill(4))

        return '{}-{}-{}'.format(first, second, last)