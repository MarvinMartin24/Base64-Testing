import base64_encode from encoder.base64
import ceil from math
import unittest

allow_character = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=')
tc = unittest.TestCase('__init__')


def test_base64_encode_character():
    encode = base64_encode("DevOps")
    for char in encode:
        tc.assertIn(char, allow_character)

def test_base64_encode_size():
    str = "DevOps"
    req_base64_size = math.ceil(len(str) / 3) * 4
    encode = base64_encode(str)
    tc.assertEqual(len(encode), req_base64_size)
