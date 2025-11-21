class Book:
    def __init__(self, title, author):
        self.title = title              # Public attribute
        self.author = author            # Public attribute
        self._is_checked_out = False    # Private attribute

    def check_out(self):
        """Mark the book as checked out if available."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False

    def return_book(self):
        """Mark the book as returned."""
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []   # Private list of Book objects

    def add_book(self, book):
        """Add a Book object to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Check out a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                if book.check_out():
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        """Return a book by title."""
        for book in self._books:
            if book.title.lower() == title.lower():
                book.return_book()
                return f"'{title}' has been returned."
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        """Print all available books."""
        available = [book for book in self._books if book.is_available()]

        if not available:
            return "No available books."

        book_list = "Available Books:\n"
        for book in available:
            book_list += f"- {book.title} by {book.author}\n"

        return book_list.strip()
