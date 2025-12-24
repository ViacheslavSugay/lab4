import pytest
from src.collection import BookCollection, IndexDict
from src.book import Book

def test_bookcollection_basic():
    collection = BookCollection()
    assert len(collection) == 0
    book = Book("Test", "Author", 2023, "Genre", "ISBN-123")
    collection.add(book)
    assert len(collection) == 1
    assert collection[0] == book

def test_bookcollection_contains():
    collection = BookCollection()
    book = Book("Test", "Author", 2023, "Genre", "ISBN-123")
    collection.add(book)
    assert "ISBN-123" in collection
    assert "ISBN-999" not in collection

def test_bookcollection_remove():
    collection = BookCollection()
    book = Book("Test", "Author", 2023, "Genre", "ISBN-123")
    collection.add(book)
    collection.remove(book)
    assert len(collection) == 0

def test_indexdict_add_book():
    index = IndexDict()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author1", 2021, "Genre", "ISBN-2")
    index.add_book(book1)
    index.add_book(book2)
    assert index.find_isbn("ISBN-1") == book1
    assert index.find_isbn("ISBN-2") == book2

def test_indexdict_find_author():
    index = IndexDict()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author1", 2021, "Genre", "ISBN-2")
    index.add_book(book1)
    index.add_book(book2)
    author1_books = index.find_author("Author1")
    assert len(author1_books) == 2
    assert book1 in author1_books
    assert book2 in author1_books

def test_indexdict_find_year():
    index = IndexDict()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author2", 2020, "Genre", "ISBN-2")
    index.add_book(book1)
    index.add_book(book2)
    year2020_books = index.find_year(2020)
    assert len(year2020_books) == 2
    assert book1 in year2020_books
    assert book2 in year2020_books

def test_indexdict_remove_book():
    index = IndexDict()
    book1 = Book("Book1", "Author1", 2020, "Genre", "ISBN-1")
    book2 = Book("Book2", "Author1", 2021, "Genre", "ISBN-2")
    index.add_book(book1)
    index.add_book(book2)
    index.remove_book(book1)
    assert index.find_isbn("ISBN-1") is None
    assert len(index.find_author("Author1")) == 1


def test_bookcollection_slices():
    collection = BookCollection()

    books = [
        Book("Book1", "Author1", 2020, "Genre", "ISBN-1"),
        Book("Book2", "Author2", 2021, "Genre", "ISBN-2"),
        Book("Book3", "Author3", 2022, "Genre", "ISBN-3"),
        Book("Book4", "Author4", 2023, "Genre", "ISBN-4"),
    ]

    for book in books:
        collection.append(book)

    slice_result = collection.data[1:3]
    assert len(slice_result) == 2
    assert slice_result[0].title == "Book2"
    assert slice_result[1].title == "Book3"

    assert len(collection.data[::2]) == 2
    assert len(collection.data[-2:]) == 2
    assert len(collection.data[10:20]) == 0