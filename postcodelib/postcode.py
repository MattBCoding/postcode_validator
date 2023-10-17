from postcodelib.validation_rules import Rules


class Postcode:
    """A class to represent a postcode
    ---
    Attributes
    ----------
    postcode : str
        a postcode
    """

    def __init__(self, postcode: str):
        self.postcode = postcode
