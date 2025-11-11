class Book:
    __counter_isbn = 0
    def __init__(self,title,author):
        self.title = title
        self.author = author
        self.isbn = Book.__counter_isbn
        self.is_available = True
        Book.__counter_isbn += 1


    def cheng_to_dict(self):
        return {f"{self.isbn}":{"title":self.title,"author":self.author,"is_available":self.is_available}}

    def __str__(self):
        return f"title: {self.title}, author: {self.author} ,isbn: {self.isbn}"

