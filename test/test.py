import base64_encode from encoder.base64
import unittest

allow_character = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=')
tc = unittest.TestCase('__init__')


def test_base64_encode_character():
    encode = base64_encode("DevOps")
    for char in encode:
        tc.assertIn(char, allow_character)
