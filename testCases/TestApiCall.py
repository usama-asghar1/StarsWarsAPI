import unittest




class MyTestCase(unittest.TestCase):
    def test_APIClassExists(self):
        self.assertTrue(hasattr(APIRetrieval, '__init__'))  # Check if the class has an __init__ method
        self.assertTrue(callable(APIRetrieval.__init__))  # Check if __init__ is callable (i.e., it's a method)


if __name__ == '__main__':
    unittest.main()
