import pytest
from src.simulation import run_simulation
from src.library import Library
from src.book import PaperBook, DigitalBook
from src.data import book_data, titles


class TestSimulation:

    def test_library_add_printed_book(self):
        library = Library()

        book_info = book_data[titles[0]]
        book = PaperBook(
            titles[0],
            book_info["author"],
            book_info["year"],
            book_info["genre"],
            "ISBN-12345",
            500,
            300,
            "Твёрдая"
        )

        initial_count = len(library.book_collection)
        library.add_book(book)

        assert len(library.book_collection) == initial_count + 1

    def test_library_add_ebook(self):
        library = Library()

        book_info = book_data[titles[1]]
        book = DigitalBook(
            titles[1],
            book_info["author"],
            book_info["year"],
            book_info["genre"],
            "ISBN-67890",
            15,
            "PDF",
            False
        )

        initial_count = len(library.book_collection)
        library.add_book(book)

        assert len(library.book_collection) == initial_count + 1

    def test_library_find_author(self):
        library = Library()

        author = book_data[titles[0]]["author"]

        books = library.find_author(author)

        assert isinstance(books, list)

    def test_library_find_year(self):
        library = Library()

        year = book_data[titles[0]]["year"]

        books = library.find_year(year)

        assert isinstance(books, list)

    def test_book_creation(self):
        book_info = book_data[titles[0]]

        printed_book = PaperBook(
            titles[0],
            book_info["author"],
            book_info["year"],
            book_info["genre"],
            "ISBN-22222",
            600,
            400,
            "Твёрдая"
        )

        ebook = DigitalBook(
            titles[1],
            book_info["author"],
            book_info["year"],
            book_info["genre"],
            "ISBN-33333",
            20,
            "EPUB",
            True
        )

        assert printed_book.title == titles[0]
        assert ebook.title == titles[1]