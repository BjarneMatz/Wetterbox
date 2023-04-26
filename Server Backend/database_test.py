from database import Database as DB

db = DB("testdatenbank")
db.load()
db.set("test", "test")
db.save()
db.load()
print(db.data)
print(db.get("test"))
db.delete("test")
db.save()
db.load()
print(db.data)