"""
Author: Matthew Kane
File: triangle_test.py
Purpose: Unit tests for the Triangle class.
Credit: Based on Nick Russo's "Learning Python by Example" online course on oreilly.com
"""

from unittest import TestCase
from shapes.triangle import Triangle


class TriangleTest(TestCase):
    """
    Defines a test case for the Triangle class.
    """
    def setUp(self):
        """
        Create a few test Triangle objects.
        """
        self.sides745 = Triangle(7, 4, 5)  # scalene
        self.sides555 = Triangle(5, 5, 5)  # equilateral and isosceles
        self.sides883 = Triangle(8, 8, 3)  # isosceles (sides 1 and 2 equal)
        self.sides266 = Triangle(2, 6, 6)  # isosceles (sides 2 and 3 equal)
        self.sides747 = Triangle(7, 4, 7)  # isosceles (sides 1 and 3 equal)
        self.sides543 = Triangle(5, 4, 3)  # scalene and right angle, hypotenuse is side1
        self.sides686 = Triangle(6, 8.48528, 6)  # right angle and isosceles, hypotenuse is side2
        self.sides738 = Triangle(7.5, 3.5, 8.27647)  # scalene and right angle, hypotenuse is side3

    def test_sides(self):
        """
        Compare the test triangle sides to the actual values
        """
        self.assertEqual(self.sides745.sides(), (7, 4, 5))
        self.assertEqual(self.sides555.sides(), (5, 5, 5))
        self.assertEqual(self.sides883.sides(), (8, 8, 3))
        self.assertEqual(self.sides266.sides(), (2, 6, 6))
        self.assertEqual(self.sides747.sides(), (7, 4, 7))
        self.assertEqual(self.sides543.sides(), (5, 4, 3))
        self.assertEqual(self.sides686.sides(), (6, 8.48528, 6))
        self.assertEqual(self.sides738.sides(), (7.5, 3.5, 8.27647))

    def test_perimeter(self):
        """
        Compare the test triangle perimeter computations to the actual values
        """
        self.assertEqual(self.sides745.perimeter(), 16.00000)
        self.assertEqual(self.sides555.perimeter(), 15.00000)
        self.assertEqual(self.sides883.perimeter(), 19.00000)
        self.assertEqual(self.sides266.perimeter(), 14.00000)
        self.assertEqual(self.sides747.perimeter(), 18.00000)
        self.assertEqual(self.sides543.perimeter(), 12.00000)
        self.assertEqual(self.sides686.perimeter(), 20.48528)
        self.assertEqual(self.sides738.perimeter(), 19.27647)

    def test_height(self):
        """
        Compare the test triangle height computations to the actual values
        """
        self.assertEqual(self.sides745.heights(), (2.79942, 4.89898, 3.91918))
        self.assertEqual(self.sides555.heights(), (4.33013, 4.33013, 4.33013))
        self.assertEqual(self.sides883.heights(), (2.94679, 2.94679, 7.85812))
        self.assertEqual(self.sides266.heights(), (5.91608, 1.97203, 1.97203))
        self.assertEqual(self.sides747.heights(), (3.83326, 6.70820, 3.83326))
        self.assertEqual(self.sides543.heights(), (2.40000, 3.00000, 4.00000))
        self.assertEqual(self.sides686.heights(), (6.00000, 4.24264, 6.00000))
        self.assertEqual(self.sides738.heights(), (3.50000, 7.50000, 3.17164))

    def test_area(self):
        """
        Compare the test triangle area computations to the actual values
        """
        self.assertEqual(self.sides745.area(), 9.79796)
        self.assertEqual(self.sides555.area(), 10.82532)
        self.assertEqual(self.sides883.area(), 11.78718)
        self.assertEqual(self.sides266.area(), 5.91608)
        self.assertEqual(self.sides747.area(), 13.41641)
        self.assertEqual(self.sides543.area(), 6.00000)
        self.assertEqual(self.sides686.area(), 18.00000)
        self.assertEqual(self.sides738.area(), 13.12500)

    def test_area_base_height(self):
        """
        Compare the triangle area computations to the actual values using base and height.
        Since we used Heron's Formula to calculate the triangle area in the class,
        now we use the traditional formula of b*h/2 as a sanity check.

        Note we have to limit the number of decimal places when testing for equality because
        the standard mathematical operations of multiplication and division don't return as
        precise of a value as math.sqrt(), unless we supply the appropriate number of
        significant digits.
        Triangle.area() uses math.sqrt() because it's required by Heron's Formula,
        and then rounds its return value, but we're testing this value from Triangle.area()
        against basic multiplication and division with a limited number of significant digits.
        In some, but not all, cases, this rounding can cause a test to erroneously fail.

        Example: in self.sides745.area(), the math.sqrt() usage results in area() returning
        a value of 9.79796. However, with a base of 7.00000 and height of 2.79942, calculating
        b*h/2 will return a value of 9.79797 in python. The wholly correct area is 9.797958971132712.
        This illustrates how rounding multiple times, even at 5 decimal places, can result in a
        slightly incorrect value.  In a production environment one would certainly want to
        avoid rounding altogether, but that feels unnecessary for this demo.
        """

        for base, height in zip(self.sides745.sides(), self.sides745.heights()):
            self.assertAlmostEqual(self.sides745.area(), base * height / 2, places=4)

        for base, height in zip(self.sides555.sides(), self.sides555.heights()):
            self.assertAlmostEqual(self.sides555.area(), base * height / 2, places=4)

        for base, height in zip(self.sides883.sides(), self.sides883.heights()):
            self.assertAlmostEqual(self.sides883.area(), base * height / 2, places=4)

        for base, height in zip(self.sides266.sides(), self.sides266.heights()):
            self.assertAlmostEqual(self.sides266.area(), base * height / 2, places=4)

        for base, height in zip(self.sides747.sides(), self.sides747.heights()):
            self.assertAlmostEqual(self.sides747.area(), base * height / 2, places=4)

        for base, height in zip(self.sides543.sides(), self.sides543.heights()):
            self.assertAlmostEqual(self.sides543.area(), base * height / 2, places=4)

        for base, height in zip(self.sides686.sides(), self.sides686.heights()):
            self.assertAlmostEqual(self.sides686.area(), base * height / 2, places=4)

        for base, height in zip(self.sides738.sides(), self.sides738.heights()):
            self.assertAlmostEqual(self.sides738.area(), base * height / 2, places=4)

    def test_categories(self):
        """
        Compare the test triangle categories to the actual values.
        Each triangle has four possible categories.
        Note some triangles will be a member of more than one category, such
        as an equilateral triangle is also isosceles.
        """
        # A 7-4-5 triangle is scalene only
        self.assertTrue(self.sides745.is_scalene())
        self.assertFalse(self.sides745.is_equilateral())
        self.assertFalse(self.sides745.is_isosceles())
        self.assertFalse(self.sides745.is_right_angle())

        # A 5-5-5 triangle is both equilateral and isosceles
        self.assertFalse(self.sides555.is_scalene())
        self.assertTrue(self.sides555.is_equilateral())
        self.assertTrue(self.sides555.is_isosceles())
        self.assertFalse(self.sides555.is_right_angle())

        # A 8-8-3 triangle is isosceles only (sides 1 and 2 are equal)
        self.assertFalse(self.sides883.is_scalene())
        self.assertFalse(self.sides883.is_equilateral())
        self.assertTrue(self.sides883.is_isosceles())
        self.assertFalse(self.sides883.is_right_angle())

        # A 2-6-6 triangle is isosceles only (sides 2 and 3 are equal)
        self.assertFalse(self.sides266.is_scalene())
        self.assertFalse(self.sides266.is_equilateral())
        self.assertTrue(self.sides266.is_isosceles())
        self.assertFalse(self.sides266.is_right_angle())

        # A 7-4-7 triangle is isosceles only (sides 1 and 3 are equal)
        self.assertFalse(self.sides747.is_scalene())
        self.assertFalse(self.sides747.is_equilateral())
        self.assertTrue(self.sides747.is_isosceles())
        self.assertFalse(self.sides747.is_right_angle())

        # A 5-4-3 triangle is both scalene and right-angle with side 1 as hypotenuse
        self.assertTrue(self.sides543.is_scalene())
        self.assertFalse(self.sides543.is_equilateral())
        self.assertFalse(self.sides543.is_isosceles())
        self.assertTrue(self.sides543.is_right_angle())

        # A 6-8.485-6 triangle is both isosceles and right-angle with side 2 as hypotenuse
        self.assertFalse(self.sides686.is_scalene())
        self.assertFalse(self.sides686.is_equilateral())
        self.assertTrue(self.sides686.is_isosceles())
        self.assertTrue(self.sides686.is_right_angle())

        # A 7.5-3.5-8.2765 triangle is both scalene and right-angle with side 3 as hypotenuse
        self.assertTrue(self.sides738.is_scalene())
        self.assertFalse(self.sides738.is_equilateral())
        self.assertFalse(self.sides738.is_isosceles())
        self.assertTrue(self.sides738.is_right_angle())
