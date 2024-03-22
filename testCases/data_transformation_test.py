import unittest
from classes.data_transformation import MongoTransformation
import bson


class MyTestCase(unittest.TestCase):
    def test_mongo_transformation_exists(self):
        self.assertTrue(hasattr(MongoTransformation, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(MongoTransformation.__init__))  # Check if __init__ is callable (i.e., it's a method)


    def test_check_if_name_in_db_returns_false_when_not_found(self):

        self.find_id_in_db = lambda name: None

        result = MongoTransformation.check_if_name_in_db(self, input_name="John")

        self.assertFalse(result)

    def test_check_if_name_in_db_returns_true_when_found(self):

        self.find_id_in_db = lambda name: "123456"  # Some example ID

        result = MongoTransformation.check_if_name_in_db(self, input_name="Luke Skywalker")

        self.assertTrue(result)


    def test_class_has_a_body_prep_method(self):
        self.assertTrue(hasattr(MongoTransformation, 'data_body_prep'))

    def test_body_prep_method_returns_dict(self):

        name_of_ship = 'Millennium Falcon'
        model = "YT-1300 light freighter"
        ids = {}

        result = MongoTransformation.data_body_prep(self, name_of_ship, model, ids)

        # Assert that the return value is a dictionary
        self.assertIsInstance(result, dict)
        self.assertTrue(len(result) == 3)

    def test_get_obj_id_from_mongo_with_name(self):
        result = MongoTransformation.get_id_from_name_in_DB("Luke Skywalker")
        self.assertEqual(type(result), bson.objectid.ObjectId)



if __name__ == '__main__':
    unittest.main()
