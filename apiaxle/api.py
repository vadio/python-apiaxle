class Api():

    def __init__(self, api, api_name, **kwargs):
        self._api_name = api_name
        for key in api:
            setattr(self, key, api[key])

        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        return self._api_name
