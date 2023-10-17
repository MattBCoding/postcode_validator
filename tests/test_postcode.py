import unittest
from src.postcodelib.postcode import Postcode


class TestPostcode(unittest.TestCase):
    """A class to test the Postcode class"""

    def test_is_valid_with_valid_postcode(self):
        """Test the is_valid method
        the method should returns True for a valid postcode
        and should return False for an invalid postcode.
        """
        test_values = ["TW13 4TA", "TW134TA"]
        for value in test_values:
            postcode = Postcode(value)
            self.assertTrue(postcode.is_valid())

    def test_is_valid_with_invalid_postcode(self):
        """Test the is_valid method
        the method should return False for an invalid postcode.
        """
        postcode = Postcode("TW1344TA")
        self.assertFalse(postcode.is_valid())

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

    def test_validate(self):
        """Test the validate method
        the method should return a formatted postcode if valid,
        formatted to uppercase with all whitespace removed.
        if not valid, the method should return False.
        """
        test_values = {
            "ec1a 1bb": "EC1A1BB",
            " ec1a1bb": "EC1A1BB",
            "ec1a1bb ": "EC1A1BB",
            "ec1a 1bb ": "EC1A1BB",
            " ec1a 1bb": "EC1A1BB",
            " ec1a    1bb ": "EC1A1BB",
            " e c 1 a 1 b b ": "EC1A1BB",
            "ecwrong": False,
            "ec1a1bbwrong": False,
            "ec1a1bb wrong": False,
            "ec1ab": False,
            "ec1a1b": False,
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.validate(), value)

    def test_validate_and_update(self):
        """Test the validate_and_update method

        the method should return a formatted postcode if valid,
        formatted to uppercase with all whitespace removed.
        if not valid, the method should return False.
        """
        test_values = {
            "ec1a 1bb": "EC1A1BB",
            "tw134ta": "TW134TA",
            "LL11 4BJ": "LL114BJ",
            "ecwrong": False,
            "ec1ab": False,
            "ec1a1b": False,
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.validate_and_update(), value)
            if value:
                self.assertEqual(postcode.postcode, value)

    def test_to_print(self):
        """Test the to_print method

        the method should return a formatted postcode if valid,
        formatted to uppercase with a single space between the outward code
        and inward code.
        if not valid, the method should return False.
        """
        test_values = {
            "ec1a 1bb": "EC1A 1BB",
            "tw134ta": "TW13 4TA",
            "LL11 4BJ": "LL11 4BJ",
            "ecwrong": False,
            "ec1ab": False,
            "ec1a1b": False,
        }
        for key, value in test_values.items():
            postcode = Postcode(key)
            self.assertEqual(postcode.to_print(), value)


if __name__ == "__main__":
    unittest.main()
