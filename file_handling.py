import json

class FileHandling:

    @staticmethod
    def load_json():
        with open("books.json" , "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return []

    @staticmethod
    def save_json(data):
        with open("books.json" ,"w",encoding="utf-8") as file:
            json.dump(data,file,indent=4,ensure_ascii=False)

