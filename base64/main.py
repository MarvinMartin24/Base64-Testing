import math

character = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"

############### Binary - Decimal ##############

def decimal_to_binary(n):
    return bin(n).replace("0b", "")

def binary_to_decimal(n):
    return int(n,2)

def string_to_binary(str):
    list = []
    for i in str:
        res = decimal_to_binary(ord(i))
        if (len(res) < 8):
            for i in range(0, 8-len(res)):
                res = "0" + res
        list.append(res)
    return (''.join(list))

################## Encoder ######################

def group_bytes6(str):
    list = []
    bin = string_to_binary(str)
    nb_bits = len(bin)
    if(nb_bits % 6 == 0):
        for i in range(0, nb_bits, 6):
            list.append(bin[i:i+6])
    else:
        nb_bits_quotient = nb_bits//6
        new_len = int(math.ceil(len(str)/3)*24)
        for k in range(nb_bits, new_len, 1):
            bin += "0"

        for y in range(0, new_len, 6):
            list.append(bin[y:y+6])
    return [list,int(math.ceil(nb_bits/6))]

def base64_encode_bin_to_char(list):
    list2 = []
    for i in range (0, list[1]):
        nb = binary_to_decimal(list[0][i])
        list2.append(character[nb])
    if (len(list[0]) != len(list2)):
        for i in range(len(list[0])-len(list2)):
            list2.append("=")
    return (''.join(list2))

def base64_encode(str):
    base64_group6 = group_bytes6(str)
    return base64_encode_bin_to_char(base64_group6)


################## Decoder ######################

def base64_str_to_bin(str):
    dec_list = []
    bin_list = []

     # from string to base64 decimal values
    for i in str:
        if(i != '='):
            dec = character.index(i)
            dec_list.append(dec)

     # from base64 decimal values to binary
    for y in dec_list:
        bin = decimal_to_binary(y)
        if (len(bin) < 6):
            for i in range(0, 6-len(bin)):
                bin = "0" + bin
        bin_list.append(bin)
    return (''.join(bin_list))

def group_bytes8(bin):
    list = []
    nb_bits = len(bin)
    if(nb_bits % 8 == 0):
        for i in range(0, nb_bits, 8):
            list.append(bin[i:i+8])
    else:
        nb_bits_quotient = nb_bits//8
        for y in range(0, nb_bits_quotient*8, 8):
            list.append(bin[y:y+8])
    return list

def base64_decode_bin_to_char(list):
    dec_list = []
    char_list = []

    for bin in list:
        dec_list.append(binary_to_decimal(bin))

    for dec in dec_list:
        char_list.append(chr(dec))
    return (''.join(char_list))

def base64_decode(str):
    base64_group8 = group_bytes8(base64_str_to_bin(str))
    return base64_decode_bin_to_char(base64_group8)
