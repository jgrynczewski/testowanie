import unittest

import my_functions

class TestAdd(unittest.TestCase):
    def test_add_integer(self):
        """
        Test that the addition of two integers returns correct result
        """
        self.assertEqual(my_functions.add(1, 2), 3)
        self.assertEqual(my_functions.add(0, 0), 0)

    def test_add_float(self):
        """
        Test that addition of two floats returns correct result
        """
        self.assertAlmostEqual(my_functions.add(2.3, 5.2), 7.5)
        self.assertAlmostEqual(my_functions.add(2.3, -1.1), 1.2)

    def test_add_string(self):
        """Test the addition of two strings returns one concatenated string"""
        self.assertEqual(my_functions.add("abc", "def"), "abcdef")
        self.assertEqual(my_functions.add("",""), "")

class TestDivide(unittest.TestCase):
    def test_value_error(self):
        """Test if ValueError is raised when needed"""
        self.assertRaises(ValueError, my_functions.divide, 3, 0)
        self.assertRaises(ValueError, my_functions.divide, 0, 0)

if __name__=="__main__":
    unittest.main()

# Zadanie domowe
# 100% pokrycie kodu my_functions testami.