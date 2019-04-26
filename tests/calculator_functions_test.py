import string

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

def describe_add():
    def it_shouldAddValues():
        expectedReturnValue = randomInteger + secondRandomInteger
        assert calc_func.add(randomInteger, secondRandomInteger) == expectedReturnValue

    def it_shouldNotAllowStrings():
        expectedReturnValue = "You must provide a number."
        assert calc_func.add(randomInteger, randomString) == expectedReturnValue

def describe_muliply():
    def it_shouldMultiplyValues():
        expectedReturnValue = randomInteger * secondRandomInteger
        assert calc_func.multiply(randomInteger, secondRandomInteger) == expectedReturnValue

    def it_shouldNotAllowStrings():
        expectedReturnValue = "You must provide a number."
        assert calc_func.multiply(randomInteger, randomString) == expectedReturnValue

def describe_divide():
    def it_shouldDivideValues():
        expectedReturnValue = randomFloat / secondRandomFloat
        assert calc_func.divide(randomFloat, secondRandomFloat) == expectedReturnValue

    def it_shouldNotAllowStrings():
        expectedReturnValue = "You must provide a number."
        assert calc_func.divide(randomInteger, randomString) == expectedReturnValue

    def it_shouldHandleDivideByZero():
        expectedReturnValue = "You can't divide by zero."
        assert calc_func.divide(randomFloat, 0) == expectedReturnValue

def describe_subtract():
    def it_shouldSubtractValues():
        expectedReturnValue = randomFloat - secondRandomFloat
        assert calc_func.subtract(randomFloat, secondRandomFloat) == expectedReturnValue

    def it_shouldNotAllowStrings():
        expectedReturnValue = "You must provide a number."
        assert calc_func.subtract(randomInteger, randomString) == expectedReturnValue

