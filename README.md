## Postcode_validator

A python library to format and validate UK postcodes.

The library provides a Postcode class that requires a postcode string to instantiate. Passing the class a data-type other than a string will return a TypeError.

The library utilises a Regular Expression to perform the validation. The Regular Expression used for the purposes of validation includes UK postcode formats and special cases. Full details can be found [here.](https://en.wikipedia.org/wiki/Postcodes_in_the_United_Kingdom#Validation)

```Regular Expression
^(([A-Z]{1,2}[0-9][A-Z0-9]?|ASCN|STHL|TDCU|BBND|[BFS]IQQ|PCRN|TKCA) ?[0-9][A-Z]{2}|BFPO ?[0-9]{1,4}|(KY[0-9]|MSR|VG|AI)[ -]?[0-9]{4}|[A-Z]{2} ?[0-9]{2}|GE ?CX|GIR ?0A{2}|SAN ?TA1)$
```

### Usage

The postcodelib.postcode library contains a Postcode class. The class can be instantiated by passing in a postcode as a string. E.g.

```python
inputted_postcode = Postcode("TW134TA")
```

#### Attributes

postcode: `str` - a string representing the UK postcode.

#### Methods

| Method                | Returns                          | Explanation                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| --------------------- | -------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| is_valid()            | boolean                          | Checks the postcode object contains a valid UK postcode, this method does not format the value in anyway.                                                                                                                                                                                                                                                                                                                                                                                        |
| remove_whitespace()   | string                           | Remove all whitespace from the postcode string. E.g. `" TW 13 4 TA "` would return as `"TW134TA"`.                                                                                                                                                                                                                                                                                                                                                                                               |
| format()              | string                           | Format a postcode string to uppercase with all whitespace removed. E.g. `"t w 13 4 ta"` would return as `"TW134TA"`.                                                                                                                                                                                                                                                                                                                                                                             |
| outward_code()        | string                           | Extract the outward code from a postcode string. E.g. `"TW134TA"` would return `"TW13"`.                                                                                                                                                                                                                                                                                                                                                                                                         |
| inward_code()         | string                           | Extract the inward code from a postcode string. E.g. `"TW134TA"` would return `"4TA"`.                                                                                                                                                                                                                                                                                                                                                                                                           |
| validate()            | string if valid, bool if invalid | Validate a postcode string, this method will format the postcode string into uppercase and remove all whitespace before attempting validation. If the formatted string is a valid UK postcode, it will return the formatted string. E.g. `" tw13 4t  a"` would return `"TW134TA"`. If the formatted string is not a valid postcode, it will return `False`.                                                                                                                                      |
| validate_and_update() | string if valid, bool if invalid | Validate a postcode string and update the postcode attribute. This method will format the postcode string into uppercase and remove all whitespace before attempting validation. If the formatted string is a valid UK postcode, it will update the postcode string stored within the object to the formatted string, before returning the formatted postcode string. E.g. `" tw13 4t  a"` would return `"TW134TA"`. If the formatted string is not a valid UK postcode, it will return `False`. |
| to_print()            | string if valid, bool if invalid | Insert a space between the outward code and the inward code. This method will take the stored postcode string, format it into uppercase and remove all whitespace before attempting validation. If the formatted string is a valid UK postcode, it will insert a single space prior to the final three characters of the string, taking a string such as `"tw134ta"` and returning `"TW13 4TA"`.                                                                                                 |

### Unit Tests

To run the tests within the tests folder, clone the repository locally.
Within the terminal, navigate to the postcode_validator directory.
On a Windows machine, enter the following command in the terminal.

```
py -m unittest tests/test_postcode.py
```

For a Mac or Linux machine, you might need to specify 'python3' at the start

```
python3 -m unittest tests/test_postcode.py
```

Test coverage was monitored using the `coverage` package. To install the package, run `pip install coverage` in the terminal from the project root directory. To run the test suite with coverage, use the following command in a Windows terminal from the project root directory.

```
coverage run -m unittest discover
```

This enables the coverage package to collate information on which parts of the program have been executed. To view a report of the results in the terminal you can use `coverage report`. To view the results in a browser use `coverage html`. This will create a `"htmlcov/"` directory containing a number of files, open the `"htmlcov/index.html"` file in your browser to view the results.

### Build as a library

To build the project as a library, ready to upload to PyPi you will need to install the build package from pip, this will install colorama, packaging and pyproject_hooks as well.
To install the packages run the following command in the project root directory within your windows terminal

```
pip install -r requirements.txt
```

then once the packages are successfully installed, run the following command on a Windows machine

```
py -m build
```

or on a Mac or Linux machine

```
python3 -m build
```

This command will generate two files and place them in a new `dist/` directory.
The `tar.gz` file is a source distribution whereas the `.whl` file is a built distribution.
