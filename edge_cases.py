"""
This module checks
the edge cases of input for main.py module.

It presents the modified version of verify_json_data,
which takes into account the corner cases described.

The condition for checking input data is:
    Method returns:
    False - if an input JSON Resource field
    contains a single asterisk
    True - in any other case. 

"""

"""

--- Part 1: edge cases already covered in main.py:


Case 1: an empty input
    Expected output: True
    (no Resource field -> no single asterisk as a value)
    Program output: True

Case 2: Resource field is a single asterisk
    Expected output: False
    Program output: False

Case 3: Resource field is str, but not a single asterisk
    Expected output: True
    Program output: True

Case 4: no Statement/ no Resource
    Expected output: True
    Program output: True

    
Case 5: many Statements - different Resources (at least 1 is *)
    Expected output: False
    Program output: False

Case 6: many Statements - one Resource (is a  single *)
    Expected output: False
    Program output: False


--- Part 2: Cases that should be implemented (aren't covered in main.py)

Case 7: Resource is not a string:
    Example: "Resource": 0
    Expected output:
    Program output:

Case 8: 1 Statement - many Resources (for instance list):
    Example: "Resource": ["sth_else", "*"]
    Expected output:
    Program output:

Case 9: Invalid path:
    Expected output;
    Program output:

Case 10: big JSON File (can't load the whole file at once):
    Expected output:
    Program output:

Case 11: Invalid JSON file (empty, invalid syntax)




"""




import json
import os


def verify_json_data(file):
    """
    Modified version of JSON classifier from main.py
    """
    # Case 9: Invalid path
    if not os.path.exists(file):
        raise FileNotFoundError("Error: Invalid path")

    try:
        with open(file, 'r') as f:
            # Case 10: big JSON File
            # loading the file line by line
            for line in f:
                data = json.loads(line)
                policy_doc_dct = data.get('PolicyDocument', {})
                statement_ls = policy_doc_dct.get('Statement', [])

                for statement in statement_ls:
                    resource = statement.get('Resource')
                    # Case 7: Resource is not a string
                    if not isinstance(resource, str):
                        raise TypeError("Error: Resource is not a string")
                    # Case 8: 1 Statement - many Resources (for instance list)
                    if isinstance(resource, list) and '*' in resource:
                        raise ValueError("Error: one Statement and many Resources")

                    if resource == '*':
                        return False
    except json.JSONDecodeError:
        # Case 11: Invalid JSON file (empty, invalid syntax)
        raise json.JSONDecodeError("Error: Invalid JSON file (empty, invalid syntax, etc)")

    return True


