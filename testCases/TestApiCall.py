import unittest
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
        self.assertTrue(hasattr(APIRetrieval, 'BaseUrl'))

    def test_API_class_has_method_To_get_all_star_shipInfo(self):
        self.assertTrue(hasattr(APIRetrieval, 'get_people_info'))

    def test_Get_all_people_info(self):
        api = APIRetrieval()
        people = api.get_people_info()
        self.assertTrue(len(people) == 82)
    def test_Get_all_starship_info(self):
        api = APIRetrieval()
        people = api.get_starships_info()
        self.assertTrue(len(people) == 36)


if __name__ == '__main__':
    unittest.main()
