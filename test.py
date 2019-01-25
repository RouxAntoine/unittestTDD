#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from fizzbuzz.FizzBuzz import FizzBuzzClass


class TestFizzBuzzLibrary(unittest.TestCase):

    FIZZ_CONST = "Fizz"
    BUZZ_CONST = "Buzz"

    def test_should_return_one_for_one(self):
        self.assertEqual(1, FizzBuzzClass.evaluate(1), "FizzBuzz.evaluate(1) should return 1")
    

    def test_should_return_two_For_two(self):
        self.assertEqual(2, FizzBuzzClass.evaluate(2), "FizzBuzz.evaluate(2) should return 2")


    def test_should_return_fizz_For_three(self):
        self.assertEqual(self.FIZZ_CONST, FizzBuzzClass.evaluate(3), "FizzBuzz.evaluate(3) should return Fizz")



    # def test_isupper(self):
    #     self.assertTrue('FOO'.isupper())
    #     self.assertFalse('Foo'.isupper())

    # def test_split(self):
    #     s = 'hello world'
    #     self.assertEqual(s.split(), ['hello', 'world'])
    #     # check that s.split fails when the separator is not a string
    #     with self.assertRaises(TypeError):
    #         s.split(2)



if __name__ == '__main__':
    unittest.main()