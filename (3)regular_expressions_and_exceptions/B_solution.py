import re
import random

def check(c):
    if c >= 'a' and c <= 'z':
        return True
    if c >= 'A' and c <= 'Z':
        return True
    if c >= 'А' and c <= 'Я':
        return True
    if c >= 'а' and c <= 'я':
        return True
    return False
def prepare_to_british_scientists(text, letters_to_shuffle_nm):
    if letters_to_shuffle_nm <= 1:
        return text
    lst = list(text)
    for i in range(len(lst)):
        can = True
        for j in range(i, i + letters_to_shuffle_nm + 2):
            if not check(lst[j]):
                can = False
                break
        if can is True:
            lst[i + 1], lst[i + 2] = lst[i + 2], lst[i + 1]
            break
    return ''.join(lst)