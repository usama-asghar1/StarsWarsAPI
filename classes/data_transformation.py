import pymongo

client = pymongo.MongoClient()
db = client['starwars']


class MongoTransformation:
    def __init__(self, starship_data, name_of_pilot):
        self.starship_data = starship_data
        self.name_of_pilot = name_of_pilot

    def get_obj_id(self, name_of_pilot):
        ID = db.characters.find_one({"name": name_of_pilot}, {"_id": 1})
        return ID["_id"]










