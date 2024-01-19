from ebooklib import epub
from bs4 import BeautifulSoup
from convert import ru_to_arm
from data.letters import *


def get_template(chapter: epub.EpubHtml) -> str:
    content = chapter.content.decode('utf-8')
    res = content.split('<body')
    return res[0]


def convert_chapter(chapter: epub.EpubHtml, options: dict) -> epub.EpubHtml:
    content = chapter.content.decode('utf-8')
    processed_text = ru_to_arm(content, options).encode('utf-8')
    chapter.content = processed_text
    return chapter


def convert_epub(book: epub.EpubBook, options: dict) -> epub.EpubBook:
    book_items = list(book.get_items())
    content_items, kept_items = [], []
    template = ''

    for _ in book_items:
        if type(_) == epub.EpubHtml:
            if not template:
                template = get_template(_)
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
    new_book.title = book.title
    new_book.language = book.language
    new_book.direction = book.direction
    new_book.templates = book.templates
    new_book.templates['chapter'] = template  # default template is evil
    new_book.prefixes = book.prefixes
    new_book.namespaces = book.namespaces
    new_book.IDENTIFIER_ID = book.IDENTIFIER_ID
    new_book.FOLDER_NAME = book.FOLDER_NAME
    new_book.EPUB_VERSION = book.EPUB_VERSION

    for _ in kept_items:
        #new_book.add_item(_)
        new_book.items.append(_)
    for _ in content_items:
        # new_book.add_item(_)
        new_book.items.append(_)

    return new_book


def epub2txt(book: epub.EpubBook) -> str:
    book_items = list(book.get_items())
    text_items = []

    for _ in book_items:
        if type(_) == epub.EpubHtml:
            soup = BeautifulSoup(_.get_body_content(), 'html.parser')
            text = [para.get_text() for para in soup.find_all('p')]
            text_items.append('\n'.join(text))

    return '\n\n\n\n\n'.join(text_items)


if __name__ == '__main__':
    boo = epub.read_epub('texts/test.epub')
    # (boo.templates)
    # print(dir(boo))
    # print(epub2txt(boo))
    new_boo = convert_epub(boo, VOWELS)
    epub.write_epub('texts/test_write.epub', new_boo)

