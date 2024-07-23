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


book_a = Book('Идиот', 'Достоевский', 500, 256, False)
book_b = Book('Война и мир', 'Толстой', 1300, 100, False)
book_c = Book('Одиссея', 'Гамер', 312, 200, False)
book_d = Book('Над пропастью во ржи', 'Сэелинджер', 272, 400, False)
book_e = Book('Унесенные ветром', 'Митчелл', 640, 121, False)

book_a.reservation_flag = True

book_a.info_about_book()
book_b.info_about_book()
book_c.info_about_book()
book_d.info_about_book()
book_e.info_about_book()
