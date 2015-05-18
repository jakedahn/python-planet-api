from planet_api import base
from planet_api import resources
from planet_api.resources import scenes

import requests


class BaseClient(object):

    def __init__(self, base_url='https://api.planet.com', api_key=None,
                 email=None, password=None):
        self.base_url = base_url
        self._api_key = api_key
        self._email = email
        self._password = password

        self.token = None
        self.auth_headers = {
            'Authorization': 'api-key ' + self.token,
        }

    def authenticate(self):
        raise base.NotImplementedError()


class ApiV0Client(BaseClient):
    scenes = None
    # mosaics = None
    # workspaces = None

    def __init__(self, *args, **kwargs):
        super(ApiV0Client, self).__init__(*args, **kwargs)
        self.scenes = scenes.ScenesResource(client=self)

    def authenticate(self):
        if self._api_key:
            self.token = self._api_key
            return True

        req_url = '{base_url}/v0/auth/login'.format(base_url=self.base_url)
        payload = dict(email=self._email, password=self._password)

        res = requests.post(req_url, data=payload)
        self.token = res['token']
