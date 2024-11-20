import unittest

from app import multplication

class TestStringMethods(unittest.TestCase):

    def test_multiplicationTrue(self):
        self.assertEqual(multplication(2,5), 10)

    def test_multiplicationNotTrue(self):
        self.assertNotEqual(multplication(2,5), 11)
        
if __name__ == '__main__':
    unittest.main()