import os
import time


def check_time(filename):
    start_time = time.time()
    for _ in range(100):
        os.system(filename)
    return time.time() - start_time


print(f"Время выполнения исходной программы: {check_time('lab4_1.py')}")
print(f"Время выполнения программы с библиотекой json: {check_time('lab4_2.py')}")
print(f"Время выполнения программы с компилированными регулярными выражениями: {check_time('lab4_3.py')}")
