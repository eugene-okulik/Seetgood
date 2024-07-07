students = ['Ivanov', 'Petrov', 'Sidorov']
subjects = ['math', 'biology', 'geography']

students_text = ', '.join(students)
subjects_text = ', '.join(subjects)

print(f'Students {students_text} study these subjects: {subjects_text}')
print('Students', ', '.join(students), 'study these subjects:', ', '.join(subjects))  # Еще один способ вывода строки
