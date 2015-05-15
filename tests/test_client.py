import fixtures  # sample responses, etc
import unittest


from mock import patch
from planet_api import base
from planet_api import clients


class TestClient(unittest.TestCase):

    def setUp(self):
        self.test_base_url = 'http://apitest.foo.com'
        self.test_api_key = 'foobarwibblewobble'
        self.test_email = 'user@place.com'
        self.test_password = 'seeekr3t'

    def tearDown(self):
        pass

    def test_base_client(self):
        client = base.BaseClient(base_url=self.test_base_url,
                                 api_key=self.test_api_key,
                                 email=self.test_email,
                                 password=self.test_password)

        self.assertEqual(None, client.token)
        self.assertEqual(self.test_base_url, client.base_url)
        self.assertEqual(self.test_api_key, client._api_key)
        self.assertEqual(self.test_email, client._email)
        self.assertEqual(self.test_password, client._password)

        with self.assertRaises(base.NotImplementedError):
            client.authenticate()

    def test_client_authenticate(self):
        client_with_key = clients.ApiV0Client(base_url=self.test_base_url,
                                              api_key=self.test_api_key)
        client_with_account = clients.ApiV0Client(base_url=self.test_base_url,
                                                  email=self.test_email,
                                                  password=self.test_password)

        client_with_key.authenticate()
        self.assertEqual(self.test_api_key, client_with_key.token)

        with patch('requests.post') as req_mock:
            req_mock.return_value = dict(token='fancytoken')

            client_with_account.authenticate()

            req_mock.assert_called_once_with(
                '{base_url}/v0/auth/login'.format(base_url=self.test_base_url),
                data=dict(email=self.test_email, password=self.test_password))

        self.assertEqual('fancytoken', client_with_account.token)
