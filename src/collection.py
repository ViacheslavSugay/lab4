from collections import UserList, UserDict


class BookCollection(UserList):
    def __init__(self):
        super().__init__()

    def add(self, book):
        self.append(book)

    def __contains__(self, isbn):
        for book in self.data:
            if book.isbn == isbn:
                return True
        return False


class IndexDict(UserDict):
    def __init__(self):
        super().__init__()
        self.author_index = dict()
        self.year_index = dict()

    def add_book(self, book):
        self.data[book.isbn] = book

        if book.author not in self.author_index:
            self.author_index[book.author] = []
        if book not in self.author_index[book.author]:
            self.author_index[book.author].append(book)

        if book.year not in self.year_index:
            self.year_index[book.year] = []
        if book not in self.year_index[book.year]:
            self.year_index[book.year].append(book)

    def remove_book(self, book):
        if book.isbn in self.data:
            del self.data[book.isbn]

        if book.author in self.author_index and book in self.author_index[book.author]:
            self.author_index[book.author].remove(book)
            if not self.author_index[book.author]:
                del self.author_index[book.author]

        if book.year in self.year_index and book in self.year_index[book.year]:
            self.year_index[book.year].remove(book)
            if not self.year_index[book.year]:
                del self.year_index[book.year]

    def find_isbn(self, isbn):
        return self.data.get(isbn)

    def find_author(self, author):
        return self.author_index.get(author, [])

    def find_year(self, year):
        return self.year_index.get(year, [])
