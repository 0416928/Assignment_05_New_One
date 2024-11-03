"""
Description: This program will test the functions by using unittest.
Author: Gaganpreet Kaur
Date: November 3,2024
Usage: Testing the functions.
"""

import unittest
from src.chatbot import get_account, get_amount
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

    def test_get_amount_valid_number(self):
        # arrange
        with patch('builtins.input') as mock_input:
             mock_input.side_effect = ["500.01"]
             expected = 500.01
         # act
             actual = get_amount()
         # assert
             self.assertEqual(expected,actual)


    def test_get_amount_non_numeric_amount(self):
        # arrange
        with patch('builtins.input') as mock_input:
            mock_input.side_effect = ["non-numeric_data"]
            expected = "Invalid amount. Amount must be numeric."
            # act and assert
            with self.assertRaises(ValueError) as context:
                get_amount()
                self.assertEqual(expected,str(context.exception))

    def test_get_amount_invalid_data(self):
        # arrange
        with patch('builtins.input') as mock_input:
             mock_input.side_effect = ["0"]
             expected = "Invalid amount. Please enter a positive number."
             # act and assert
             with self.assertRaises(ValueError) as context:
                get_amount()
                self.assertEqual(expected,str(context.exception))

