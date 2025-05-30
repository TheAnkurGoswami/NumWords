import unittest
import sys
import os

# Add the project root to sys.path to allow direct import of NumWords
# This assumes tests are run from the project root or that the NumWords package is in PYTHONPATH
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.insert(0, project_root)

from NumWords.core import NumWords

class TestTextToNumber(unittest.TestCase):
    def test_simple_numbers(self):
        self.assertEqual(NumWords.convert("zero"), 0)
        self.assertEqual(NumWords.convert("one"), 1)
        self.assertEqual(NumWords.convert("nineteen"), 19)
        self.assertEqual(NumWords.convert("twenty"), 20)
        self.assertEqual(NumWords.convert("fifty five"), 55)
        self.assertEqual(NumWords.convert("ninety nine"), 99)

    def test_hundreds(self):
        self.assertEqual(NumWords.convert("one hundred"), 100)
        self.assertEqual(NumWords.convert("two hundred five"), 205)
        self.assertEqual(NumWords.convert("nine hundred ninety nine"), 999)
        self.assertEqual(NumWords.convert("three hundred"), 300)

    def test_thousands(self):
        self.assertEqual(NumWords.convert("one thousand"), 1000)
        self.assertEqual(NumWords.convert("two thousand three hundred"), 2300)
        self.assertEqual(NumWords.convert("five thousand sixty"), 5060) # "five thousand sixty"
        self.assertEqual(NumWords.convert("ten thousand one"), 10001)
        self.assertEqual(NumWords.convert("twelve thousand three hundred forty five"), 12345) # Using "forty"
        self.assertEqual(NumWords.convert("nine hundred ninety nine thousand nine hundred ninety nine"), 999999)

    def test_millions(self):
        self.assertEqual(NumWords.convert("one million"), 1000000)
        self.assertEqual(NumWords.convert("two million five hundred thousand"), 2500000)
        self.assertEqual(NumWords.convert("one million one"), 1000001)
        self.assertEqual(NumWords.convert("one hundred million two hundred thousand fifty"), 100200050)

    def test_billions(self):
        self.assertEqual(NumWords.convert("one billion"), 1000000000)
        self.assertEqual(NumWords.convert("two billion one hundred million"), 2100000000)

    def test_large_numbers(self):
        self.assertEqual(NumWords.convert("one trillion"), 1000000000000)
        # Assuming VIGINTILLION is the max in mappings
        self.assertEqual(NumWords.convert("one vigintillion"), 10**63)


    def test_negative_numbers(self):
        self.assertEqual(NumWords.convert("minus ten"), -10)
        self.assertEqual(NumWords.convert("minus one hundred twenty three"), -123)
        self.assertEqual(NumWords.convert("minus one million"), -1000000)
        self.assertEqual(NumWords.convert("minus fifty five"), -55)

    def test_case_insensitivity_and_spacing(self):
        self.assertEqual(NumWords.convert("  ONE HUNDRED   "), 100)
        self.assertEqual(NumWords.convert("minus TWENTY two"), -22)
        self.assertEqual(NumWords.convert("   Minus forty five THOUSAND six HUNDRED SEVENty EIGHT      "), -45678)

    def test_edge_cases(self):
        self.assertEqual(NumWords.convert("zero"), 0)
        self.assertEqual(NumWords.convert("minus zero"), 0) # int(0) is 0, not -0
        self.assertEqual(NumWords.convert("thousand"), 1000)
        self.assertEqual(NumWords.convert("million"), 1000000)
        self.assertEqual(NumWords.convert("hundred"), 100)
        self.assertEqual(NumWords.convert("minus hundred"), -100)
        self.assertEqual(NumWords.convert("minus thousand"), -1000)

    def test_problematic_cases_from_implementation_details(self):
        # "hundred five" -> 105
        self.assertEqual(NumWords.convert("hundred five"), 105)
        self.assertEqual(NumWords.convert("minus hundred five"), -105)
        # "thousand five" -> 1005
        self.assertEqual(NumWords.convert("thousand five"), 1005)
        # "one hundred thousand" -> 100000
        self.assertEqual(NumWords.convert("one hundred thousand"), 100000)


if __name__ == '__main__':
    unittest.main()
