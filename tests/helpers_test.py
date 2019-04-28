import string
import unittest

from random import randint, uniform, choice

from context import calc_func
from context import helpers

MIN_NUM = 0
MAX_NUM = 9999

MIN_CHAR = 10
MAX_CHAR = 15

randomInteger        = randint(MIN_NUM, MAX_NUM)
secondRandomInteger  = randint(MIN_NUM, MAX_NUM)
randomFloat          = uniform(MIN_NUM, MAX_NUM)
secondRandomFloat    = uniform(MIN_NUM, MAX_NUM)

allchar              = string.ascii_letters + string.punctuation + string.digits
randomString         = "".join(choice(allchar) for x in range(randint(MIN_CHAR, MAX_CHAR)))

class describe_isString(unittest.TestCase):
    def test__it_shouldReturnTrueIfFirstParameterIsAString(self):
        self.assertTrue(helpers.isString(randomString, randomInteger))

    def test__it_shouldReturnTrueIfSecondParameterIsAString(self):
        self.assertTrue(helpers.isString(randomFloat, randomString))

    def test__it_shouldReturnTrueIfBothParametersAreStrings(self):
        self.assertTrue(helpers.isString(randomString, randomString))

    def test__it_shouldReturnFalseIfNeitherParameterIsAString(self):
        self.assertFalse(helpers.isString(randomFloat, secondRandomFloat))

