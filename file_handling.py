import json

class FileHandler:

    @staticmethod
    def load_json(name_of_file):
        with open(name_of_file , "r", encoding="utf-8") as file:
            try:
                return json.load(file)
            except json.JSONDecodeError:
                return {name_of_file[:5]:{}}

    @staticmethod
    def dump_json(name_of_file,data):
        with open(name_of_file ,"w",encoding="utf-8") as file:
            json.dump(data,file,indent = 4,ensure_ascii = False)

