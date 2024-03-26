import unittest


class TestMaxInteger(unittest.TestCase):

    def test_single_element_list(self):
        """Test list with one element."""
        test_list = [5]
        self.assertEqual(max_integer, output) 

    def test_multiple_elements_list(self):
        """Test with multiple elements."""
        test_list = [3, 7, 2, 9, 1]
        self.assertEqual(9, max_integer(test_list))

    def test_non_numeric_list(self):
        """Test a list with non-numeric elements."""
        test_list = ["apple", 7, "banana", 9, 1]
        with self.assertRaises(TypeError):
            max_integer(test_list)

    def test_empty_list(self):
        """Test with an empty list."""
        self.assertEqual(None, max_integer([]))

    def test_negative_integers(self):
        """Test list with negative ints."""
        test_list = [-2, -5, -1, -8]
        self.assertEqual(-1, max_integer(test_list))

    def test_mixed_numbers(self):
        """Test list with mixed number types."""
        test_list = [3.5, 7, 2.2, 9.1, 1]
        self.assertEqual(9.1, max_integer(test_list))


if __name__ == "__main__":
    unittest.main()
