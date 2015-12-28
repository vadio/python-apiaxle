import cStringIO
import logging
import traceback
import json
try:
    import pycurl
except ImportError, e:
    print("Error: {}\n Please install pycurl.")

logger = logging


class RestClient(object):

    def __init__(self, url):
        self.api_url = url
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
            logger.error(e)
            return None

        statusCode = c.getinfo(pycurl.HTTP_CODE)
        error = c.errstr()
        message = buf.getvalue()  # get results do nothing yet

        logger.error(message)

        try:
            return json.loads(message).get('results')
        except Exception, e:
            logger.error(message)
            logger.error(e)

        return None

    def get(self, path):
        return self.__parse_response(self.__do_curl(path, 'GET'))

    def post(self, path, payload):
        return self.__parse_response(self.__do_curl(path, 'POST', payload))

    def put(self, path, payload={}):
        return self.__parse_response(self.__do_curl(path, 'PUT', payload))

    def delete(self, path, payload={}):
        return self.__parse_response(self.__do_curl(path, 'DELETE', payload))

    def __parse_response(self, response):
        try:
            if 'error' in response:
                logger.error(response['error']['message'])
        except TypeError, e:
            logger.error(e)

        return response
