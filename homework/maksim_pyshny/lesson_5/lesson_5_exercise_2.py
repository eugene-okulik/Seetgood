result_operation_1 = 'результат операции: 42'
result_operation_2 = 'результат операции: 514'
result_operation_3 = 'результат работы программы: 9'
n = 10

result_operation_1_index = result_operation_1.index(':') + 2
result_operation_2_index = result_operation_2.index(':') + 2
result_operation_3_index = result_operation_3.index(':') + 2

number_1 = int(result_operation_1[result_operation_1_index:])
number_2 = int(result_operation_2[result_operation_2_index:])
number_3 = int(result_operation_3[result_operation_3_index:])

sum_number_1 = number_1 + n
sum_number_2 = number_2 + n
sum_number_3 = number_3 + n

print(sum_number_1, sum_number_2, sum_number_3)  # Если имелось ввиду результат слоежния каждого из полученных чисел
print(sum_number_1 + sum_number_2 + sum_number_3)  # Если имелся ввиду итоговый результат сложения полученных трех чисел
