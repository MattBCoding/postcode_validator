## Postcode_validator

A python library to format and validate UK postcodes

## Unit Tests

To run the tests within the tests folder, clone the repository locally.
Within the terminal, navigate to the postcode_validator directory.
On a Windows machine, enter the following command in the terminal.

```
python -m unittest tests/test_postcode.py
```

For a Mac or Linux machine, you might need to specify 'python3' at the start

```
python3 -m unittest tests/test_postcode.py
```

## Build as a library

To build the project as a library, ready to upload to PyPi you will need to install the build package from pip, this will install colorama, packaging and pyproject_hooks as well.
To install the packages run the following command in the root directory within your windows terminal

```
pip install -r requirements.txt
```
