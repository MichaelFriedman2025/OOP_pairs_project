class Book:
    def __init__(self,title,author,isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True


    def cheng_to_dict(self):
        return {"isbn":self.isbn,"title":self.title,"author":self.author,"is_available":self.is_available}

    def __str__(self):
        return f"title: {self.title}, author: {self.author} ,isbn: {self.isbn}"

