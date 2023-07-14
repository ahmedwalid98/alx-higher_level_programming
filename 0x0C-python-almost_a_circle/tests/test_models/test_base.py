#!/usr/bin/python3
import unittest

class TestBase(unittest.TestCase):
    from models.base import Base

    def test_no_args(self):
        b1 = Base()
        self.assertEqual(b1.id, 1)

    def test_with_args(self):
        b1 = Base(12)
        self.assertEqual(b1.id, 12)
