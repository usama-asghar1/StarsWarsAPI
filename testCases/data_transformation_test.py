import unittest
from classes.data_transformation import MongoTransformation


class MyTestCase(unittest.TestCase):
    def test_mongo_transformation_exists(self):
        self.assertTrue(hasattr(MongoTransformation, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(MongoTransformation.__init__))  # Check if __init__ is callable (i.e., it's a method)
        self.assertTrue(hasattr(MongoTransformation, 'client'))
        self.assertTrue(hasattr(MongoTransformation, 'db'))

    def test_check_if_name_in_db_returns_false_when_not_found(self):

        self.find_id_in_db = lambda name: None


        result = self.check_if_name_in_db("John")


        self.assertFalse(result)

    def test_check_if_name_in_db_returns_true_when_found(self):

        self.find_id_in_db = lambda name: "123456"  # Some example ID

        result = self.check_if_name_in_db("Alice")

        self.assertTrue(result)


    def test_class_has_a_body_prep_method(self):
        self.assertTrue(hasattr(MongoTransformation, 'data body prep'))

    def test_body_prep_method_returns_dict(self):

        result = MongoTransformation.data_body_prep()

        # Assert that the return value is a dictionary
        self.assertIsInstance(result, dict)








if __name__ == '__main__':
    unittest.main()
