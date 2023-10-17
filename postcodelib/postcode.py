import re
from postcodelib.validation_rules import Rules


class Postcode:
    """A class to represent a postcode
    ---
    Parameters
    ----------
    postcode : str
        a postcode string
    """

    def __init__(self, postcode: str):
        self.postcode = self.validate_parameter(postcode)

    def __str__(self):
        return self.postcode

    def validate_parameter(self, postcode: str):
        """Validate the postcode parameter.
        -----
        Returns
        -------
        TypeError
            if the postcode parameter is not a string
        Sets the postcode attribute to the postcode parameter
            if the postcode parameter is a string
        """
        if type(postcode) == str:
            return postcode
        else:
            raise TypeError("The postcode parameter must be a string")

    def is_valid(self):
        """Validate a postcode
        ---
        Returns
        -------
        bool
            True if the postcode is valid, False otherwise
        """
        return bool(re.match(Rules.UK, self.postcode))

    def remove_whitespace(self):
        """Remove whitespace from a postcode
        ---
        Returns
        -------
        str
            the postcode with whitespace removed
        """
        return self.postcode.replace(" ", "")

    def format(self):
        """Format a postcode
        ---
        Returns
        -------
        str
            the postcode formatted to uppercase with whitespace removed
        """
        whitespace_removed = self.remove_whitespace()
        return whitespace_removed.upper()

    def outward_code(self):
        """Extract the outward code from a postcode
        ---
        Returns
        -------
        str
            the outward code of the postcode
            formatted to uppercase with whitespace removed
        """
        formatted_code = self.format()
        return formatted_code[:-3]

    def inward_code(self):
        """Extract the inward code from a postcode
        ---
        Returns
        -------
        str
            the inward code of the postcode
            formatted to uppercase with whitespace removed
        """
        formatted_code = self.format()
        return formatted_code[-3:]

    def validate(self):
        """Validates a postcode
        ---
        Returns
        -------
        str
            a formatted postcode if the postcode is valid,
            formatted to uppercase with whitespace removed.
        bool
            False if the postcode is invalid.
        """
        formatted_postcode = self.format()
        if bool(re.match(Rules.UK, formatted_postcode)):
            return formatted_postcode
        else:
            return False

    def validate_and_update(self):
        """Validates a postcode and updates the postcode attribute
        ---
        Returns
        -------
        str
            a formatted postcode if the postcode is valid,
            formatted to uppercase with whitespace removed.
        bool
            False if the postcode is invalid.
        """
        formatted_postcode = self.validate()
        if formatted_postcode:
            self.postcode = formatted_postcode
            return formatted_postcode
        else:
            return False

    def to_print(self):
        """Inserts a space between the outward code and the inward code
        ---

        Takes the postcode string, confirms validity, and inserts a space
        between the outward code and the inward code if valid.

        Returns
        -------
        str
            the postcode with a space inserted between the outward code
            and the inward code
        bool
            False if the postcode is invalid.
        """
        formatted_postcode = self.validate()
        if formatted_postcode:
            return formatted_postcode[:-3] + " " + formatted_postcode[-3:]
        else:
            return False
