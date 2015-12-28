
class Api(object):

    def __init__(self, rest_client, api, api_name):
        self._api_name = api_name
        self._client = rest_client
        self._api_path = "/api/{}".format(api_name)
        for key in api:
            setattr(self, key, api[key])

    def __str__(self):
        return self._api_name

    @property
    def name(self):
        return self._api_name

    def update(self, **kwargs):
        response = self._client.put(self._api_path, kwargs)
        return response

    def delete(self):
        response = self._client.delete(self._api_path)
        return response
