class Book:
    has_text = True
    page_material = 'бумага'

    def __init__(self, title, author, count_page, ISBN, reservation_flag):
        self.title = title
        self.author = author
        self.count_page = count_page
        self.ISBN = ISBN
        self.reservation_flag = reservation_flag

    def info_about_book(self):
        if self.reservation_flag:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                  f'материал: {self.page_material}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                  f'материал: {self.page_material}')


class SchoolBook(Book):

    def __init__(self, title, author, count_page, ISBN, reservation_flag, item, group, availability_of_task):
        super().__init__(title, author, count_page, ISBN, reservation_flag)
        self.item = item
        self.group = group
        self.availability_of_task = availability_of_task

    def info_about_book_school(self):
        if self.reservation_flag:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                  f'предмет: {self.item}, класс: {self.group}, зарезервирована')
        else:
            print(f'Название: {self.title}, Автор: {self.author}, страниц: {self.count_page}, '
                  f'предмет: {self.item}, класс: {self.group}')


school_book_a = SchoolBook('Алгебра', 'Иванов', 200, 300,
                           False, 'Математика', 9, True)
school_book_b = SchoolBook('Геометрия', 'Ткачук', 300, 400,
                           False, 'Математика', 9, True)

school_book_a.reservation_flag = True

school_book_a.info_about_book_school()
school_book_b.info_about_book_school()
