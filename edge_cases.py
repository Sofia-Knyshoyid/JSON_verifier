"""
This module checks
the edge cases of input for main.py module.
"""
from main import verify_json_data

"""
Case 1: an empty input
Example: {}
Expected output: True
Program output: 
"""
json = {}
bool_res = verify_json_data(json)
assert(bool_res == True)

