
# JSON Verifier

## The general description

A program containing a method **verifying the input JSON data**.

Input:
- data format is defined as AWS::IAM::Role Policy - definition can be found [here](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-iam-role-policy.html)
- Input JSON is read from a file. 

JSON example:
JSON
```
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
```
## Details of implementation
Language: Python

Version: 3.10

Modules used: json

## Logic of the program

The boolean output of this JSON classifier is based on a single condition.
| The condition for JSON classification |
| ---------------------- |
| returns logical False if an input JSON Resource field contains a single asterisk |
| returns True in any other case |

## Project structure

| purpose | module |
| ----------- | ----------- |
| logic of the program | main.py |
| covering edge cases | edge_cases.py |
| unit testing functionality | unit_tests.py |

## Running the program
To use functionality of the JSON classifier:
1. Navigate to the directory where You saved main.py
2. Run the main.py module and write the path to your JSON file:
```console
JSON_verifier:~$ python3 main.py
Please enter the path to your JSON file: path_to_JSON/my_JSON.json
```
3. The output will be a corresponding boolean value:
```console
JSON_verifier:~$ python3 main.py
Please enter the path to your JSON file: path_to_JSON/my_JSON.json
True
```
