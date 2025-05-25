class Book:
    """Базовый класс книги."""

    def __init__(self, name: str, author: str):
        """
        Инициализация книги.

        Args:
            name: Название книги
            author: Автор книги
        """
        self._name = name
        self._author = author

    @property
    def name(self) -> str:
        """Возвращает название книги."""
        return self._name

    @property
    def author(self) -> str:
        """Возвращает автора книги."""
        return self._author

    def __str__(self) -> str:
        """Строковое представление книги."""
        return f"Книга {self.name}. Автор {self.author}"

    def __repr__(self) -> str:
        """Официальное строковое представление книги."""
        return f"{self.__class__.__name__}(name={self.name!r}, author={self.author!r})"


class PaperBook(Book):
    """Класс бумажной книги."""

    def __init__(self, name: str, author: str, pages: int):
        """
        Инициализация бумажной книги.

        Args:
            name: Название книги
            author: Автор книги
            pages: Количество страниц
        """
        super().__init__(name, author)
        self.pages = pages

    @property
    def pages(self) -> int:
        """Возвращает количество страниц."""
        return self._pages

    @pages.setter
    def pages(self, value: int):
        """
        Устанавливает количество страниц.

        Args:
            value: Количество страниц

        Raises:
            TypeError: Если значение не целое число
            ValueError: Если значение <= 0
        """
        if not isinstance(value, int):
            raise TypeError("Количество страниц должно быть целым числом")
        if value <= 0:
            raise ValueError("Количество страниц должно быть положительным")
        self._pages = value

    def __repr__(self) -> str:
        """Официальное строковое представление бумажной книги."""
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, pages={self.pages!r})")


class AudioBook(Book):
    """Класс аудиокниги."""

    def __init__(self, name: str, author: str, duration: float):
        """
        Инициализация аудиокниги.

        Args:
            name: Название книги
            author: Автор книги
            duration: Продолжительность в часах
        """
        super().__init__(name, author)
        self.duration = duration

    @property
    def duration(self) -> float:
        """Возвращает продолжительность аудиокниги."""
        return self._duration

    @duration.setter
    def duration(self, value: float):
        """
        Устанавливает продолжительность аудиокниги.

        Args:
            value: Продолжительность в часах

        Raises:
            TypeError: Если значение не число
            ValueError: Если значение <= 0
        """
        if not isinstance(value, (int, float)):
            raise TypeError("Продолжительность должна быть числом")
        if value <= 0:
            raise ValueError("Продолжительность должна быть положительной")
        self._duration = float(value)

    def __repr__(self) -> str:
        """Официальное строковое представление аудиокниги."""
        return (f"{self.__class__.__name__}(name={self.name!r}, "
                f"author={self.author!r}, duration={self.duration!r})")