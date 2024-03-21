import unittest
from classes.data_transformation import MongoTransformation


class MyTestCase(unittest.TestCase):
    def test_mongo_transformation_exists(self):
        self.assertTrue(hasattr(MongoTransformation, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(MongoTransformation.__init__))  # Check if __init__ is callable (i.e., it's a method)


    def test_get_obj_id_from_mongo_with_name(self):
        result = get_id_from_name_in_DB("Luke Skywalker")
        self.assertEqual(len(result), 1)


if __name__ == '__main__':
    unittest.main()
