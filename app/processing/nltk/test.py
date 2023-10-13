import unittest

from processing.nltk.email import getEmailFromString
from processing.nltk.phone import getPhoneFromString

class TestRegexStringParsing(unittest.TestCase):
    def test_single_email(self):
        text = "Please contact me at john@example.com"
        expected = ["john@example.com"]
        self.assertEqual(getEmailFromString(text), expected)

    def test_multiple_emails(self):
        text = "Please contact me at john@example.com or jane@example.com"
        expected = ["john@example.com", "jane@example.com"]
        self.assertEqual(getEmailFromString(text), expected)

    def test_no_email(self):
        text = "Please contact me via phone"
        expected = []
        self.assertEqual(getEmailFromString(text), expected)

    def test_email_with_special_characters(self):
        text = "Please contact me at john.doe+test@example.com"
        expected = ["john.doe+test@example.com"]
        self.assertEqual(getEmailFromString(text), expected)

    def test_getPhoneFromString_with_us_numbers(self):
        text = "My phone number is 123-456-7890. Call me anytime."
        expected_output = ['123-456-7890']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_us_numbers_with_period(self):
        text = "Please call me at 555.123.4567 or 555-987-6543"
        expected_output = ['555.123.4567', '555-987-6543']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_uk_numbers(self):
        text = "My phone number is 020 1234 5678. Call me anytime."
        expected_output = ['020 1234 5678']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_ukplus_numbers(self):
        text = "Please call me at +44 7911 123456 or 07911 123456"
        expected_output = ['+44 7911 123456', '07911 123456']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_parameterized_numbers(self):
        text = "My phone number is (123) 456-7890. Call me anytime."
        expected_output = ['(123) 456-7890']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_extension_numbers(self):
        text = "Please call me at 555-123-4567 ext. 1234"
        expected_output = ['555-123-4567 ext. 1234']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_no_numbers(self):
        text = "No phone number in this text."
        expected_output = []
        self.assertEqual(getPhoneFromString(text), expected_output)
