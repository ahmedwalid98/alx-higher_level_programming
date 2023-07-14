#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
from models.base import Base
"""test for rectangle class
"""
class TestRectangle(unittest.TestCase):
    """Unittests for testing instantiation of the Rectangle class."""

    def test_id_for_first_rectangle(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 1)

    def test_id_for_second_rectangle(self):
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 2)

    def test_id_with_rectangle_takes_id_as_arg(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(r3.id, 12)

    def test_width_with_wrong_type(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
