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

    def validate(self):
        """Validate a postcode
        ---
        Returns
        -------
        bool
            True if the postcode is valid, False otherwise
        """
        return bool(re.match(Rules.UK, self.postcode))
