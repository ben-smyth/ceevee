import unittest

from processing.spacy.name import getNameFromString
from processing.spacy.phone import getPhoneFromString

class TestSpacyStringParsing(unittest.TestCase):
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
    

    def test_getPhoneFromString_with_us_numbers(self):
        text = "My phone number is 123-456-7890. Call me anytime."
        expected_output = ['123-456-7890']
        self.assertEqual(getPhoneFromString(text), expected_output)