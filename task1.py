import csv
import json

INPUT_FILENAME = "input.csv"  # Имя входного CSV-файла
OUTPUT_FILENAME = "output.json"  # Имя выходного JSON-файла


def task() -> None:
    # Чтение данных из CSV
    with open(INPUT_FILENAME, 'r', encoding='utf-8') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = [row for row in csv_reader]  # Преобразование в список словарей

    # Запись данных в JSON
    with open(OUTPUT_FILENAME, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4, ensure_ascii=False)  # Форматированный вывод


if __name__ == '__main__':
    # Проверка работы функции
    task()

    # Вывод содержимого JSON-файла для проверки
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
