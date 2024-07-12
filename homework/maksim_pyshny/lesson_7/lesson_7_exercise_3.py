def result_operation(result_input, n):
    split_result = result_input.split()
    return int(split_result[-1]) + n


result_operation_1 = 'результат операции: 42'
result_operation_2 = 'результат операции: 514'
result_operation_3 = 'результат работы программы: 9'
result_operation_4 = 'результат: 2'
n = 10

print(result_operation(result_operation_1, n))
print(result_operation(result_operation_2, n))
print(result_operation(result_operation_3, n))
print(result_operation(result_operation_4, n))
