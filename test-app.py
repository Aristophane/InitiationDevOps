import unittest

from app import multplication
"""Calculatrice"""
class TestStringMethods(unittest.TestCase):

    def testMultiplicationTrue(self):
        """Test OK Calculatrice"""
        self.assertEqual(multplication(2,5), 10)

    def testMultiplicationNotTrue(self):
        """Test KO Calculatrice"""
        self.assertNotEqual(multplication(2,5), 11)

if __name__ == '__main__':
    unittest.main()
