import unittest
import json

from signer import preparer

class PreparerTest(unittest.TestCase):
    def check_payload(self, obj: object, expected_payload: str):
        sub = preparer.PreparerFactory().get_preparer(obj)
        self.assertEqual(expected_payload, sub.parse())

    def test_empty_dict(self):
        self.check_payload(dict(), "")

    def test_empty_array(self):
        self.check_payload([], "")

    def test_one_key_dict(self):
        obj = json.loads('{"foo": "bar"}')
        self.check_payload(obj, 'foo=bar')

    def test_two_key_dict(self):
        obj = json.loads('{"a":"foo", "b": "bar"}')
        self.check_payload(obj, "a=foo&b=bar")

    def test_two_key_dict_with_unordered_keys(self):
        obj = json.loads('{"b": "bar", "a":"foo"}')
        self.check_payload(obj, "a=foo&b=bar")

    def test_one_item_array(self):
        self.check_payload(["foo"], '[0]=foo')

    def test_two_items_array(self):
        self.check_payload(["foo", "bar"], '[0]=foo&[1]=bar')