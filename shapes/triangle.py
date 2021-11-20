#!/usr/bin/env python

"""
Author: Matthew Kane
File: triangle.py
Purpose: Defines a Triangle object, inherited from the abstract class Shape
Credit: Based on Nick Russo's "Learning Python by Example" online course on oreilly.com
"""

from math import sqrt
from shapes.shape import Shape

class Triangle(Shape):
    """
    Represents a Triangle shape, and contains values for each of
    the three sides and the number of decimal places to use when
    computing values such as area.
    Overrides the area() and perimeter() methods from the parent class Shape
    """

    # Since we're dealing with square roots, allow for extra decimal places
    decimal_places = 5

    def __init__(self, side1, side2, side3):
        """
        Create the triangle by storing the base and height
        """
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def __str__(self):
        """
        Allows the triangle to be treated like a string,
        returning the sides
        """
        return f"Triangle {self.side1}-{self.side2}-{self.side3}"

    def _semi_perimeter(self):
        """
        Helper function that returns the semi-perimeter of the triangle
        by computing half the triangle's perimeter.
        """
        return self.perimeter() / 2

    def to_dict(self):
        """
        Convert this triangle into a dictionary with:
        name, perimeter, area, and heights.
        """
        return {
            "type": str(self),
            "perimeter": self.perimeter(),
            "area": self.area(),
            "heights": self.heights(),
        }

    def sides(self):
        """
        Return a tuple of the three sides for this triangle
        """
        return (round(self.side1, self.decimal_places),
                round(self.side2, self.decimal_places),
                round(self.side3, self.decimal_places))

    def area(self):
        """
        Compute the area using Heron's Formula:
        area = sqrt( s * (s-a) * (s-b) * (s-c) )
        where s is the semi-perimeter and the sides are a, b, and c

        NOTE: area can also be calculated using only the three sides and
        without using the semi-perimeter, but the _semi-perimeter() method is used
        here to practice adding class method that, I THINK, will be treated as private.
        See the heights() method for the alternative usage of Heron's Formula

        Returns the area rounded to the object's internal decimal_places property
        """
        s = self._semi_perimeter()
        a1 = s - self.side1
        a2 = s - self.side2
        a3 = s - self.side3
        area = sqrt(s * a1 * a2 * a3)
        return round(area, self.decimal_places)

    def heights(self):
        """
        Calculate the heights of the triangle for all three sides.
        Uses Heron's Formula.

        height1 = 0.5 * sqrt( (a+b+c) * (-a+b+c) * (a-b+c) * (a+b-c) ) / a
        height2 = 0.5 * sqrt( (a+b+c) * (-a+b+c) * (a-b+c) * (a+b-c) ) / b
        height3 = 0.5 * sqrt( (a+b+c) * (-a+b+c) * (a-b+c) * (a+b-c) ) / c
        for sides a, b, and c

        Returns a tuple of heights, where each height corresponds to using
        each side as the base.
        For example...
        the first tuple element is the height when referencing self.side1 as the base,
        the second tuple element is the height when referencing self.side2 as the base,
        the third tuple element is the height when referencing self.side3 as the base.
        """
        part1 = self.side1 + self.side2 + self.side3
        part2 = -self.side1 + self.side2 + self.side3
        part3 = self.side1 - self.side2 + self.side3
        part4 = self.side1 + self.side2 - self.side3
        part5 = sqrt(part1 * part2 * part3 * part4)
        height1 = round(0.5 * part5 / self.side1, self.decimal_places)
        height2 = round(0.5 * part5 / self.side2, self.decimal_places)
        height3 = round(0.5 * part5 / self.side3, self.decimal_places)
        return height1, height2, height3

    def perimeter(self):
        """
        Compute the perimeter by adding all three sides
        """
        return round(self.side1 + self.side2 + self.side3, self.decimal_places)

    def is_special(self):
        return self.is_equilateral() or \
               self.is_isosceles() or \
               self.is_right_angle() or \
               self.is_scalene()

    def is_equilateral(self):
        """
        Compute whether or not the object is an equilateral triangle.
        Returns True only if all three sides are equal.
        Returns False otherwise.
        """
        return self.side1 == self.side2 == self.side3

    def is_isosceles(self):
        """
        Compute whether or not the object is an isosceles triangle.
        Returns True only if at least two of the sides are equal.
        Returns False otherwise.
        Superfluous parentheses are added for readability only.
        """
        return (self.side1 == self.side2) or \
               (self.side1 == self.side3) or \
               (self.side2 == self.side3)

    def is_right_angle(self):
        """
        A right triangle must satisfy the pythagorean theorem
        Rather than testing for the longest side, we can use boolean logic,
        since one of the following three cases must be True for us to have
        a right triangle, where each case corresponds to a different side
        being the hypotenuse.
        Superfluous parentheses are added for readability only.
        """
        s1_squared = round(self.side1 ** 2, 4)
        s2_squared = round(self.side2 ** 2, 4)
        s3_squared = round(self.side3 ** 2, 4)
        return (s1_squared + s2_squared == s3_squared) or \
               (s1_squared + s3_squared == s2_squared) or \
               (s2_squared + s3_squared == s1_squared)

    def is_scalene(self):
        """
        Compute whether or not the object is a scalene triangle.
        Returns True only if there does not exist a pair of equal sides in the triangle.
        Three comparisons need to be made. If all three comparisons fail to find
        equal sides then returns True. If any pair of sides is equal then returns False
        Superfluous parentheses are added for readability only.
        """
        return (self.side1 != self.side2) and \
               (self.side2 != self.side3) and \
               (self.side1 != self.side3)
