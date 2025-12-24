class Book:
    def __init__(self, title, author, year, genre, isbn):
        self.title = title
        self.author = author
        self.year = year
        self.genre = genre
        self.isbn = isbn

    def __repr__(self):
        return f"Book('{self.title}', '{self.author}', {self.year}, '{self.genre}', '{self.isbn}')"


class PaperBook(Book):
    def __init__(self, title, author, year, genre, isbn, pages, weight, cover_type):
        super().__init__(title, author, year, genre, isbn)
        self.pages = pages
        self.weight = weight
        self.cover_type = cover_type

    def get_weight(self):
        return self.weight

    def __repr__(self):
        return (f"PrintedBook('{self.title}', '{self.author}', {self.year}, "
                f"'{self.genre}', '{self.isbn}', {self.pages}, {self.weight}, '{self.cover_type}')")


class DigitalBook(Book):
    def __init__(self, title, author, year, genre, isbn, file_size, format_type, drm_protected):
        super().__init__(title, author, year, genre, isbn)
        self.file_size = file_size
        self.format_type = format_type
        self.drm_protected = drm_protected

    def get_file_info(self):
        return f"{self.format_type}, {self.file_size}MB"

    def can_be_shared(self):
        return not self.drm_protected

    def __repr__(self):
        return (f"Ebook('{self.title}', '{self.author}', {self.year}, "
                f"'{self.genre}', '{self.isbn}', {self.file_size}, '{self.format_type}', {self.drm_protected})")