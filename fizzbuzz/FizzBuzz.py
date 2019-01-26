#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class FizzBuzzClass:
    BUZZ = "Buzz"
    FIZZ = "Fizz"

    @classmethod
    def evaluate(self, x):
        "evaluate x then return x number or Fizz for multiple of 3 or Buzz for multiple of 5"
        res = x

        if FizzBuzzClass.isMultipleOfThree(x):
            res = FizzBuzzClass.FIZZ
        if FizzBuzzClass.isMultipleOfFive(x):
            res = FizzBuzzClass.BUZZ
        if FizzBuzzClass.isMultipleOfThree(x) and FizzBuzzClass.isMultipleOfFive(x):
            res = FizzBuzzClass.FIZZ + FizzBuzzClass.BUZZ

        return res

    @classmethod
    def isMultipleOfThree(self, v):
        "return true or false if @v is or isn't multiple of number three"
        return FizzBuzzClass.isMultipleOf(v, 3)

    @classmethod
    def isMultipleOfFive(self, v):
        "return true or false if @v is or isn't multiple of number five"
        return FizzBuzzClass.isMultipleOf(v, 5)

    @classmethod
    def isMultipleOf(self, value, multiple):
        "return true or false if @value is or isn't multiple of number @multiple"
        return value % multiple == 0
