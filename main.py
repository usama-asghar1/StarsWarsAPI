from unittest import main
from classes.data_transformation import *
from classes.APIRetrieval import *
import pymongo


apiObj= APIRetrieval()
mongoObj = MongoTransformation()

starship_data = apiObj.get_starships_info()


for starship in starship_data:
    model = starship['model']
    name_of_ship = starship['name']
    ids = {}
#    print(starship['name'])
    for pilot in starship['pilots']:

        name_of_pilot = apiObj.Get_Json_from_full_URL(pilot)['name'] ##Api side
        ID = mongoObj.get_id_from_name_in_DB(name_of_pilot)  ## Mongo side
        ids[name_of_pilot] = ID
    data =mongoObj.data_body_prep(name_of_ship,model,ids)  ##Mongo side
    mongoObj.insert_into_mongodb(data) ##Mongo side
    print("new set")
