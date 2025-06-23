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


class Library:
    def __init__(self, books: list[Book] = None) -> None:
        """
        Инициализация библиотеки.

        :param books: список книг (по умолчанию пустой)
        """
        if books is None:
            books = []
        self.books = books

    def get_next_book_id(self) -> int:
        """
        Возвращает следующий доступный идентификатор для новой книги.

        :return: целое число (1, если книг нет; иначе max id + 1)
        """
        if not self.books:
            return 1
        return max(book.id for book in self.books) + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги в списке по её id.

        :param book_id: идентификатор книги
        :return: индекс в списке self.books
        :raises ValueError: если книга с таким id не найдена

        >>> lib = Library([Book(1, "A", 100), Book(2, "B", 200)])
        >>> lib.get_index_by_book_id(2)
        1
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()
    print(empty_library.get_next_book_id())

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)
    print(library_with_books.get_next_book_id())

    print(library_with_books.get_index_by_book_id(1))
