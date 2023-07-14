#!/usr/bin/python3
import unittest
from models.base import Base

class TestBase(unittest.TestCase):

    def test_no_args(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_second_no_args(self):
        b2 = Base()
        self.assertEqual(b2.id, 2)

    def test_with_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
