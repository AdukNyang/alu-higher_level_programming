#!/usr/bin/python3
"""Module that defines a Square class with comparison operators."""


class Square:
    """A class that defines a square with comparison capabilities."""

    def __init__(self, size=0):
        """Initialize a Square.

        Args:
            size: The size of the square.
        """
        self.size = size

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square.

        Args:
            value: The size value to set.

        Raises:
            TypeError: If value is not a number.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, (int, float)):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on area."""
        return self.area() == other.area()

    def __ne__(self, other):
        """Check if two squares are not equal based on area."""
        return self.area() != other.area()

    def __lt__(self, other):
        """Check if this square is less than another based on area."""
        return self.area() < other.area()

    def __le__(self, other):
        """Check if this square is less than or equal to another based on
        area."""
        return self.area() <= other.area()

    def __gt__(self, other):
        """Check if this square is greater than another based on area."""
        return self.area() > other.area()

    def __ge__(self, other):
        """Check if this square is greater than or equal to another based on
        area."""
        return self.area() >= other.area()
