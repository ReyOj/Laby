class Tree:
    def __init__(self, height: float, age: int, kind: str) -> None:
        if height <= 0:
            raise ValueError("Высота не может быть отрицательной")
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.height = height
        self.age = age
        self.kind = kind

    def grow(self, years: int = 1) -> None:
        """
        Увеличивает возраст дерева на заданное количество лет.
        Также увеличивает высоту (по 0.5 м за каждый год).

        :param years: Количество лет роста (должно быть положительным)
        :raises ValueError: если years <= 0

        >>> t = Tree(3.0, 5, "Oak")
        >>> t.grow(2)
        >>> t.age
        7
        >>> t.height
        4.0
        """
        if years <= 0:
            raise ValueError("Возраст не может быть отрицательным")
        self.age += years
        self.height += 0.5 * years

    def is_mature(self) -> bool:
        """
        Проверяет, достигло ли дерево зрелости (>= 10 лет)

        :return: True, если зрелое, иначе False

        >>> Tree(4.5, 12, "Birch").is_mature()
        True
        """
        return self.age >= 10


class Book:
    def __init__(self, title: str, author: str, rating: float) -> None:
        if not (0 <= rating <= 5):
            raise ValueError("Рейтинг должен быть от 0 до 5")
        self.title = title
        self.author = author
        self.rating = rating

    def update_rating(self, new_rating: float) -> None:
        """
        Обновляет рейтинг книги

        :param new_rating: новое значение рейтинга (0-5)
        :raises ValueError: если рейтинг вне допустимых границ

        >>> b = Book("1984", "George Orwell", 4.6)
        >>> b.update_rating(4.9)
        >>> b.rating
        4.9
        """
        if not (0 <= new_rating <= 5):
            raise ValueError("Рейтинг должен быть от 0 до 5")
        self.rating = new_rating

    def full_title(self) -> str:
        """
        Возвращает полное описание книги

        :return: строка вида "Название — Автор"

        >>> Book("1984", "George Orwell", 4.6).full_title()
        '1984 — George Orwell'
        """
        return f"{self.title} — {self.author}"


class Stack:
    def __init__(self, a: int = 1, max_size: int = 100) -> None:
        """
        Стек фиксированной длины.

        :param max_size: максимальное количество элементов (должно быть положительным)
        :raises ValueError: если max_size <= 0
        """
        if max_size <= 0:
            raise ValueError("max_size не может быть отрицательным")
        self.items = []
        self.max_size = max_size

    def push(self, item: int) -> None:
        """
        Добавляет элемент в стек, если он не переполнен.

        :param item: Целое число
        :raises TypeError: если item не int
        :raises OverflowError: если стек полон

        >>> s = Stack(2)
        >>> s.push(1)
        >>> s.push(2)
        >>> s.items
        [1, 2]
        """
        if not isinstance(item, int):
            raise TypeError("Only integers allowed")
        if len(self.items) >= self.max_size:
            raise OverflowError("Stack is full")
        self.items.append(item)

    def pop(self) -> int:
        """
        Удаляет верхний элемент и возвращает его.

        :return: последний элемент
        :raises IndexError: если стек пуст

        >>> s = Stack()
        >>> s.push(5)
        >>> s.pop()
        5
        """
        if not self.items:
            raise IndexError("Pop from empty stack")
        return self.items.pop()

    def is_empty(self) -> bool:
        """
        Проверяет, пуст ли стек.

        :return: True, если стек пуст

        >>> Stack().is_empty()
        True
        """
        return len(self.items) == 0
