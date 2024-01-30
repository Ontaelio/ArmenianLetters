from data.sets import BOOKS_SELECTION, SetResponse


def get_sets_list() -> list:
    res = []
    for book in BOOKS_SELECTION.values():
        res.append({'id': book.id, 'name': book.name})
    return res


def get_sets_full() -> list:
    return list(book for book in BOOKS_SELECTION.values())


def get_sets_for_frontend() -> dict:
    res = {}
    for book in BOOKS_SELECTION.values():
        res_b = {1: []}
        column_count = 1
        for section in book.contents:
            if section.front_name in book.columns:
                column_count += 1
                res_b[column_count] = []
            res_b[column_count].append(SetResponse(name=section.name, front_name=section.front_name,
                                                   title=section.title, offset=section.offset))
        res[book.name] = res_b
    return res


def get_set_by_id(set_id: int) -> list:
    return BOOKS_SELECTION[set_id].contents
