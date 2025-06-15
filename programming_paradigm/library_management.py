class Book:
    """Represents a book with title, author, and availability status."""

    def __init__(self, title, author):
        """Initialize the book with a title, author, and availability."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as available."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out

    def __str__(self):
        """String representation of the book."""
        return f"{self.title} by {self.author}"


class Library:
    """Represents a collection of books and supports book management operations."""

    def __init__(self):
        """Initialize the library with an empty book list."""
        self._books = []

    def add_book(self, book):
        """Add a book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Attempt to check out a book by title."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"You have checked out '{title}'.")
                return
        print(f"'{title}' is either not available or does not exist.")

    def return_book(self, title):
        """Attempt to return a book by title."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"'{title}' has been returned.")
                return
        print(f"'{title}' was not checked out or does not exist.")

    def list_available_books(self):
        """Print a list of available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(book)
        else:
            print("No books available.")

from library_management import Book, Library

def main():
    """Demonstrates interaction with the library system."""
    library = Library()
    library.add_book(Book("Brave New World", "Aldous Huxley"))
    library.add_book(Book("1984", "George Orwell"))

    # Initial list of available books
    print("Available books after setup:")
    library.list_available_books()

    # Simulate checking out a book
    library.check_out_book("1984")
    print("\nAvailable books after checking out '1984':")
    library.list_available_books()

    # Simulate returning a book
    library.return_book("1984")
    print("\nAvailable books after returning '1984':")
    library.list_available_books()

if __name__ == "__main__":
    main()
