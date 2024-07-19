import datetime


my_date = 'Jan 15, 2023 - 12:05:33'

my_date_python = datetime.datetime.strptime(my_date, '%b %d, %Y - %H:%M:%S')
full_month_name = my_date_python.strftime('%B')
new_date = my_date_python.strftime('%d.%m.%Y, %H:%M')

print(my_date_python)
print(full_month_name)
print(new_date)
