import base
import requests


class ApiV0Client(base.BaseClient):

    def authenticate(self):
        if self._api_key:
            self.token = self._api_key
            return True

        req_url = '{base_url}/v0/auth/login'.format(base_url=self.base_url)
        payload = dict(email=self._email, password=self._password)

        res = requests.post(req_url, data=payload)
        self.token = res['token']
