# -*- coding: utf-8 -*-

import time

def print_numbers():
    for i in range(1, 11):
        print("Number {}".format(i))
        time.sleep(0.5)

def print_letters():
    for letter in 'abcdefghij':
        print("Letter {}".format(letter))
        time.sleep(1)

# 함수 순차 실행
print_numbers()
print_letters()

print("Done!")
