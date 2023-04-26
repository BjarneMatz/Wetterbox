import json


# Path to the database folder
DATABASEPATH = r"./Server Backend/Database/Testdata/" 


class Database:
    def __init__(self, dbname: str) -> None:
        """generates a new database object

        Args:
            dbname (str): name of the database
        """
        self.dbname = dbname
        try:
            self.load()
        except FileNotFoundError:
            self.data = {}
            self.save()


    def set(self, key:str, value):
        """function to set a value in the database

        Args:
            key (str): key to set
            value (any): value to bind to key
        """

        self.data[key] = value


    def get(self, key:str):
        """function to get a value from the database
        
        Args:
            key (str): key to get
        """

        return self.data[key]


    def delete(self, key:str):
        """function to delete a key from the database

        Args:
            key (str): key to delete
        """

        del self.data[key]


    def get_keys(self):
        """function to get all keys from the database"""

        return self.data.keys()


    def save(self):
        """function to save the database to a file"""

        with open(f"{DATABASEPATH}{self.dbname}.json", "w") as file_data:
            json.dump(self.data, file_data, indent=4)

    
    def load(self):
        """function to load the database from a file"""
        with open(f"{DATABASEPATH}{self.dbname}.json") as file_data:
            self.data = json.load(file_data)

    def update(self):
        """function to (quickly) update made changes to the database"""
        self.save()
        self.load()
