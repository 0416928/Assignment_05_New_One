"""
Description: This program will test the functions by using unittest.
Author: Gaganpreet Kaur
Date: November 3,2024
Usage: Testing the functions.
"""

import unittest
from src.chatbot import get_account
from src.chatbot import VALID_TASKS, ACCOUNTS
from unittest.mock import patch

class TestChatbot(unittest.TestCase):

    def test_get_account_valid_data_first(self):
        # arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["123456"]
            expected = 123456
        # act
            actual1 = get_account()
        # assert
            self.assertEqual(expected , actual1)

    def test_get_account_non_numeric_data(self):
        # arrange
        with patch('builtins.input') as mock_input:
             mock_input.side_effect = ["non-numeric_data"]     
             expected = "Account number must be a whole number."

            # act and assert
             with self.assertRaises(ValueError) as context:
                get_account()
                self.assertEqual(expected,str(context.exception))

    def test_get_account_invalid_account_number(self):
        # arrange
        with patch('builtins.input') as mock_input:
             mock_input.side_effect = ["112233"]
             expected = "Account number entered does not exist."

            # act and assert
             with self.assertRaises(ValueError) as context:
                get_account()
                self.assertEqual(expected,str(context.exception))
