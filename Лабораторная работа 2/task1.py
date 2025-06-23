BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


class Book:
    def __init__(self, id_: int, name: str, pages: int) -> None:
        """
        Инициализация книги.

        :param id_: Идентификатор книги
        :param name: Название книги
        :param pages: Количество страниц
        """
        self.id = id_
        self.name = name
        self.pages = pages

    def __str__(self) -> str:
        """
        Строковое представление книги.

        :return: строка формата Книга "название_книги"
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Представление книги для отладки и воссоздания объекта.

        :return: строка вида Book(id_=1, name='test_name_1', pages=200)
        """
        return f"Book(id_={self.id}, name={repr(self.name)}, pages={self.pages})"


if __name__ == '__main__':
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)

    print(list_books)
