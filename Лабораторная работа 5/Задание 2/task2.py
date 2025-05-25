from task_1 import Book, Car, BankAccount


def main():
    """Основная функция для демонстрации работы классов."""
    # Создаем объекты каждого класса
    book = Book("1984", "George Orwell", 200)
    car = Car("Toyota", "Camry", 50.0)
    account = BankAccount("Alice", 1000.0)

    # Проверяем обработку ошибок в методах
    test_error_handling(book, car, account)



def test_error_handling(book, car, account):
    """Тестирование обработки ошибок."""
    try:
        # Попытка создать книгу с отрицательным количеством страниц
        Book("Ошибка", "Автор", -10)
    except ValueError as e:
        print(f'Ошибка в Book: {e}')

    try:
        # Попытка проехать отрицательное расстояние
        car.drive(-100)
    except ValueError as e:
        print(f'Ошибка в Car.drive(): {e}')

    try:
        # Попытка снять отрицательную сумму
        account.withdraw(-500)
    except ValueError as e:
        print(f'Ошибка в BankAccount.withdraw(): {e}')


if __name__ == "__main__":
    main()