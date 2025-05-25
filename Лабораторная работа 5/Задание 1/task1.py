class Book:
    """Класс, описывающий книгу."""

    def __init__(self, title: str, author: str, pages: int):
        """
        Инициализация книги.

        :param title: Название книги.
        :param author: Автор книги.
        :param pages: Количество страниц (должно быть положительным числом).

        :raises ValueError: Если количество страниц <= 0.

        >>> book = Book("1984", "George Orwell", 200)  # Корректное создание
        >>> book.title
        '1984'
        >>> book.pages
        200
        >>> Book("Test", "Author", 0)  # Некорректное количество страниц
        Traceback (most recent call last):
            ...
        ValueError: Количество страниц должно быть положительным числом.
        """
        if pages <= 0:
            raise ValueError("Количество страниц должно быть положительным числом.")
        self.title = title
        self.author = author
        self.pages = pages

    def read(self, pages_to_read: int = 10) -> str:
        """
        Чтение книги.

        :param pages_to_read: Количество страниц для чтения (по умолчанию 10).
        :return: Сообщение о прочитанных страницах.

        :raises ValueError: Если pages_to_read <= 0 или больше, чем осталось страниц.

        >>> book = Book("1984", "George Orwell", 200)
        >>> book.read(20)
        'Прочитано 20 страниц. Осталось 180.'
        >>> book.read(0)
        Traceback (most recent call last):
            ...
        ValueError: Количество страниц для чтения должно быть положительным.
        >>> book.read(200)
        Traceback (most recent call last):
            ...
        ValueError: Нельзя прочитать больше, чем осталось страниц.
        """
        if pages_to_read <= 0:
            raise ValueError("Количество страниц для чтения должно быть положительным.")
        if pages_to_read > self.pages:
            raise ValueError("Нельзя прочитать больше, чем осталось страниц.")
        self.pages -= pages_to_read
        return f"Прочитано {pages_to_read} страниц. Осталось {self.pages}."

    def get_info(self) -> str:
        """
        Возвращает информацию о книге.

        :return: Строка с названием и автором.

        >>> book = Book("1984", "George Orwell", 200)
        >>> book.get_info()
        'Книга "1984", автор: George Orwell'
        """
        return f'Книга "{self.title}", автор: {self.author}'

    if __name__ == "__main__":
        import doctest
        doctest.testmod()


class Car:
    """Класс, описывающий автомобиль."""

    def __init__(self, brand: str, model: str, fuel_level: float):
        """
        Инициализация автомобиля.

        :param brand: Марка автомобиля.
        :param model: Модель автомобиля.
        :param fuel_level: Уровень топлива (должен быть от 0 до 100).

        :raises ValueError: Если уровень топлива вне допустимого диапазона.

        >>> car = Car("Toyota", "Camry", 50.0)  # Корректное создание
        >>> car.brand
        'Toyota'
        >>> car.fuel_level
        50.0
        >>> Car("Tesla", "Model S", 150.0)  # Некорректный уровень топлива
        Traceback (most recent call last):
            ...
        ValueError: Уровень топлива должен быть от 0 до 100.
        """
        if not 0 <= fuel_level <= 100:
            raise ValueError("Уровень топлива должен быть от 0 до 100.")
        self.brand = brand
        self.model = model
        self.fuel_level = fuel_level

    def drive(self, distance: float) -> float:
        """
        Поездка на автомобиле.

        :param distance: Расстояние в км (должно быть > 0).
        :return: Оставшийся уровень топлива.

        :raises ValueError: Если расстояние <= 0 или топлива недостаточно.

        Примеры:
        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.drive(30)  # 50.0 - 30*1.0 = 20.0
        20.0
        >>> car.drive(300)  # 20.0 - 300*1.0 → ошибка
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно топлива для поездки.
        """
        if distance <= 0:
            raise ValueError("Расстояние должно быть положительным.")
        fuel_needed = distance * 1.0  # 1.0 литр на км
        if fuel_needed > self.fuel_level:
            raise ValueError("Недостаточно топлива для поездки.")
        self.fuel_level -= fuel_needed
        return self.fuel_level

    def refuel(self, amount: float = 20.0) -> float:
        """
        Заправка автомобиля.

        :param amount: Количество топлива для заправки (по умолчанию 20.0).
        :return: Новый уровень топлива.

        :raises ValueError: Если amount <= 0 или превышает максимальный уровень.

        >>> car = Car("Toyota", "Camry", 50.0)
        >>> car.refuel(30)
        80.0
        >>> car.refuel(0)
        Traceback (most recent call last):
            ...
        ValueError: Количество топлива должно быть положительным.
        >>> car.refuel(100)
        Traceback (most recent call last):
            ...
        ValueError: Уровень топлива не может превышать 100.
        """
        if amount <= 0:
            raise ValueError("Количество топлива должно быть положительным.")
        new_level = self.fuel_level + amount
        if new_level > 100:
            raise ValueError("Уровень топлива не может превышать 100.")
        self.fuel_level = new_level
        return self.fuel_level

    if __name__ == "__main__":
        import doctest
        doctest.testmod()


class BankAccount:
    """Класс, описывающий банковский счет."""

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Инициализация банковского счета.

        :param owner: Владелец счета.
        :param balance: Начальный баланс (по умолчанию 0.0, не может быть отрицательным).

        :raises ValueError: Если баланс отрицательный.

        >>> account = BankAccount("Alice")  # Баланс по умолчанию
        >>> account.balance
        0.0
        >>> account = BankAccount("Bob", 100.0)  # Корректный баланс
        >>> account.balance
        100.0
        >>> BankAccount("Eve", -50.0)  # Некорректный баланс
        Traceback (most recent call last):
            ...
        ValueError: Баланс не может быть отрицательным.
        """
        if balance < 0:
            raise ValueError("Баланс не может быть отрицательным.")
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> float:
        """
        Пополнение счета.

        :param amount: Сумма для пополнения (должна быть > 0).
        :return: Новый баланс.

        :raises ValueError: Если сумма <= 0.

        >>> account = BankAccount("Alice")
        >>> account.deposit(100)
        100.0
        >>> account.deposit(0)
        Traceback (most recent call last):
            ...
        ValueError: Сумма пополнения должна быть положительной.
        """
        if amount <= 0:
            raise ValueError("Сумма пополнения должна быть положительной.")
        self.balance += amount
        return self.balance

    def withdraw(self, amount: float) -> float:
        """
        Снятие денег со счета.

        :param amount: Сумма для снятия (должна быть > 0 и <= баланса).
        :return: Новый баланс.

        :raises ValueError: Если сумма <= 0 или превышает баланс.

        >>> account = BankAccount("Alice", 200)
        >>> account.withdraw(50)
        150
        >>> account.withdraw(0)
        Traceback (most recent call last):
            ...
        ValueError: Сумма снятия должна быть положительной.
        >>> account.withdraw(200)
        Traceback (most recent call last):
            ...
        ValueError: Недостаточно средств на счете.
        """
        if amount <= 0:
            raise ValueError("Сумма снятия должна быть положительной.")
        if amount > self.balance:
            raise ValueError("Недостаточно средств на счете.")
        self.balance -= amount
        return self.balance
    if __name__ == "__main__":
        import doctest
        doctest.testmod()

