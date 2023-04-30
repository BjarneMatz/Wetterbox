import json
from database import Database as DB

db = DB("testdatenbank")

def manage_data(data):
    data.decode('utf-8')
    data = json.loads(data)
    print("")
    print("Data received:")
    print(data)
    print("")
    data = data.split(",")
    print(data)
    time = data[11]
    del data[11]
    procceced_data = {}
    procceced_data["dht_hum"] = data[0]
    procceced_data["dht_temp"] = data[1]
    procceced_data["dht_heatix"] = data[2]
    procceced_data["earth_temp"] = data[3]
    procceced_data["ground_temp"] = data[4]
    procceced_data["system_temp"] = data[5]
    procceced_data["earth_hum"] = data[6]
    procceced_data["sun_intensity"] = data[7]
    procceced_data["rain_intensity"] = data[8]
    procceced_data["loudness"] = data[9]

    db.load()
    db.set(str(time), procceced_data)
    db.save()


