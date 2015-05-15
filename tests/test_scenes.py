# import fixtures  # sample responses, etc
# import unittest


# from mock import patch
# from planet_api import base
# from planet_api import resources


# class TestScenesResource(unittest.TestCase):

#     def setUp(self):
#         self.test_base_url = 'http://apitest.foo.com'
#         self.test_api_key = 'foobarwibblewobble'
#         self.test_email = 'user@place.com'
#         self.test_password = 'seeekr3t'

#     def tearDown(self):
#         pass

#     def _authenticated_client(self):
#         client = base.ApiV0Client(base_url=self.test_base_url,
#                                   email=self.test_email,
#                                   password=self.test_password)
#         client.token = 'fancytoken'
#         return client

#     def test_scenes_resource_exists(self):
#         client = self._authenticated_client()

#         self.assertEqual(resources.Scenes, client.scenes)
