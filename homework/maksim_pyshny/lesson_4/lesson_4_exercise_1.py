my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': [6, 7, 8, 9, 10],
    'dict': {
        'key1': 'value1',
        'key2': 'value2',
        'key3': 'value3',
        'key4': 'value4',
        'key5': 'value5'
    },
    'set': {11, 12, 13, 14, 15}
}

# Работа с ключом 'tuple':
my_tuple = my_dict['tuple']
print(my_tuple[-1])

# Работа с ключом 'list':
my_dict['list'].append(100)
my_dict['list'].pop(1)

# Работа с ключом 'dict':
my_dict['dict'].update({('i am a tuple', ): 'new key'})
my_dict['dict'].pop('key1')

# Работа с ключом 'set':
my_dict['set'].add(300)
my_dict['set'].remove(15)

# Вывод на экран
print(my_dict)
