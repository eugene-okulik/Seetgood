import os
import datetime


base_path = os.path.dirname(__file__)
homework_path = os.path.dirname(os.path.dirname(base_path))
eugene_okulik_path = os.path.join(homework_path, 'eugene_okulik', 'hw_13', 'data.txt')


def return_date_lines(file_path):
    with open(file_path, 'r') as data_file:
        for line in data_file:
            list_line = line.split(' - ')
            date_info = list_line[0].split('. ')
            record_number = int(date_info[0])
            date_string = date_info[1]

            date = datetime.datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S.%f")
            if record_number == 1:
                new_date = date + datetime.timedelta(weeks=1)
                print(new_date)
            elif record_number == 2:
                day_of_week = date.strftime("%A")
                print(day_of_week)
            elif record_number == 3:
                current_date = datetime.datetime.now()
                days_ago = (current_date - date).days
                print(days_ago)


return_date_lines(eugene_okulik_path)
