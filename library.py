from file_handling import FileHandler

class Library:

    def __init__(self):
        self.__books =  FileHandler("books.json")
        self.__users = FileHandler("users.json")
        self.list_books = self.__books.load_json()
        self.list_users = self.__users.load_json()

    def add_book(self, book):
        self.list_books["books"].append(book.cheng_to_dict())
        self.__books.dump_json(self.list_books)

    def add_user(self, user):
        self.list_users["users"].append(user.cheng_to_dict())
        self.__users.dump_json(self.list_users)

    def borrow_book(self, user_id, book_isdn):
        for user in self.list_users["users"]:
            if user["id"] == user_id:
                for book in self.list_books["books"]:
                    if book["isbn"] == book_isdn:
                        if book["is_available"]:
                            user["borrowed_books"].append(book)
                            book["is_available"] = False
                            self.__users.dump_json(self.list_users)
                            self.__books.dump_json(self.list_books)
                        else:
                            print("the book isn't available ")

    def return_book(self, user_id, book_isdn):
        for user in self.list_users["users"]:
            if user["id"] == user_id:
                for book in self.list_books["books"]:
                    if book["isbn"] == book_isdn:
                        user["borrowed_books"].remove(book)
                        book["is_available"] = True
                        self.__users.dump_json(self.list_users)
                        self.__books.dump_json(self.list_books)

    def list_available_books(self):
        available_books = []
        for book in self.list_books["books"]:
            if book["is_available"]:
                available_books.append(book)
        return available_books

    def search_book(self, title):
        for book in self.list_books["books"]:
            if book["title"] == title:
                return book
        return None

