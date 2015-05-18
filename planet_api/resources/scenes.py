from planet_api import resources

import requests


class ScenesResource(resources.BaseResource):

    def __init__(self, client=None, *args, **kwargs):
        super(ScenesResource, self).__init__(*args, **kwargs)

        if client is None:
            raise Exception('Client not properly setup')

        self.client = client

    def list(self, filters=None):
        req_url = '{b}/v0/scenes/ortho'.format(b=self.client.base_url)

        response = requests.post(req_url)

        return response
