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
    """Класс, описывающий книгу."""

    def __init__(self, id_: int, name: str, pages: int):
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
        Возвращает строковое представление книги.

        :return: Строка формата 'Книга "название_книги"'
        """
        return f'Книга "{self.name}"'

    def __repr__(self) -> str:
        """
        Возвращает строку для инициализации идентичного экземпляра.

        :return: Строка формата "Book(id_=1, name='test_name_1', pages=200)"
        """
        return f"Book(id_={self.id}, name='{self.name}', pages={self.pages})"


class Library:
    """Класс, описывающий библиотеку книг."""

    def __init__(self, books: list[Book] = None):
        """
        Инициализация библиотеки.

        :param books: Список книг (по умолчанию None)
        """
        self.books = books if books is not None else []

    def get_next_book_id(self) -> int:
        """
        Возвращает идентификатор для добавления новой книги.

        :return: 1, если книг нет, либо id последней книги + 1
        """
        if not self.books:
            return 1
        return self.books[-1].id + 1

    def get_index_by_book_id(self, book_id: int) -> int:
        """
        Возвращает индекс книги по её id.

        :param book_id: Идентификатор книги
        :return: Индекс книги в списке
        :raises ValueError: Если книги с указанным id не существует
        """
        for index, book in enumerate(self.books):
            if book.id == book_id:
                return index
        raise ValueError("Книги с запрашиваемым id не существует")


if __name__ == '__main__':
    empty_library = Library()  # Инициализируем пустую библиотеку
    print(empty_library.get_next_book_id())  # Проверяем следующий id для пустой библиотеки

    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"])
        for book_dict in BOOKS_DATABASE
    ]
    library_with_books = Library(books=list_books)  # Инициализируем библиотеку с книгами
    print(library_with_books.get_next_book_id())  # Проверяем следующий id для непустой библиотеки

    print(library_with_books.get_index_by_book_id(1))  # Проверяем индекс книги с id = 1