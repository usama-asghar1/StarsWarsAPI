import unittest
import requests
from classes.APIRetrieval import APIRetrieval




class MyTestCase(unittest.TestCase):
    def test_APIClass_exists(self):
        self.assertTrue(hasattr(APIRetrieval, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(APIRetrieval.__init__))  # Check if __init__ is callable (i.e., it's a method)
    def test_APIClass_has_method_to_get_all_starship_Info(self):
        self.assertTrue(hasattr(APIRetrieval, 'get_starships_info'))
    def test_APIClassHas_starship_link(self):
        self.assertTrue(hasattr(APIRetrieval, 'StarshipUrl'))
    def test_APIClass_has_baseLink(self):
        self.assertTrue(hasattr(APIRetrieval, 'BaseUrl'))
    def test_APIClass_has_peopleLink(self):
        self.assertTrue(hasattr(APIRetrieval, 'PeopleUrl'))

    def test_API_class_has_method_To_get_all_people_info(self):
        self.assertTrue(hasattr(APIRetrieval, 'get_people_info'))

    def test_Get_all_people_info(self):
        api = APIRetrieval()
        people = api.get_people_info()
        self.assertEqual(len(people), 82)
    def test_Get_all_starship_info(self):
        api = APIRetrieval()
        sharships = api.get_starships_info()
        self.assertTrue(len(sharships) == 36)
    def test_get_specific_starship_info(self):
        api = APIRetrieval()
        starship = api.get_specific_starship_info(9)
        self.assertTrue(starship['name'] == "Death Star")
        self.assertTrue(starship['model'] == "DS-1 Orbital Battle Station")

    def test_get_specific_people_info(self):
        api = APIRetrieval()
        people = api.get_specific_people_info(1)
        self.assertTrue(people['name'] == "Luke Skywalker")
        self.assertTrue(people['height'] == "172")

    def test_fail_to_get_specific_people_info(self):
        api = APIRetrieval()
        people = api.get_specific_people_info(100)
        self.assertTrue(people.status_code == 404)
    def test_fail_to_get_specific_starship_info(self):
        api = APIRetrieval()
        starships = api.get_specific_starship_info(100)
        self.assertTrue(starships.status_code == 404)


if __name__ == '__main__':
    unittest.main()

