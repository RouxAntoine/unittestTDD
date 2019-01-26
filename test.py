#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from fizzbuzz.FizzBuzz import FizzBuzzClass

class TestFizzBuzzLibrary(unittest.TestCase):

    FIZZ_CONST = "Fizz"
    BUZZ_CONST = "Buzz"

    def test_should_return_one_for_one(self):
        self.assertEqual(1, FizzBuzzClass.evaluate(1), "FizzBuzz.evaluate(1) should return 1")
    
    def test_should_return_two_for_two(self):
        self.assertEqual(2, FizzBuzzClass.evaluate(2), "FizzBuzz.evaluate(2) should return 2")

    def test_should_return_fizz_for_three(self):
        self.assertEqual(self.FIZZ_CONST, FizzBuzzClass.evaluate(3), "FizzBuzz.evaluate(3) should return 'Fizz'")

    def test_should_return_four_for_four(self):
        self.assertEqual(4, FizzBuzzClass.evaluate(4), "FizzBuzz.evaluate(4) should return 4")

    def test_should_return_Buzz_for_five(self):
        self.assertEqual(self.BUZZ_CONST, FizzBuzzClass.evaluate(5), "FizzBuzz.evaluate(5) should return 'Buzz'")

    def test_should_return_Fizz_for_six(self):
        self.assertEqual(self.FIZZ_CONST, FizzBuzzClass.evaluate(6), "FizzBuzz.evaluate(6) should return 'Fizz'")

    def test_should_return_seven_for_seven(self):
        self.assertEqual(7, FizzBuzzClass.evaluate(7), "FizzBuzz.evaluate(7) should return 7")

    def test_should_return_Buzz_for_ten(self):
        self.assertEqual(self.BUZZ_CONST, FizzBuzzClass.evaluate(10), "FizzBuzz.evaluate(10) should return 'Buzz'")
    
    def test_should_return_FizzBuzz_for_fifteen(self):
        self.assertEqual(self.FIZZ_CONST+self.BUZZ_CONST, FizzBuzzClass.evaluate(15), "FizzBuzz.evaluate(15) should return 'Fizz'+'Buzz'")

    # def test_exemple(self):
    #     self.assertFalse('Foo'.isupper())
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)

if __name__ == '__main__':
    unittest.main()