from database import Database as DB
from os import listdir

DATABASEPATH = r"./Server Backend/Database/Testdata/"

def main():
    print(listdir(DATABASEPATH))
    dbname = input("Wähle eine der gelisten Datenbanken oder gib einen neuen Namen ein: ")
    db = DB(dbname)
    db.load()

    menu_action = 0
    while menu_action != 9:
        print("""
        [1] Alle Schlüssel anzeigen
        [2] Schlüssel-Wert-Paar hinzufügen
        [3] Wert anzeigen
        [4] Schlüssel-Wert-Paar löschen
        [5] Datenbank speichern
        [9] Beenden
        """)
        menu_action = int(input("Was möchtest du tun? "))
        if menu_action == 9:
            exit()
        elif menu_action == 1:
            print(db.get_keys())
        elif menu_action == 2:
            key = input("Schlüssel: ")
            value = input("Wert: ")
            db.set(key, value)
        elif menu_action == 3:
            key = input("Schlüssel: ")
            print(db.get(key)) 
        elif menu_action == 4:
            key = input("Schlüssel: ")
            db.delete(key)
        elif menu_action == 5:
            db.save()
        else:
            print("Ungültige Eingabe!")
        





    

if __name__ == "__main__":
    main()