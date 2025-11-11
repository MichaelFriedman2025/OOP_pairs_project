from file_handling import FileHandler

class Library:

    def __init__(self):
        self.list_books = FileHandler.load_json("books.json")
        self.list_users = FileHandler.load_json("users.json")

    def add_book(self, book):
        self.list_books["books"].update(book.cheng_to_dict())
        FileHandler.dump_json("books.json",self.list_books)

    def add_user(self, user):
        self.list_users["users"].update(user.cheng_to_dict())
        FileHandler.dump_json("users.json",self.list_users)

    def borrow_book(self, user_id, book_isdn):
        book = self.list_books["books"].get(book_isdn)
        user = self.list_users["users"].get(user_id)
        if book.is_available:
            if book and user:
                user.borrowed_books.appand(book)
                book.is_available = False
        else:
            print("the book isn't available ")

    def return_book(self, user_id, book_isdn):
        book = self.list_books["books"].get(book_isdn)
        user = self.list_users["users"].get(user_id)
        if book in user.borrowed_books:
            book.is_available = True
            user.borrowed_books.remove(book)

    def list_available_books(self):
        available_books = []
        for book in self.list_books["books"].values():
            if book.is_available:
                available_books.append(book)
        return available_books

    def search_book(self, title):
        for book in self.list_books["books"].value():
            if book["title"] == title:
                return book
        return None

