from __future__ import print_function

"""
Define a function 'add' that accepts two numbers as arguments.
Return the sum of the two numbers.
"""
def add(num_1, num_2):
    return num_1 + num_2

"""
Define a function 'subtract' that accepts two numbers as arguments.
Return the subtraction of the two numbers
"""

def subtract (num_1, num_2):
    return num_1 - num_2

"""
Define a function 'integer_divide' that accepts two numbers as arguments.
Return the Integer Division of the two numbers.
Hint: https://www.w3schools.com/python/python_operators.asp
"""

def integer_divide(num_1, num_2):
    return num_1//num_2

"""
Define a function 'float_divide' that accepts two numbers as arguments.
Return the Float Division of the two numbers.
Hint: https://www.w3schools.com/python/python_operators.asp
"""

def float_divide(num_1, num_2):
    return num_1/num_2

"""
Define a function 'remainder_divide' that accepts two numbers as arguments.
Return the Remainder Division of the two numbers.
Hint: https://www.w3schools.com/python/python_operators.asp
"""

def remainder_divide(num_1, num_2):
    return num_1%num_2

"""
Define a function 'multiplication' that accepts two numbers as arguments.
Return the multiplication of the two numbers.
Hint: https://www.w3schools.com/python/python_operators.asp
"""

def multiplication(num_1, num_2):
    return num_1*num_2

"""
Define a function 'power' that accepts two numbers as arguments.
Return the power of the two numbers.
Hint: https://www.w3schools.com/python/python_operators.asp
"""

def power(num_1,num_2):
    return num_1**num_2

"""
Define a function 'convert_celsius_to_fahrenheit' that takes one argument, celsius.
Using your defined arithmetic functions above, calculate the conversion.
The formula is F = C * 1.8 + 32
"""

def convert_celcius_to_farenheit(cel):
    return add(multiplication(cel, 1.8), 32)

"""
Define a function 'convert_kilometers_to_miles' that takes one argument, kilometers.
Using your defined arithmetic functions above, calculate the conversion.
The formula is miles = kilometers * 0.6214
"""

def convert_kilogram_to_miles(k):
    return multiplication (k, 0.6214)

"""
Define a function 'calculate_bmi' that takes two arguments, weight and height.
Using your defined arithmetic functions above, calculate the bmi.
the formula is bmi = (weight * 703) / (height ^ 2)
"""

def calculate_bmi(weight, height):
    return float_divide(multiplication(weight, 783), power(height, 2))

"""
DO NOT TOUCH THE CODE BELOW
THIS CODE WILL TEST YOUR PROGRAM AND OUTPUT THE RESULTS
IF A TEST FAILS, YOUR CODE IS WRONG.
TO ACHIEVE MAXIMUM CREDIT ALL TESTS SHOULD PASS.
"""
import unittest

class TestCalculations(unittest.TestCase):
    def test_add(self):
        try:
            self.assertEqual(add(-1, 1), 0)
            self.assertEqual(add(1.5, 3.5), 5.0)
            self.assertEqual(add(99, 1), 100)
        except NameError:
            self.fail("Method 'add' not defined.")
        
    def test_sub(self):
        try:
            self.assertEqual(subtract(-1, 1), -2)
            self.assertEqual(subtract(100, 100), 0)
            self.assertEqual(subtract(12345, 1234), 11111)
        except NameError:
            self.fail("Method 'subtract' not defined")
        
    def test_integer_divide(self):
        try:
            self.assertEqual(integer_divide(3, 2), 1)
            self.assertEqual(integer_divide(10, 2), 5)
            self.assertTrue(type(integer_divide(3, 2)) is int)
        except NameError:
            self.fail("Method 'integer_divide' not defined")
        
    def test_float_divide(self):
        try:
            self.assertEqual(float_divide(3, 2), 1.5)
            self.assertEqual(float_divide(10, 2), 5.0)
            self.assertTrue(type(float_divide(3, 2)) is float)
        except NameError:
            self.fail("Method 'float_divide' not defined")
        
    def test_remainder_divide(self):
        try:
            self.assertEqual(remainder_divide(3, 2), 1)
            self.assertEqual(remainder_divide(1, 1), 0)
        except NameError:
            self.fail("Method 'remainder_divide' not defined")
        
    def test_multiplication(self):
        try:
            self.assertEqual(multiplication(-1, 2), -2)
            self.assertEqual(multiplication(2, 2), 4)
            self.assertEqual(multiplication(10000000, 0), 0)
        except NameError:
            self.fail("Method 'multiplication' not defined")
        
    def test_power(self):
        try:
            self.assertEqual(power(3, 3), 27)
            self.assertEqual(power(2, 2), 4)
            self.assertEqual(power(529, 0.5), 23)
        except NameError:
            self.fail("Method 'power' not defined")
        
    def test_convert_celsius_to_fahrenheit(self):
        try:
            self.assertEqual(convert_celsius_to_fahrenheit(20), 68)
            self.assertEqual(convert_celsius_to_fahrenheit(-40), -40)
            self.assertEqual(convert_celsius_to_fahrenheit(100), 212)
        except NameError:
            self.fail("Method 'convert_celsius_to_fahrenheit' not defined")
        
    def test_convert_kilometers_to_miles(self):
        try:
            self.assertEqual(convert_kilometers_to_miles(1), 0.6214)
            self.assertAlmostEqual(convert_kilometers_to_miles(10), 6.2140, places=4)
            self.assertAlmostEqual(convert_kilometers_to_miles(0.01), 0.0062, places=4)
        except NameError:
            self.fail("Method 'convert_kilometers_to_miles' not defined")
        
    def test_calculate_bmi(self):
        try:
            self.assertAlmostEqual(calculate_bmi(150, 65), 24.96, places=2)
        except NameError:
            self.fail("Method 'calculate_bmi' not defined")
        
if __name__ == '__main__':
    unittest.main()