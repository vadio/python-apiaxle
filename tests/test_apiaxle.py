import nose
from apiaxle import api, key, restclient, Apiaxle
import unittest
from mock import patch
import os, json
import logging as logger


def test_get_test_api(*args):
    f = open('tests/resources/test_api')
    return json.loads(f.read())['results']


# def test_post_create_api(rest_client, path, **kwargs):
#     pass


class TestApiaxle(unittest.TestCase):

    def setUp(self):
        self.apiaxle = Apiaxle()
        self.start_patchers()
        self.test_api = self.apiaxle.api('test_api')

    def test_get_api(self):
        self.assertIsInstance(self.test_api, api.Api)

    def test_api_endooint(self):
        self.assertEqual(self.test_api.name, 'test_api')
        self.assertEqual(self.test_api.endPoint, 'test-endpoint')

    def test_create_api(self):
        test_api_2 = self.apiaxle.new_api('test_api_2', endPoint="test_api_2_endpoint")
        self.assertEqual(test_api_2.name, 'test_api_2')
        self.assertEqual(test_api_2.endPoint, 'test-endpoint')
        self.assertIsInstance(test_api_2, api.Api)

    def teardown(self):
        self.stop_patchers()

    @property
    def patchers(self):
        return [
            patch('apiaxle.restclient.RestClient.get', test_get_test_api),
            #patch('apiaxle.restclient.RestClient.post', test_post_create_api),
        ]

    def start_patchers(self):
        for patch in self.patchers:
            patch.start()

    def stop_patchers(self):
        for patch in self.patchers:
            patch.stop()
