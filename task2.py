import json


def task() -> float:
    """
    Вычисляет взвешенную сумму оценок из JSON-файла.
    Возвращает результат, округлённый до 3 знаков после запятой.
    """
    with open('input.json', 'r') as f:
        data = json.load(f)  # Загружаем данные из JSON-файла

    total = 0.0
    for item in data:
        # Суммируем произведения оценок на их веса
        total += item['score'] * item['weight']

    return round(total, 3)  # Округляем результат до 3 знаков


if __name__ == '__main__':
    print(task())
