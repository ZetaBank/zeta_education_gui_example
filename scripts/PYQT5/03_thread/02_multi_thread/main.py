# -*- coding: utf-8 -*-

import threading
import time

def print_numbers():
    for i in range(1, 11):
        print("Number {}".format(i))
        time.sleep(0.5)

def print_letters():
    for letter in 'abcdefghij':
        print("Letter {}".format(letter))
        time.sleep(1)

# 두 개의 스레드 생성
thread1 = threading.Thread(target=print_numbers)
thread2 = threading.Thread(target=print_letters)

# 스레드 시작
thread1.start()
thread2.start()

# 주 스레드에서 두 스레드가 종료될 때까지 기다림
thread1.join()
thread2.join()

print("Done!")
