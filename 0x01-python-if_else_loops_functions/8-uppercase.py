#!/usr/bin/python3
def uppercase(str):
    for c in str:
        i = ord(c)
        print("{}".format((i >= 97 and i <= 122) and chr(i - 32) or c), end='')
    print()
