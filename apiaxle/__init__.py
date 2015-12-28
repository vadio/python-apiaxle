import api, restclient, key
import logging as logger


class Apiaxle(object):

    VERSION = 'v1'

    def __init__(self, host='localhost', port=3000):
        self.host = host
        self.port = port
        self.api_url = "http://{}:{}/{}".format(self.host, self.port, self.VERSION)
        self.curl_timeout = 5
        self.host = host
        self.port = port
        self.__rest_client = restclient.RestClient(self.api_url)

    def apis(self):
        api_names = self.__rest_client.get('/apis')
        apis = []
        for api_name in api_names:
            apis.append(self.api(api_name))
        return apis

    def keys(self):
        key_names = self.__rest_client.get('/keys')
        keys = []
        for key_name in key_names:
            keys.append(self.key(key_name))
        return keys

    def new_api(self, name, **kwargs):
        response = self.__rest_client.post('/api/{}'.format(name), kwargs)
        return self.api(name)

    def new_key(self, key):
        self.__rest_client.post('/key/{}'.format(key), {})
        return self.key(key)

    def link_key(self, api, key):
        return self.__rest_client.put('/api/{api}/linkkey/{key}'.format(api=api, key=key))

    def api(self, name):
        try:
            return api.Api(self.__rest_client, self.__rest_client.get('/api/{}'.format(name)), name)
        except Exception, e:
            logger.error(e)
        return None

    def key(self, key):
        try:
            return key.Key(self.__rest_client, self.__get('/key/{}'.format(key)), key)
        except Exception, e:
            logger.error(e)
        return None
