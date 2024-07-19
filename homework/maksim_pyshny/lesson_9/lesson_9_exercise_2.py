temperatures = [20, 15, 32, 34, 21, 19, 25, 27, 30, 32, 34, 30, 29, 25, 27, 22, 22, 23, 25, 29, 29,
                31, 33, 31, 30, 32, 30, 28, 24, 23]

hot_days = filter(lambda x: x > 28, temperatures)
list_hot_days = list(hot_days)

average_temperature = sum(list_hot_days) // len(list_hot_days)

print('Жаркие дни ', list_hot_days)
print('Самая высокая температура ',max(list_hot_days))
print('Самая низкая температура ', min(list_hot_days))
print('Средняя температура ', average_temperature)
