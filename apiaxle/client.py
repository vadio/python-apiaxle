import cStringIO
import logging, json
import traceback
from logging import getLogger
from api import Api
from key import Key

try:
    import pycurl
except ImportError, e:
    print("Error: {}\n Please install pycurl.")


class Client():

    VERSION = 'v1'

    def __init__(self, host='localhost', port=3000):
        self.host = host
        self.port = port
        self.api_url = "http://{}:{}/{}".format(self.host, self.port, self.VERSION)
        self.curl_timeout = 5

    def __do_curl(self, path, method=None, payload=None):
        url = self.api_url + path

        header = "Content-Type: application/json"
        buf = cStringIO.StringIO()  # initialize buffer to write curl results to
        c = pycurl.Curl()
        c.setopt(pycurl.HTTPHEADER, [header])
        c.setopt(pycurl.WRITEFUNCTION, buf.write)
        c.setopt(pycurl.URL, str(url))
        c.setopt(pycurl.CONNECTTIMEOUT, self.curl_timeout)

        # pycurl auto swtiches to post when this is added
        if payload or method == "POST":
            if not payload:
                payload = {}
            c.setopt(pycurl.POSTFIELDS, json.dumps(payload))

        # forcing put even with post fields. This may not work
        if method == 'PUT':
            c.setopt(pycurl.CUSTOMREQUEST, "PUT")
        elif method == 'DELETE':
            c.setopt(pycurl.CUSTOMREQUEST, 'DELETE')

        if url.startswith('https'):
            c.setopt(pycurl.PORT, 443)
            c.setopt(pycurl.SSL_VERIFYPEER, 0)  # to make ssl work for the time being
            c.setopt(pycurl.SSL_VERIFYHOST, 0)
        try:
            c.perform()
        except Exception, e:
            logging.error(e)
            return None

        statusCode = c.getinfo(pycurl.HTTP_CODE)
        error = c.errstr()
        message = buf.getvalue()  # get results do nothing yet

        try:
            return json.loads(message).get('results')
        except Error, e:
            logging.error(message)
            logging.error(e)

        return None

    def __get(self, path):
        return self.__parse_response(self.__do_curl(path, 'GET'))

    def __post(self, path, payload):
        return self.__parse_response(self.__do_curl(path, 'POST', payload))

    def __put(self, path, payload={}):
        return self.__parse_response(self.__do_curl(path, 'PUT', payload))

    def __parse_response(self, response):
        try:
            if 'error' in response:
                logging.error(response['error']['message'])
        except TypeError, e:
            logging.error(e)

        return response

    def apis(self):
        return self.__get('/apis')

    def keys(self):
        return self.__get('/keys')

    def new_api(self, name, **kwargs):
        response = self.__post('/api/{}'.format(name), kwargs)
        return self.api(name)

    def new_key(self, key):
        self.__post('/key/{}'.format(key), {})
        return self.key(key)

    def link_key(self, api, key):
        return self.__put('/api/{api}/linkkey/{key}'.format(api=api, key=key))

    def api(self, name):
        try:
            return Api(self.__get('/api/{}'.format(name)), name)
        except Exception, e:
            logging.error(e)
        return None

    def key(self, key):
        try:
            return Key(self.__get('/key/{}'.format(key)), key)
        except Exception, e:
            logging.error(e)
        return None
