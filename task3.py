# Константы для расчета размера книги
PAGES = 100
LINES_PER_PAGE = 50
CHARS_PER_LINE = 25
BYTES_PER_CHAR = 4

# Константа размера дискеты в байтах (1.44 МБ)
DISKETTE_SIZE_BYTES = 1.44 * 1024 * 1024

# Вычисление общего объема книги
total_chars = PAGES * LINES_PER_PAGE * CHARS_PER_LINE
book_size_bytes = total_chars * BYTES_PER_CHAR

# Расчет количества книг на дискете
num_books = int(DISKETTE_SIZE_BYTES // book_size_bytes)

print(f"Количество книг, помещающихся на дискету: {num_books}")
