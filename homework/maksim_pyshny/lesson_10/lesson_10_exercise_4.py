PRICE_LIST = '''тетрадь 50р
книга 200р
ручка 100р
карандаш 70р
альбом 120р
пенал 300р
рюкзак 500р'''

my_list = PRICE_LIST.split()
new_my_list_1 = [x for x in my_list[0::2]]
new_my_list_2 = [int(x.replace('р', '')) for x in my_list[1::2]]

my_dict = dict(zip(new_my_list_1, new_my_list_2))

print(new_my_list_1)
print(new_my_list_2)
print(my_dict)
