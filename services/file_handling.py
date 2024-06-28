import os
import sys

BOOK_PATH = 'book/book.txt'
PAGE_SIZE = 1050

book: dict[int, str] = {}

# Функция, возвращающая строку с текстом и ее размером
def _get_part_text(text: str, start: int, page_size: int) -> tuple[str, int]:
    exepts = '.,;:!?'
    final_size = page_size
    if len(text) < start + page_size:
        final_size = len(text) - start
    else:
        for i in range(start + page_size - 1, start, -1):
            if text[i] in exepts and text[i + 1] not in exepts:
                break
            final_size -= 1
    return text[start: final_size + start], final_size

# Функция, формирующая словарь книги
def prepare_book(path: str) -> None:
    with open(file=path, mode='r', encoding='utf-8') as file:
        content = file.read()
    start = 0
    page_number = 1
    while start < len(content):
        page_text, length = _get_part_text(content, start, PAGE_SIZE)
        if page_text:
            book[page_number] = page_text.strip()
            page_number += 1
            start += length


prepare_book(os.path.join(sys.path[1], os.path.normpath(BOOK_PATH)))
print(book)
