import unittest
from unittest.mock import mock_open, patch
from main import verify_json_data
import json

# replacing open by mock_open, simulating an input read from file
class TestVerifyJsonData(unittest.TestCase):
    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({}))
    def test_empty_input(self, mock_file):
        self.assertTrue(verify_json_data('my_path'))


    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        "PolicyDocument": {
            "Statement": [
                {
                    "Resource": "*"
                }
            ]
        }
    }))
    def test_resource_field_is_single_asterisk(self, mock_file):
        self.assertFalse(verify_json_data('my_path'))


    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        "PolicyDocument": {
            "Statement": [
                {
                    "Resource": "sth_else_*"
                }
            ]
        }
    }))
    def test_resource_field_is_str_but_not_single_asterisk(self, mock_file):
        self.assertTrue(verify_json_data('my_path'))


    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        "PolicyDocument": {
            "Statement": [
                {
                    "Action": [
                        "iam:ListRoles",
                        "iam:ListUsers"
                    ]
                }
            ]
        }
    }))
    def test_no_statement_or_no_resource(self, mock_file):
        self.assertTrue(verify_json_data('my_path'))


    @patch('builtins.open', new_callable=mock_open, read_data=json.dumps({
        "PolicyDocument": {
            "Statement": [
                {
                    "Resource": "sth_else_*"
                },
                {
                    "Resource": "*"
                }
            ]
        }
    }))
    def test_many_statements_different_resources_at_least_one_is_asterisk(self, mock_file):
        self.assertFalse(verify_json_data('my_path'))



if __name__ == '__main__':
    unittest.main()
