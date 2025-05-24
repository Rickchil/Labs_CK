def find_common_participants(group1: str, group2: str, sep: str = ',') -> list:
    """
    Находит общих участников в двух группах.

    Args:
        group1: Первая группа участников (строка с разделителями)
        group2: Вторая группа участников (строка с разделителями)
        sep: Разделитель в строках (по умолчанию запятая)

    Returns:
        Отсортированный список общих участников
    """
    # Разделяем строки на списки участников
    participants1 = group1.split(sep)
    participants2 = group2.split(sep)

    # Находим пересечение множеств
    common_participants = set(participants1) & set(participants2)

    # Возвращаем отсортированный результат
    return sorted(common_participants)


def main():
    # Тестовые данные
    first_group = "Иванов|Петров|Сидоров"
    second_group = "Петров|Сидоров|Смирнов"

    # Находим общих участников с разделителем |
    common = find_common_participants(
        group1=first_group,
        group2=second_group,
        sep='|'
    )

    # Выводим результат
    print("Общие участники:", common)


if __name__ == '__main__':
    main()