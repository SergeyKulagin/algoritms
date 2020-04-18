from random import *

alphabet = "abcdefghijklmnopqrstuvwxyz"

def rand_array_sorted(size, p, r):
    i = 0
    res = []
    while i < size:
        number = randint(p, r)
        res = res + [number]
        i = i + 1

    return sorted(res)


def rand_string(size):
    return ''.join(choice(alphabet) for i in range(size))



sign_choice = [["+-", "  "], ["abcdefghijklmnopqrstuvwxyz., /#!123456789"]]


def rand_string_number():
    return choice(choice(choice(sign_choice))) + choice(choice(sign_choice[0])) + str(randint(0, 100000000000000000000000000000)) + ''.join(choice("abcdefghijklmnopqrstuvwxyz., /#!123456789") for i in range(5))


for i in range(1, 1000):
    print('"' + rand_string_number() + '"')

