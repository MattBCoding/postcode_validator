import unittest
from postcodelib.postcode import Postcode


class TestPostcode(unittest.TestCase):
    """A class to test the Postcode class"""

    def test_to_confirm_imports_work(self):
        """Test that the postcode attribute is a string"""
        postcode = Postcode("EC1A 1BB")
        self.assertEqual(type(postcode.postcode), str)


if __name__ == "__main__":
    unittest.main()
