from typing import Dict


def count_letters(text: str) -> Dict[str, int]:
    """
    Подсчитывает количество вхождений каждой буквы в тексте.

    Args:
        text: Анализируемый текст

    Returns:
        Словарь с количеством вхождений каждой буквы (ключ - буква, значение - количество)
    """
    letter_counts = {}
    for char in text.lower():
        if char.isalpha():
            letter_counts[char] = letter_counts.get(char, 0) + 1
    return letter_counts


def calculate_frequency(letter_counts: Dict[str, int]) -> Dict[str, float]:
    """
    Вычисляет частоту встречаемости букв в тексте.

    Args:
        letter_counts: Словарь с количеством вхождений букв

    Returns:
        Словарь с частотой встречаемости каждой буквы (ключ - буква, значение - частота)
    """
    total = sum(letter_counts.values())
    return {letter: round(count / total, 2) for letter, count in letter_counts.items()}


def print_frequencies(frequencies: Dict[str, float]) -> None:
    """
    Выводит частоты букв в отсортированном порядке.

    Args:
        frequencies: Словарь с частотами букв
    """
    for letter, freq in sorted(frequencies.items()):
        print(f"{letter}: {freq}")


def main():
    poem = """
    У лукоморья дуб зелёный;
    Златая цепь на дубе том:
    И днём и ночью кот учёный
    Всё ходит по цепи кругом;
    Идёт направо — песнь заводит,
    Налево — сказку говорит.
    Там чудеса: там леший бродит,
    Русалка на ветвях сидит;
    Там на неведомых дорожках
    Следы невиданных зверей;
    Избушка там на курьих ножках
    Стоит без окон, без дверей;
    Там лес и дол видений полны;
    Там о заре прихлынут волны
    На брег песчаный и пустой,
    И тридцать витязей прекрасных
    Чредой из вод выходят ясных,
    И с ними дядька их морской;
    Там королевич мимоходом
    Пленяет грозного царя;
    Там в облаках перед народом
    Через леса, через моря
    Колдун несёт богатыря;
    В темнице там царевна тужит,
    А бурый волк ей верно служит;
    Там ступа с Бабою Ягой
    Идёт, бредёт сама собой,
    Там царь Кащей над златом чахнет;
    Там русский дух… там Русью пахнет!
    И там я был, и мёд я пил;
    У моря видел дуб зелёный;
    Под ним сидел, и кот учёный
    Свои мне сказки говорил.
    """

    counts = count_letters(poem)
    frequencies = calculate_frequency(counts)
    print_frequencies(frequencies)


if __name__ == '__main__':
    main()