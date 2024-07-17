import sys

sys.set_int_max_str_digits(100000)


def fibonacci_sequence_generator():
    num = 0
    n = 1
    while True:
        yield num
        num, n = n, num + n


count = 1

for number in fibonacci_sequence_generator():
    if count == 5:
        print(f'Пятое число: {number}')
    elif count == 200:
        print(f'Двухсотое число: {number}')
    elif count == 1000:
        print(f'Тысячное число: {number}')
    elif count == 100000:
        print(f'Стотысячное число: {number}')
        break
    count += 1
