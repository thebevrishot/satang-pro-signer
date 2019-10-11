import unittest
import json

from satang_pro_signer import preparer

class PreparerTest(unittest.TestCase):
    def check_payload(self, obj: object, expected_payload: str):
        sub = preparer.PreparerFactory().get_preparer(obj)
        self.assertEqual(expected_payload, sub.parse())

    # string only
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
        self.check_payload(["foo"], '0=foo')

    def test_two_items_array(self):
        self.check_payload(["foo", "bar"], '0=foo&1=bar')

    def test_two_layers_dict(self):
        obj = json.loads('{"foo": {"dog": "cat"} }')
        self.check_payload(obj, "foo[dog]=cat")

    def test_three_layers_dict(self):
        obj = json.loads('{"foo": {"dog": {"layer3": "val"} } }')
        self.check_payload(obj, "foo[dog][layer3]=val")

    def test_dict_with_array(self):
        obj = json.loads('{"foo": ["cat", "dog"] }')
        self.check_payload(obj, "foo[0]=cat&foo[1]=dog")

    # integer
    def test_dict_with_an_integer_as_value(self):
        obj = json.loads('{"foo": 100}')
        self.check_payload(obj, "foo=100")

    def test_dict_with_both_str_and_integer_as_values(self):
        obj = json.loads('{"foo": 100, "bar": "dog"}')
        self.check_payload(obj, "bar=dog&foo=100")

    def test_dict_with_dict_and_integer_as_values(self):
        obj = json.loads('{"foo": 100, "bar": {"dog": "cool", "cat": 10} }')
        self.check_payload(obj, "bar[cat]=10&bar[dog]=cool&foo=100")

    def test_dict_with_integer_and_array_as_values(self):
        obj = json.loads('{"foo": 100, "bar": ["dog", "cat", 99] }')
        self.check_payload(obj, "bar[0]=dog&bar[1]=cat&bar[2]=99&foo=100")

    # double
    def test_dict_with_double(self):
        obj = json.loads('{"foo":1.01}')
        self.check_payload(obj, "foo=1.01")

    # single value
    def test_single_value_string_should_throw(self):
        self.assertRaises(
            ValueError,
            self.check_payload, "foo", ""
        )

    def test_single_value_integer_should_throw(self):
        self.assertRaises(
            ValueError,
            self.check_payload, 10, ""
        )

    def test_single_value_float_should_throw(self):
        self.assertRaises(
            ValueError,
            self.check_payload, 1.01, ""
        )