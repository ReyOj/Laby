from task1 import Tree, Book, Stack

if __name__ == "__main__":
    tree = Tree(height=3.5, age=5, kind="Pine")
    book = Book(title="Python 101", author="Guido", rating=4.5)
    stack = Stack(max_size=3)

    try:
        stack.push("не число")
    except TypeError:
        print("Ошибка: неправильные данные")

    try:
        book.update_rating(10.0)
    except ValueError:
        print("Ошибка: неправильные данные")

    try:
        tree.grow(-2)
    except ValueError:
        print("Ошибка: неправильные данные")
