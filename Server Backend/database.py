import json

DATABASEPATH = r"./Server Backend/Database/Testdata/"

class Database:
    def __init__(self, dbname: str) -> None:
        self.dbname = dbname
        try:
            self.load()
        except FileNotFoundError:
            self.data = {}
            self.save()

    def set(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]

    def delete(self, key):
        del self.data[key]

    def get_keys(self):
        return self.data.keys()

    def save(self):
        with open(f"{DATABASEPATH}{self.dbname}.json", "w") as file_data:
            json.dump(self.data, file_data, indent=4)

    def load(self):
        with open(f"{DATABASEPATH}{self.dbname}.json") as file_data:
            self.data = json.load(file_data)

    def update(self):
        self.save()
        self.load()
