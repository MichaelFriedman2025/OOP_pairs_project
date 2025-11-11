import json

class FileHandler:
    def __init__(self,name_of_file):
        self.name_of_file = name_of_file

    def load_json(self):
        with open(self.name_of_file , "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {self.name_of_file[:5]:[]}

    def dump_json(self,data):
        with open(self.name_of_file ,"w",encoding="utf-8") as file:
            json.dump(data,file,indent = 4,ensure_ascii = False)


