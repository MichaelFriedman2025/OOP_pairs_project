class User:
    __id = 0
    def __init__(self, name):
        self.name = name
        self.id = User.__id
        self.borrowed_books = []

    def cheng_to_dict(self):
        return {f"{self.id}":{"name":self.name,"id":self.id}}
