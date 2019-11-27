
import math
import unittest
from encoder.main import base64_encode, string_to_binary
tc = unittest.TestCase('__init__')


allow_character = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789/+=')
allow_binary = set('01')


def test_base64_encode_character():
    encode = base64_encode("DevOps")
    for char in encode:
        tc.assertIn(char, allow_character)

def test_base64_encode_size():
    str = "DevOps"
    req_base64_size = math.ceil(len(str) / 3) * 4
    encode = base64_encode(str)
    tc.assertEqual(len(encode), req_base64_size)

def test_base64_encode_example():
    encode = base64_encode("*->DevOps<-*")
    tc.assertEqual(encode, "Ki0+RGV2T3BzPC0q")

def test_bin_utf8():
    binary = string_to_binary("Hello DevOps\n")
    tc.assertEqual(len(binary)%8, 0 )
    for bin in binary:
        tc.assertIn(bin, allow_binary)
