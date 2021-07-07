import unittest
from converter import *

class TestConverter(unittest.TestCase):

    def test_same_result(self):
        test_value=input("enter test text\n")
        self.assertEqual(convert_text_using_loop_method(test_value),convert_text_using_lower_method(test_value))