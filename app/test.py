import unittest

from processing.spacy.name import getNameFromString
from processing.nltk.email import getEmailFromString
from processing.nltk.phone import getPhoneFromString

class TestStringParsing(unittest.TestCase):
    def test_getNameFromString(self):
        self.assertEqual(getNameFromString("My name is John Smith"), ["John Smith"])

    def test_getNameFromString_with_hello(self):
        self.assertEqual(getNameFromString("Hello, my name is Jane Doe"),["Jane Doe"])

    def test_getNameFromString_with_book_author(self):
        self.assertEqual(getNameFromString("The author of this book is J.K. Rowling"), ["J.K. Rowling"])

    def test_getNameFromString_with_ceo(self):
        self.assertEqual(getNameFromString("The CEO of Microsoft is Satya Nadella"),["Satya Nadella"])

    def test_getNameFromString_with_actor(self):
        self.assertEqual(getNameFromString("The famous actor Tom Hanks starred in the movie Forrest Gump"),["Tom Hanks"])

    def test_getNameFromString_with_singer(self):
        self.assertEqual(getNameFromString("The singer Beyonce Knowles is known for her hit songs"),["Beyonce Knowles"])

    def test_getNameFromString_with_artist(self):
        self.assertEqual(getNameFromString("The artist Vincent van Gogh painted Starry Night"),["Vincent van Gogh"])

    def test_getNameFromString_with_author(self):
        self.assertEqual(getNameFromString("The author Ernest Hemingway wrote The Old Man and the Sea") ,["Ernest Hemingway"])

    def test_getNameFromString_with_physicist(self):
        self.assertEqual(getNameFromString("The physicist Albert Einstein is famous for his theory of relativity"),["Albert Einstein"])

    def test_getNameFromString_with_actress(self):
        self.assertEqual(getNameFromString("The actress Meryl Streep has won multiple Academy Awards"),["Meryl Streep"])

    def test_getNameFromString_with_musician(self):
        self.assertEqual(getNameFromString("The musician Freddie Mercury was the lead singer of Queen"),["Freddie Mercury"])
    
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

        text = "Please call me at 555.123.4567 or 555-987-6543"
        expected_output = ['555.123.4567', '555-987-6543']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_uk_numbers(self):
        text = "My phone number is 020 1234 5678. Call me anytime."
        expected_output = ['020 1234 5678']
        self.assertEqual(getPhoneFromString(text), expected_output)

        text = "Please call me at +44 7911 123456 or 07911 123456"
        expected_output = ['+44 7911 123456', '07911 123456']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_parameterized_numbers(self):
        text = "My phone number is (123) 456-7890. Call me anytime."
        expected_output = ['(123) 456-7890']
        self.assertEqual(getPhoneFromString(text), expected_output)

        text = "Please call me at 555-123-4567 ext. 1234"
        expected_output = ['555-123-4567 ext. 1234']
        self.assertEqual(getPhoneFromString(text), expected_output)

    def test_getPhoneFromString_with_no_numbers(self):
        text = "No phone number in this text."
        expected_output = []
        self.assertEqual(getPhoneFromString(text), expected_output)

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"\033[92m✓\033[0m {test.id()}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"\033[91m✗\033[0m {test.id()}")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestStringParsing))
    runner = unittest.TextTestRunner(failfast=False, resultclass=CustomTextTestResult)
    runner.run(test_suite)