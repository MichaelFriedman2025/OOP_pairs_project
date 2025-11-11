class User:
    def __init__(self, name,id):
        self.name = name
        self.id = id
        self.borrowed_books = []

    def cheng_to_dict(self):
        return {"name":self.name,"id":self.id,"borrowed_books":[]}
