class Book:
    def __init__(self, title,author):
        self.title = title
        self.author = author
        self._is_checked_out = False

class Library:
    def __init__(self):
        self._books = []
    def add_book(self,book):
        self._books.append(book)

    def check_out_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                if not book._is_checked_out:
                    book._is_checked_out = True
                    return f"'{title}' has been checked out."
                else:
                    return f"'{title}' is already checked out."
        return f"Book titled '{title}' not found."

    def return_book(self, title):
        for book in self._books:
            if book.title.lower() == title.lower():
                book._is_checked_out = False
                return f"'{title}' has been returned."
        return f"Book titled '{title}' not found."

    def list_available_books(self):
        available_books = [book for book in self._books if not book._is_checked_out]
        if not available_books:
            return "No available books."

        output = "Available Books:\n"
        for book in available_books:
            output += f"- {book.title} by {book.author}\n"
        return output.strip()