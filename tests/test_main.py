
import math
import unittest
sys.path.insert(0, base64)


from base64.main import base64_encode, string_to_binary, base64_decode
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

def test_base64_decode_example():
    decode = base64_decode("Ki0+RGV2T3BzPC0q")
    tc.assertEqual(decode, "*->DevOps<-*")


def test_base64_encode_to_decode():
    encode = base64_encode("<azert1AZERT>99")
    decode = base64_decode(encode)
    tc.assertEqual(decode, "<azert1AZERT>99")
