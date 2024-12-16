import logging
from abc import ABC, abstractmethod
from typing import List

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s', handlers=[logging.StreamHandler()])
logger = logging.getLogger(__name__)

# Клас, що представляє книгу
class Book:
    def __init__(self, title: str, author: str, year: str):
        self.title = title
        self.author = author
        self.year = year

    def __repr__(self) -> str:
        return f"Title: {self.title}, Author: {self.author}, Year: {self.year}"

# Інтерфейс бібліотеки
class LibraryInterface(ABC):
    @abstractmethod
    def add_book(self, book: Book) -> None:
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        pass

    @abstractmethod
    def show_books(self) -> None:
        pass

# Реалізація бібліотеки
class Library(LibraryInterface):
    def __init__(self) -> None:
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        self.books.append(book)
        logger.info(f"Book added: {book}")

    def remove_book(self, title: str) -> None:
        book_to_remove = next((book for book in self.books if book.title == title), None)
        if book_to_remove:
            self.books.remove(book_to_remove)
            logger.info(f"Book removed: {book_to_remove}")
        else:
            logger.info(f"Book with title '{title}' not found.")

    def show_books(self) -> None:
        if not self.books:
            logger.info("No books in the library.")
        for book in self.books:
            logger.info(book)

# Клас, що управляє бібліотекою (Manager)
class LibraryManager:
    def __init__(self, library: LibraryInterface) -> None:
        self.library = library

    def add_book(self, title: str, author: str, year: str) -> None:
        book = Book(title, author, year)
        self.library.add_book(book)

    def remove_book(self, title: str) -> None:
        self.library.remove_book(title)

    def show_books(self) -> None:
        self.library.show_books()

# Основна функція для взаємодії з користувачем
def main() -> None:
    library = Library()
    manager = LibraryManager(library)

    while True:
        command = input("Enter command (add, remove, show, exit): ").strip().lower()

        match command:
            case "add":
                title = input("Enter book title: ").strip()
                author = input("Enter book author: ").strip()
                year = input("Enter book year: ").strip()
                manager.add_book(title, author, year)
            case "remove":
                title = input("Enter book title to remove: ").strip()
                manager.remove_book(title)
            case "show":
                manager.show_books()
            case "exit":
                break
            case _:
                logger.info("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
