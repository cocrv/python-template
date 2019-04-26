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

def test_add_ShouldAddValues():
    expectedReturnValue = randomInteger + secondRandomInteger
    assert calc_func.add(randomInteger, secondRandomInteger) == expectedReturnValue

def test_add_ShouldNotAllowStrings():
    expectedReturnValue = "You must provide a number."
    assert calc_func.add(randomInteger, randomString) == expectedReturnValue

def test_multiply_ShouldMultiplyValues():
    expectedReturnValue = randomInteger * secondRandomInteger
    assert calc_func.multiply(randomInteger, secondRandomInteger) == expectedReturnValue

def test_multiply_ShouldNotAllowStrings():
    expectedReturnValue = "You must provide a number."
    assert calc_func.multiply(randomInteger, randomString) == expectedReturnValue

def test_divide_ShouldDivideValues():
    expectedReturnValue = randomFloat / secondRandomFloat
    assert calc_func.divide(randomFloat, secondRandomFloat) == expectedReturnValue

def test_divide_ShouldNotAllowStrings():
    expectedReturnValue = "You must provide a number."
    assert calc_func.divide(randomInteger, randomString) == expectedReturnValue

def test_divide_ShouldHandleDivideByZero():
    expectedReturnValue = "You can't divide by zero."
    assert calc_func.divide(randomFloat, 0) == expectedReturnValue

def test_subtract_ShouldSubtractValues():
    expectedReturnValue = randomFloat - secondRandomFloat
    assert calc_func.subtract(randomFloat, secondRandomFloat) == expectedReturnValue

def test_subtract_ShouldNotAllowStrings():
    expectedReturnValue = "You must provide a number."
    assert calc_func.subtract(randomInteger, randomString) == expectedReturnValue

