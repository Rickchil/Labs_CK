def find_first_index(items: list, item_to_find: str) -> int | None:
    """
    Находит индекс первого вхождения элемента в списке.

    Args:
        items: Список для поиска
        item_to_find: Искомый элемент

    Returns:
        Индекс первого вхождения или None, если элемент не найден
    """
    try:
        return items.index(item_to_find)
    except ValueError:
        return None


def main():
    # Тестовые данные
    items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']
    search_items = ['банан', 'груша', 'персик']

    # Поиск и вывод результатов
    for item in search_items:
        item_index = find_first_index(items_list, item)

        if item_index is not None:
            print(f"Первое вхождение товара '{item}' имеет индекс {item_index}.")
        else:
            print(f"Товар '{item}' не найден в списке.")


if __name__ == '__main__':
    main()