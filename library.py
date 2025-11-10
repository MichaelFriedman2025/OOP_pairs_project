class Library:

    def __init__(self):
        self.list_books = []
        self.list_users = []

    def add_book(self, book):
        self.list_books.append(book)

    def add_user(self, user):
        self.list_users.append(user)

    def borrow_book(self, user_id, book_isdn):
        for book in self.list_books:
            if book.isbn == book_isdn:
                book.isbn = False
                for user in self.list_users:
                    if user.id == user_id:
                        user.borrowed_books.append(book)

    def return_book(self, user_id, book_isdn):
        for book in self.list_books:
            if book.isbn == book_isdn:
                book.isbn = True
                for user in self.list_users:
                    if user.id == user_id:
                        user.borrowed_books.remove(book)

    def list_available_books(self):
        available_books = []
        for book in self.list_books:
            if book.is_available:
                available_books.append(book)
        return available_books

    def search_book(self, title):
        for book in self.list_books:
            if book.title == title:
                return book
        return None

