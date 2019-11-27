import math

character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

def decimalToBinary(n):
    return bin(n).replace("0b", "")

def binaryToDecimal(n):
    return int(n,2)

def string_to_binary(str):
    list = []
    for i in str:
        res = decimalToBinary(ord(i))
        if (len(res) < 8):
            for i in range(0, 8-len(res)):
                res = "0" + res
        list.append(res)
    return (''.join(list))

def group_bytes6(str):
    list = []
    nb_bits = len(str)
    if(nb_bits % 6 == 0):
        for i in range(0, nb_bits, 6):
            list.append(str[i:i+6])
    else:
        nb_bits_quotient = nb_bits//6
        new_len = (math.ceil(nb_bits/6)+1)*6
        for k in range(nb_bits_quotient+1, new_len, 6):
            str += "0"

        for y in range(0, new_len, 6):
            list.append(str[y:y+6])

    return list

def base64_bin_to_char(list):
    list2 = []
    for i in list:
        nb = binaryToDecimal(i)
        if (nb != 0):
            list2.append(character[nb])
        else:
            list2.append("=")
    return (''.join(list2))

def base64_encode(str):
    base64_group6 = group_bytes6(string_to_binary(str))
    return base64_bin_to_char(base64_group6)
