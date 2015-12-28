import nose
from apiaxle import api, key, restclient, Apiaxle
import unittest


class TestKey(unittest.TestCase):

    def setUp(self):
        self.client = restclient.RestClient('test')
        self.test_key = key.Key(self.client, {'three': 3, 'four': 4}, 'test_api_name')

    def test_instance_of(self):
        self.assertIsInstance(self.test_key, key.Key)

    def test_attributes_one(self):
        self.assertTrue(self.test_key.three == 3)

    def test_attributes_two(self):
        self.assertTrue(self.test_key.four == 4)

    def test_missing_attributes(self):
        with self.assertRaises(AttributeError):
            test = self.test_key.five
