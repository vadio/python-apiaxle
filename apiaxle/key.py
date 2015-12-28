
class Key(object):

    def __init__(self, rest_client, api_key, key_text):
        self._key_text = key_text
        self._client = rest_client
        self._key_path = "/key/{}".format(key_text)
        for key in api_key:
            setattr(self, key, api_key[key])

    def __str__(self):
        return self._key_text

    def update(self, **kwargs):
        response = self._client.put(self._key_path, kwargs)
        return response

    def delete(self):
        response = self._client.delete(self._key_path)
        return response
