import string
import re


def strings(filename, min_str_len = 4):
    min_str_len += 1
    f = open(filename, "rb")
    for byte_str in f:
        s = ''.join(list(map(chr, list(byte_str))))
        patt = re.compile("[" + string.printable + "]{" + str(min_str_len) + ",}")
        lst = patt.findall(s)
        yield from lst
