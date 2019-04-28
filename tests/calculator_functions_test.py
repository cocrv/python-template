import string
import unittest

from mock import Mock, MagicMock, patch
from context import calc_func
from random import randint, uniform, choice

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

class describe_add(unittest.TestCase):
    def test__it_shouldAddValues(self):
        expectedReturnValue = randomInteger + secondRandomInteger
        self.assertEqual(calc_func.add(randomInteger, secondRandomInteger), expectedReturnValue)

    def test__it_shouldNotAllowStrings(self):
        expectedReturnValue = "You must provide a number."
        self.assertEqual(calc_func.add(randomInteger, randomString), expectedReturnValue)

class describe_multiply(unittest.TestCase):
    def test__it_shouldMultiplyValues(self):
        expectedReturnValue = randomInteger * secondRandomInteger
        self.assertEqual(calc_func.multiply(randomInteger, secondRandomInteger), expectedReturnValue)

    def test__it_shouldNotAllowStrings(self):
        expectedReturnValue = "You must provide a number."
        self.assertEqual(calc_func.multiply(randomInteger, randomString), expectedReturnValue)

class describe_divide(unittest.TestCase):
    def test__it_shouldDivideValues(self):
        expectedReturnValue = randomFloat / secondRandomFloat
        self.assertEqual(calc_func.divide(randomFloat, secondRandomFloat), expectedReturnValue)

    def test__it_shouldNotAllowStrings(self):
        expectedReturnValue = "You must provide a number."
        self.assertEqual(calc_func.divide(randomInteger, randomString), expectedReturnValue)

    def test__it_shouldHandleDivideByZero(self):
        expectedReturnValue = "You can't divide by zero."
        self.assertEqual(calc_func.divide(randomFloat, 0), expectedReturnValue)

class describe_subtract(unittest.TestCase):
    def test__it_shouldSubtractValues(self):
        expectedReturnValue = randomFloat - secondRandomFloat
        self.assertEqual(calc_func.subtract(randomFloat, secondRandomFloat), expectedReturnValue)

    def test__it_shouldNotAllowStrings(self):
        expectedReturnValue = "You must provide a number."
        self.assertEqual(calc_func.subtract(randomInteger, randomString), expectedReturnValue)

if __name__=='__main__':
      unittest.main()
