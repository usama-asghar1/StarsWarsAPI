import unittest
from classes.APIRetrieval import APIRetrieval




class MyTestCase(unittest.TestCase):
    def test_APIClassExists(self):
        self.assertTrue(hasattr(APIRetrieval, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(APIRetrieval.__init__))  # Check if __init__ is callable (i.e., it's a method)
    def test_APIClassHasMethodToGetAllStarShipInfo(self):
        self.assertTrue(hasattr(APIRetrieval, 'get_starships_info'))
    def test_APIClassHasBaseLink(self):
        self.assertTrue(hasattr(APIRetrieval, 'BaseUrl'))


if __name__ == '__main__':
    unittest.main()
