
class Key():

    def __init__(self, api_key, key_text, **kwargs):
        self._key_text = key_text
        for key in api_key:
            setattr(self, key, api_key[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        return self._key_text
