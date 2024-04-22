"""
This program contains method verifying the input JSON data.

Input data format is defined as:
AWS::IAM::Role Policy
Input JSON might be read from a file.

Method returns:
False - if an input JSON Resource field
contains a single asterisk
True - in any other case. 

Language of implementation: Python
JSON example:

{
    "PolicyName": "root",
    "PolicyDocument": {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "IamListAccess",
                "Effect": "Allow",
                "Action": [
                    "iam:ListRoles",
                    "iam:ListUsers"
                ],
                "Resource": "*"
            }
        ]
    }
}

"""


import json

def verify_json_data(file):
    with open(file, 'r') as f:
        data = json.load(f)
        policy_doc_dct = data.get('PolicyDocument', {})
        statement_ls = policy_doc_dct.get('Statement', [])


        for statement in statement_ls:
            # looking for "Resource": "*"
            # if statements list is non-empty
            if statement.get('Resource') == '*':
                return False
    return True

