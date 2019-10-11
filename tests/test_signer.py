import unittest
import json

from satang_pro_signer import signer

class SignerTest(unittest.TestCase):
    def check_sign(self, obj, expected: bytes, key: bytes = bytes.fromhex('8781e58f94f8b2a58b6aa30649fd6a46')):
        result = signer.Signer(key).sign(obj)
        self.assertEqual(expected, result)

    def test_sign_empty(self):
        self.check_sign(None, bytes.fromhex("6c9ceae52583980dbe65487dc7f5a2b36865c8f17eeab5841e979b35e75f54335b1c5076352d5a38c60e256848b508766a6cc3e49bb8a880e7187c086f3be49e"))

    def test_sign_dict_with_one_key(self):
        obj = json.loads('{"foo":"bar"}')
        self.check_sign(obj, bytes.fromhex("8a085f790664ea51401414d73a21b5d1f3bbda855246286c5c960a6f9919251bd7cefcb43084c67c7aec490bb051364d4e18678c946ed00109408c3d7ed2ad43"))

    def test_sign_dict_with_multiple_keys(self):
        obj = json.loads('{"foo":"bar", "dog": 99}')
        self.check_sign(obj, bytes.fromhex("e82294234e22f42d695600cda19af923a4acf53945860dcbf4af54ec2c4b5e18b023a5894cb7f010752d13c1a14da5ca22d1c769dfc5ad271caeadeabf30450a"))

    def test_sign_dict_with_double(self):
        obj = json.loads('{"foo":"bar", "dog": 99, "cat": 10.00014}')
        self.check_sign(obj, bytes.fromhex("f81938dfdd4f30244f0e242856d7be1471f4d9d75a44cba696415bf17479d80a9b511c20698d219996718bd4b1ed37538d0e0dadbbe09e280a0c0e438a1e6304"))

