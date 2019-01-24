#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import unittest
from fizzbuzz.FizzBuzz import FizzBuzzClass


class TestFizzBuzzLibrary(unittest.TestCase):

    def test_should_return_one_for_one(self):
        print(FizzBuzzClass)

        self.assertEqual(1, FizzBuzzClass.evaluate(1), "FizzBuzz.evaluate(1) should return 1")
        # self.assertEqual('foo'.upper(), 'FOO')

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