from src.collection import BookCollection, IndexDict


class Library:
    def __init__(self):
        self.book_collection = BookCollection()
        self.index = IndexDict()

    def add_book(self, book):
        self.book_collection.add(book)
        self.index.add_book(book)

    def remove_book(self, isbn):
        book = self.index.find_isbn(isbn)
        if book:
            self.book_collection.remove(book)
            self.index.remove_book(book)

    def update_book(self, isbn, title=None, author=None, year=None, genre=None):
        book = self.index.find_isbn(isbn)
        if not book:
            return False

        if title is not None:
            book.title = title
        if author is not None:
            book.author = author
        if year is not None:
            book.year = year
        if genre is not None:
            book.genre = genre

        self.index.remove_book(book)
        self.index.add_book(book)

        return True

    def find_author(self, author):
        return self.index.find_author(author)

    def find_year(self, year):
        return self.index.find_year(year)

    def find_isbn(self, isbn):
        return self.index.find_isbn(isbn)
