import inspect
import unittest



from converter import *


test_list = [("Hello there","HeLlO tHeRe"), ("hello there","hello there"), ("HELLO THERE","HELLO THERE"),
             ("HeLlO ThErE","heLLO THERE"), ("","")]


class TestConverter(unittest.TestCase):
    def setUp(self):
        self.logPoint()
        self.string = "this is a test string"


    def test_same_result(self):
        #TEST FIXTURE - TEST SCOPE
        self.logPoint()
        self.assertEqual(convert_text_using_loop_method(self.string),convert_text_using_lower_method(self.string))

        #TEST PARAMETRIZATION
        for p1,p2 in test_list:
            with self.subTest():
                self.assertEqual(convert_text_using_loop_method(p1),convert_text_using_lower_method(p2))

    def tearDown(self) -> None:
        self.logPoint()


    def logPoint(self):
        currentTest = self.id().split('.')[-1]
        callingFunction = inspect.stack()[1][3]
        print('in %s - %s()' % (currentTest, callingFunction))