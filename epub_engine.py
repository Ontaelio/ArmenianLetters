import ebooklib
from ebooklib import epub
from convert import ru_to_arm
from data.letters import *


def convert_chapter(chapter: epub.EpubHtml, options: dict) -> epub.EpubHtml:
    content = chapter.get_content().decode('utf-8')
    processed_text = ru_to_arm(content, options).encode('utf-8')
    chapter.set_content(processed_text)
    return chapter


def convert_epub(book: epub.EpubBook, options: dict) -> epub.EpubBook:
    book_items = list(book.get_items())
    content_items, kept_items = [], []

    for _ in book_items:
        if type(_) == ebooklib.epub.EpubHtml:
            content_items.append(convert_chapter(_, options))
        else:
            kept_items.append(_)

    new_book = epub.EpubBook()

    new_book.metadata = book.metadata
    new_book.spine = book.spine
    new_book.guide = book.guide
    new_book.toc = book.toc
    new_book.bindings = book.bindings
    new_book.pages = book.pages

    for _ in kept_items:
        new_book.add_item(_)
    for _ in content_items:
        new_book.add_item(_)

    return new_book


if __name__ == '__main__':
    book = epub.read_epub('texts/test.epub')
    new_book = convert_epub(book, VOWELS)
    epub.write_epub('texts/test_write.epub', new_book)
