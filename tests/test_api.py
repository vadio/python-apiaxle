import nose
from apiaxle import api, key, restclient, Apiaxle
import unittest


class TestApi(unittest.TestCase):

    def setUp(self):
        self.client = restclient.RestClient('test')
        self.test_api = api.Api(self.client, {"one": 1, "two": 2}, 'test_api_name')

    def test_instance_of(self):
        self.assertIsInstance(self.test_api, api.Api)

    def test_attributes_one(self):
        self.assertTrue(self.test_api.one == 1)

    def test_attributes_two(self):
        self.assertTrue(self.test_api.two == 2)

    def test_missing_attributes(self):
        with self.assertRaises(AttributeError):
            test = self.test_api.three
