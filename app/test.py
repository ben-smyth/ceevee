import unittest

from processing.spacy.test import TestSpacyStringParsing
from processing.nltk.test import TestRegexStringParsing

class CustomTextTestResult(unittest.TextTestResult):
    def addSuccess(self, test):
        super().addSuccess(test)
        print(f"\033[92m✓\033[0m {test.id()}")

    def addFailure(self, test, err):
        super().addFailure(test, err)
        print(f"\033[91m✗\033[0m {test.id()}")


if __name__ == '__main__':
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TestSpacyStringParsing))
    test_suite.addTest(unittest.makeSuite(TestRegexStringParsing))
    runner = unittest.TextTestRunner(failfast=False, resultclass=CustomTextTestResult)
    runner.run(test_suite)