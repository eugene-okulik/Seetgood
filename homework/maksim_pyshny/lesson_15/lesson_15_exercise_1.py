import mysql.connector as mysql


db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Создание студента
student_query = "INSERT INTO students (name, second_name, group_id) VALUES (%s, %s, %s)"
student_values = ('DwaynePython', 'JohnsonPython', None)
cursor.execute(student_query, student_values)
student_id = cursor.lastrowid
print(f'Student id: {student_id}')

# Создание книг и указание, что ранее созданный студент их взял
book_query = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
book_value = [
    ('Robinson Crusoe', student_id),
    ('The Great Gatsby', student_id)
]
cursor.executemany(book_query, book_value)

# Создание группы
group_query = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
group_values = ('WrestlingPython', '01-07-2024', '31-07-2024')
cursor.execute(group_query, group_values)
group_id = cursor.lastrowid
print(f'Group id: {group_id}')

# Распределение ранее созданного студента в группу которую мы создали
update_group_query = "UPDATE students SET group_id = %s WHERE id = %s"
update_group_value = (group_id, student_id)
cursor.execute(update_group_query, update_group_value)

# Создание нескольких учебных предметов
subjet_query_1 = "INSERT INTO subjets (title) VALUES (%s)"
subjet_value_1 = ('C#',)
cursor.execute(subjet_query_1, subjet_value_1)
subjet_id_1 = cursor.lastrowid
print(f'Subjet 1 id: {subjet_id_1}')

subjet_query_2 = "INSERT INTO subjets (title) VALUES (%s)"
subjet_value_2 = ('Swift',)
cursor.execute(subjet_query_2, subjet_value_2)
subjet_id_2 = cursor.lastrowid
print(f'Subjet 2 id: {subjet_id_2}')

# Создание по 2 занятия для созданных выше предметов
lesson_query_1 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_1 = ('Functions', subjet_id_1)
cursor.execute(lesson_query_1, lesson_value_1)
lesson_id_1 = cursor.lastrowid
print(f'Lesson 1 id: {lesson_id_1}')

lesson_query_2 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_2 = ('Classes', subjet_id_1)
cursor.execute(lesson_query_2, lesson_value_2)
lesson_id_2 = cursor.lastrowid
print(f'Lesson 2 id: {lesson_id_2}')

lesson_query_3 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_3 = ('Specific Errors', subjet_id_2)
cursor.execute(lesson_query_3, lesson_value_3)
lesson_id_3 = cursor.lastrowid
print(f'Lesson 3 id: {lesson_id_3}')

lesson_query_4 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
lesson_value_4 = ('Throwing Exceptions', subjet_id_2)
cursor.execute(lesson_query_4, lesson_value_4)
lesson_id_4 = cursor.lastrowid
print(f'Lesson 4 id: {lesson_id_4}')

# Выставление отметок
marks_query = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
marks_value = [
    ('9', lesson_id_1, student_id),
    ('8', lesson_id_2, student_id),
    ('7', lesson_id_3, student_id),
    ('9', lesson_id_4, student_id)
]
cursor.executemany(marks_query, marks_value)

db.commit()

# Получение всех оценок созданного студента
marks_my_student_query = '''
SELECT students.name, students.second_name, marks.value, marks.lesson_id
FROM students LEFT JOIN marks ON students.id = marks.student_id WHERE students.id = %s
'''
cursor.execute(marks_my_student_query, (student_id,))
data_marks = cursor.fetchall()
print(f"All student's marks: {data_marks}")

# Вывести все книги, которые есть у созданного студента
book_my_stydent_query = '''
SELECT students.name, students.second_name, books.title
FROM students LEFT JOIN books ON students.id = books.taken_by_student_id  WHERE students.id = %s
'''
cursor.execute(book_my_stydent_query, (student_id,))
data_books = cursor.fetchall()
print(f"All student's books: {data_books}")

# Вывести для созданного студента все, что есть в базе
all_info_my_stydent_query = '''
SELECT students.name, students.second_name, `groups`.title, `groups`.start_date, `groups`.end_date,
subjets.title, lessons.title, marks.value
FROM students
LEFT JOIN `groups` ON students.group_id = `groups`.id
LEFT JOIN marks ON students.id = marks.student_id
LEFT JOIN lessons ON marks.lesson_id = lessons.id
LEFT JOIN subjets ON lessons.subject_id = subjets.id
LEFT JOIN books ON students.id = books.taken_by_student_id
WHERE students.id = %s
'''
cursor.execute(all_info_my_stydent_query, (student_id,))
data_all_info = cursor.fetchall()
print(f"Student's all info: {data_all_info}")

db.close()
