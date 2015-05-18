import fixtures  # sample responses, etc
import unittest


from mock import patch
from planet_api import base
from planet_api import clients
from planet_api import resources


class TestScenesResource(unittest.TestCase):

    def setUp(self):
        self.test_base_url = 'http://apitest.foo.com'
        self.test_api_key = 'foobarwibblewobble'
        self.test_email = 'user@place.com'
        self.test_password = 'seeekr3t'
        self.test_token = 'fancytoken'

    def tearDown(self):
        pass

    def _authenticated_client(self):
        client = clients.ApiV0Client(base_url=self.test_base_url,
                                     email=self.test_email,
                                     password=self.test_password)
        client.token = self.test_token
        return client

    def test_scenes_resource_exists_on_client(self):
        client = self._authenticated_client()
        self.assertEqual(client, client.scenes.client)

    def test_scenes_list(self):
        client = self._authenticated_client()

        with patch('requests.post') as req_mock:
            req_mock.return_value = fixtures.feature_list

            client.scenes.list()
            req_url = '{base_url}/v0/scenes/ortho'.format(
                base_url=self.test_base_url)
            req_mock.assert_called_once_with(req_url)
            # , token=self.test_token
