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
        self.postcode = postcode

    def validate(self):
        """Validate a postcode
        ---
        Returns
        -------
        bool
            True if the postcode is valid, False otherwise
        """
        return bool(re.match(Rules.UK, self.postcode))
