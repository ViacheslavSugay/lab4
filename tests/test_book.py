import pytest
from src.library import Library
from src.book import Book

def test_library_add_remove():
    library = Library()
    book = Book("Test", "Author", 2023, "Genre", "ISBN-123")
    library.add_book(book)
    assert len(library.book_collection) == 1
    library.remove_book("ISBN-123")
    assert len(library.book_collection) == 0

def test_library_find_isbn():
    library = Library()
    book = Book("Test", "Author", 2023, "Genre", "ISBN-123")
    library.add_book(book)
    found = library.find_isbn("ISBN-123")
    assert found == book
    assert library.find_isbn("ISBN-999") is None

def test_library_update_book():
    library = Library()
    book = Book("Old", "Author", 2023, "Genre", "ISBN-123")
    library.add_book(book)
    library.update_book("ISBN-123", title="New")
    updated = library.find_isbn("ISBN-123")
    assert updated.title == "New"

def test_library_find_author():
    library = Library()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author1", 2021, "Genre", "ISBN-2")
    library.add_book(book1)
    library.add_book(book2)
    author1_books = library.find_author("Author1")
    assert len(author1_books) == 2

def test_library_find_year():
    library = Library()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author2", 2020, "Genre", "ISBN-2")
    library.add_book(book1)
    library.add_book(book2)
    year2020_books = library.find_year(2020)
    assert len(year2020_books) == 2

def test_library_update_nonexistent():
    library = Library()
    result = library.update_book("ISBN-999", title="New")
    assert result == False