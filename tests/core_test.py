from context import core
from random import randint, uniform

randomInteger = randint(0,999)
secondRandomInteger = randint(0,999)
randomFloat = uniform(0, 999)
secondRandomFloat = uniform(0,999)

def test_addShouldAddValues():
    expectedReturnValue = randomInteger + secondRandomInteger
    assert core.add(randomInteger, secondRandomInteger) == expectedReturnValue

def test_multiplyShouldMultiplyValues():
    expectedReturnValue = randomInteger * secondRandomInteger
    assert core.multiply(randomInteger, secondRandomInteger) == expectedReturnValue

def test_divideShouldDivideValues():
    expectedReturnValue = randomFloat / secondRandomFloat
    assert core.divide(randomFloat, secondRandomFloat) == expectedReturnValue

def test_subtractShouldSubtractValues():
    expectedReturnValue = randomFloat - secondRandomFloat
    assert core.subtract(randomFloat, secondRandomFloat) == expectedReturnValue
