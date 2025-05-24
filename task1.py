numbers = [
    2, -93, -2, 8, None, -44, -1, -85, -14,
    90, -22, -90, -100, -8, 38, -92, -45,
    67, 53, 25
]

# Находим индекс None
none_index = numbers.index(None)

# Вычисляем сумму всех элементов, кроме None
sum_without_none = sum(num for num in numbers if num is not None)

# Количество элементов (включая None)
count = len(numbers)

# Среднее арифметическое
average = sum_without_none / count

# Заменяем None на среднее
numbers[none_index] = average

print("Измененный список:", numbers)
