def calc_decorator(func):

    def wrapper(first, second):
        if first == second:
            operation = '+'
        elif first > second:
            operation = '-'
        elif second > first and second != 0:
            operation = '/'
        elif second < 0 or first < 0:
            operation = '*'

        return func(first, second, operation)

    return wrapper


number_1 = int(input('Enter first number: '))
number_2 = int(input('Enter second number: '))


@calc_decorator
def calc(first, second, operation):
    if operation == '+':
        return first + second
    elif operation == '-':
        return first - second
    elif operation == '/':
        return first / second
    elif operation == '*':
        return first * second


result = calc(number_1, number_2)
print(result)
