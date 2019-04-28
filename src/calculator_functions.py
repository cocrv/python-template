from .helpers import isString

def add(x, y):
    if isString(x, y):
        return "You must provide a number."
    else:
        return x + y

def multiply(x, y):
    if isString(x, y):
        return "You must provide a number."
    else:
        return x * y

def divide(x, y):
    if isString(x, y):
        return "You must provide a number."
    elif y == 0:
        return "You can't divide by zero."
    else:
        return x / y

def subtract(x, y):
    if isString(x, y):
        return "You must provide a number."
    else:
        return x - y
