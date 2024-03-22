import pymongo

client = pymongo.MongoClient()
db = client['starwars']


class MongoTransformation:
    def __init__(self, starship_data, name_of_pilot, client, db):
        self.starship_data = starship_data
        self.name_of_pilot = name_of_pilot
        self.client = client
        self.db = db

    def check_if_name_in_db(self, input_name):
        output_name = db.characters.find_one({"name": input_name}, {"name": 1})
        if output_name:
            return True
        else:
            return False

    def get_id_from_name_in_DB(self, name="Luke Skywalker"):
        ID = db.characters.find_one({"name": name}, {"_id": 1})
        return ID["_id"]

    def data_body_prep(self, name_of_ship=None, model=None, ids=None):
        data = {"name": name_of_ship,
                "model": model,
                "pilot": []
                }
        for pilot_name, pilot_id in ids.items():
            pilot_data = {"name": pilot_name, "character_id": pilot_id}
            data["pilot"].append(pilot_data)
        if len(data["pilot"]) == 0:
            data["pilot"] = None

        return data

    def insert_into_mongodb(self, data):
        result = db.starships.insert_one(data)
        print("Inserted document ID:", result.inserted_id)



