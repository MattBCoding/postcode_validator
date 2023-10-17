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

    def test_invalid_data_type_provided(self):
        """Test that providing an invalid data type raises a TypeError"""
        test_values = [
            True,
            1,
            1.0,
            ["a", "b", "c"],
            {"a": 1, "b": 2, "c": 3},
            ("a", "b", "c"),
            None,
        ]
        for value in test_values:
            with self.assertRaises(TypeError):
                Postcode(value)

    def test_remove_whitespace(self):
        """Test the remove_whitespace method
        the method should return the postcode with whitespace removed.
        """
        test_values = {
            "EC1A 1BB": "EC1A1BB",
            " EC1A1BB": "EC1A1BB",
            "EC1A1BB ": "EC1A1BB",
            "EC1A 1BB ": "EC1A1BB",
            " EC1A 1BB": "EC1A1BB",
            " EC1A    1BB ": "EC1A1BB",
            " E C 1 A 1 B B ": "EC1A1BB",
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.remove_whitespace(), value)

    def test_format(self):
        """Test the format method
        the method should return the postcode formatted to uppercase
        with all whitespace removed.
        """
        test_values = {
            "ec1a 1bb": "EC1A1BB",
            " ec1a1bb": "EC1A1BB",
            "ec1a1bb ": "EC1A1BB",
            "ec1a 1bb ": "EC1A1BB",
            " ec1a 1bb": "EC1A1BB",
            " ec1a    1bb ": "EC1A1BB",
            " e c 1 a 1 b b ": "EC1A1BB",
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.format(), value)

    def test_outward_code(self):
        """Test the outward_code method
        the method should return the outward code of the postcode
        formatted to uppercase with all whitespace removed.
        """
        test_values = {
            "ec1a 1bb": "EC1A",
            " ec1a1bb": "EC1A",
            "ec1a1bb ": "EC1A",
            "ec1a 1bb ": "EC1A",
            " ec1a 1bb": "EC1A",
            " ec1a    1bb ": "EC1A",
            " e c 1 a 1 b b ": "EC1A",
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.outward_code(), value)

    def test_inward_code(self):
        """Test the inward_code method
        the method should return the inward code of the postcode
        formatted to uppercase with all whitespace removed.
        """
        test_values = {
            "ec1a 1bb": "1BB",
            " ec1a1bb": "1BB",
            "ec1a1bb ": "1BB",
            "ec1a 1bb ": "1BB",
            " ec1a 1bb": "1BB",
            " ec1a    1bb ": "1BB",
            " e c 1 a 1 b b ": "1BB",
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.inward_code(), value)


if __name__ == "__main__":
    unittest.main()
