import requests


class NotImplementedError(Exception):
    pass


class BaseClient(object):

    def __init__(self, base_url='https://api.planet.com', api_key=None,
                 email=None, password=None):
        self.base_url = base_url
        self._api_key = api_key
        self._email = email
        self._password = password

        self.token = None

    def authenticate(self):
        raise NotImplementedError()


class BaseResource(object):
    pass
