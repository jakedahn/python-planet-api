import base
import requests


class BaseClient(object):

    def __init__(self, base_url='https://api.planet.com', api_key=None,
                 email=None, password=None):
        self.base_url = base_url
        self._api_key = api_key
        self._email = email
        self._password = password

        self.token = None

    def authenticate(self):
        raise base.NotImplementedError()


class ApiV0Client(BaseClient):

    def authenticate(self):
        if self._api_key:
            self.token = self._api_key
            return True

        req_url = '{base_url}/v0/auth/login'.format(base_url=self.base_url)
        payload = dict(email=self._email, password=self._password)

        res = requests.post(req_url, data=payload)
        self.token = res['token']
