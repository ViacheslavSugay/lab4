import random
from src.library import Library
from src.book import PaperBook, DigitalBook
from src.data import book_data, titles

def run_simulation(steps: int = 20, seed: int | None = None) -> None:
    if seed is not None:
        random.seed(seed)

    library = Library()
    generated_isbns = []

    for step in range(1, steps + 1):
        event_type = random.randint(1, 6)

        if event_type == 1:
            title = random.choice(titles)
            book_info = book_data[title]
            author = book_info["author"]
            year = book_info["year"]
            genre = book_info["genre"]
            isbn = f"ISBN-{random.randint(10000, 99999)}"
            pages = random.randint(100, 1000)
            weight = random.randint(200, 800)
            cover_type = random.choice(["Твёрдая", "Мягкая"])
            book = PaperBook(title, author, year, genre, isbn, pages, weight, cover_type)
            library.add_book(book)
            generated_isbns.append(isbn)
            print(f"{step}) Добавлена бумажная книга: '{title}' ({author}, {year}), {pages} стр., {weight}г, {book.cover_type} обложка")

        elif event_type == 2:
            title = random.choice(titles)
            book_info = book_data[title]
            author = book_info["author"]
            year = book_info["year"]
            genre = book_info["genre"]
            isbn = f"ISBN-{random.randint(10000, 99999)}"
            file_size = random.randint(1, 50)
            format_type = random.choice(["PDF", "EPUB", "FB2"])
            drm_protected = random.choice([True, False])
            book = DigitalBook(title, author, year, genre, isbn, file_size, format_type, drm_protected)
            library.add_book(book)
            generated_isbns.append(isbn)
            print(f"{step}) Добавлена электронная книга: '{book.title}' ({book.author}, {book.year}), {book.format_type}, {book.file_size}MB, {'нельзя копировать' if book.drm_protected else 'можно копировать'}")

        elif event_type == 3:
            if not generated_isbns:
                print(f"{step}) Невозможно удалить книгу: нет книг в библиотеке")
            else:
                isbn = random.choice(generated_isbns)
                library.remove_book(isbn)
                generated_isbns.remove(isbn)
                print(f"{step}) Удалена книга")

        elif event_type == 4:
            if not generated_isbns:
                print(f"{step}) Невозможно обновить книгу: нет книг в библиотеке")
            else:
                isbn = random.choice(generated_isbns)
                changes = dict()
                if random.random() > 0.5:
                    new_title = random.choice(titles)
                    new_info = book_data[new_title]
                    changes["title"] = new_title
                    changes["author"] = new_info["author"]
                    changes["year"] = new_info["year"]
                    changes["genre"] = new_info["genre"]
                if changes:
                    library.update_book(isbn, **changes)
                    print(f"{step}) Обновлена книга: {changes}")
                else:
                    print(f"{step}) Обновление книги отменено: нет изменений")

        elif event_type == 5:
            author = random.choice(list(set(info["author"] for info in book_data.values())))
            books = library.find_author(author)
            print(f"{step}) Поиск по автору '{author}': найдено {len(books)} книг")

        elif event_type == 6:
            year = random.choice(list(set(info["year"] for info in book_data.values())))
            books = library.find_year(year)
            print(f"{step}) Поиск по году {year}: найдено {len(books)} книг")

    print(f"Итоговое количество книг в библиотеке: {len(library.book_collection)}")