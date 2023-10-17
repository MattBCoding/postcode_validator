import unittest
from postcodelib.postcode import Postcode


class TestPostcode(unittest.TestCase):
    """A class to test the Postcode class"""

    def test_to_confirm_imports_work(self):
        """Test that the postcode attribute is a string"""
        postcode = Postcode("EC1A 1BB")
        self.assertEqual(type(postcode.postcode), str)

    def test_validate_with_valid_postcode(self):
        """Test the validate method
        the method should returns True for a valid postcode
        and should return False for an invalid postcode.
        """
        postcode = Postcode("EC1A1BB")
        self.assertTrue(postcode.validate())

    def test_validate_with_invalid_postcode(self):
        """Test the validate method
        the method should return False for an invalid postcode.
        """
        postcode = Postcode("EC1A 1BB")
        self.assertFalse(postcode.validate())


if __name__ == "__main__":
    unittest.main()
