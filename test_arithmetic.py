import unittest
from unittest import TestCase, SkipTest

from arithmetic import square


class Test_Square(TestCase):

    # examples:
    #   square(1) -> 1
    #   square(2) -> 4
    #   square(0) -> 0
    #   square(-5) -> 25
    #   square(0.5) -> 0.25
    #   square(0.1) -> 0.01
    #   square('number') -> error of some kind
    #   square(2j) -> -4 (notated as -4+0j) # might be a tough test case

    def test_square_natural_numbers(self):
        self.assertEqual(1, square(1))
        self.assertEqual(4, square(2))

    def test_square_nonnatural_integers(self):
        self.assertEqual(0, square(0))
        self.assertEqual(25, square(-5))

    def test_square_fractional_numbers(self):
        self.assertEqual(0.25, square(0.5))
        self.assertAlmostEqual(0.01, square(0.1))

    @SkipTest
    def test_square_error_cases(self):
        self.fail()

    @SkipTest
    def test_square_imaginary_numbers(self):
        self.fail()
