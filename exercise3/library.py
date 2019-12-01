# coding: utf8
from books_list import *

from book import *

class Library():
    """ """
    def __init__(self):
        self.books = []

    def add_book(self, book):
        """method for add an object book in list book """
        self.books.append(book)

    def get_book(self, title):
        """ """
        for i in self.books :
            if title == book.title :
                return book
        return None
