import json

def add_user(id):
    with open("database/db.json", "r+") as file:
        db = json.load(file)
        db[str(id)] = {"boosters_opened" : -1, "last_open" : "", "jokers" : [], "cards" : []}
        file.seek(0)
        json.dump(db, file)