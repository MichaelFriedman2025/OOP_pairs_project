from library import Library
from book import Book
from user import User

library = Library()

while True:
     menu_library = input("What do you want to do?\n"
                          "to add a book: press 1.\n"
                          "to add a user: press 2.\n"
                          "to borrow a book: press 3.\n"
                          "to return a book: press 4.\n"
                          "to show available books: press 5.\n"
                          "to search a book: press 6.\n"
                          "to save and exit: press 7.\n")
     match menu_library:
         case "1":
             title_book = input("enter title of book")
             author_book = input("enter author of book")
             isbn_book = input("enter isbn of book")
             book = Book(title_book, author_book,isbn_book)
             library.add_book(book)
         case "2":
             name_user = input("enter name of user")
             id_user = input("enter id of user")
             user = User(name_user,id_user)
             library.add_user(user)
         case "3":
             user_id = input("enter user_id:")
             book_isdn = input("enter book_isdn:")
             library.borrow_book(user_id,book_isdn)

         case "4":
             user_id = input("enter user_id:")
             book_isdn = input("enter book_isdn:")
             library.return_book(user_id, book_isdn)

         case "5":
             print(library.list_available_books())

         case "6":
             title_book = input("enter title of book")
             print(library.search_book(title_book))

         case "7":
             break
