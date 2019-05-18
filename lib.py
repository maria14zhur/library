"""Library, that allows add and remove books and search books on author's name, year of publish or book title"""


book_d = {}
year_d = {}
author_d = {}
title_d = {}


def sub_add(sub_inf, sub_dict, inform):
    """Add information about book(i.e. title, year, author) in appropriate dict by the corresponding key
    for fast search"""
    if sub_inf in sub_dict:
        sub_dict[sub_inf] += [inform]
    else:
        sub_dict[sub_inf] = [inform]


def check_type(fn):
    def wrapper(*args):
        if all(type(x) == str for x in args):
            result = fn(*args)
        else:
            result = 'Invalid type. Expected "str"'
        return result
    return wrapper


@check_type
def add(author: str, title: str, year: str, text='text'):
    book_d[author, title, year] = [text]
    sub_add(author, author_d, [author, title, year])
    sub_add(title, title_d, [author, title, year])
    sub_add(year, year_d, [author, title, year])


@check_type
def find_author(author: str):
    try:
        return author_d[author]
    except KeyError:
        return 'Книги не найдены'


@check_type
def find_title(title: str):
    try:
        return title_d[title]
    except KeyError:
        return 'Книги не найдены'


@check_type
def find_year(year: str):
    try:
        return year_d[year]
    except KeyError:
        return 'Книги не найдены'


def sub_remove(sub_dict, sub_inf, inform):
    sub_dict[sub_inf] = [i for i in sub_dict[sub_inf] if i != inform]
    if not sub_dict[sub_inf]:
        del sub_dict[sub_inf]


@check_type
def remove(author: str, title: str, year: str):
    try:
        del book_d[author, title, year]
    except KeyError:
        return None
    sub_remove(author_d, author, [author, title, year])
    sub_remove(title_d, title, [author, title, year])
    sub_remove(year_d, year, [author, title, year])
