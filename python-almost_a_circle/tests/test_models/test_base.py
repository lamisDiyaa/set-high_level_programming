#!/usr/bin/python3
"""Unittest for models/base.py"""
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """TestCase for Base class."""

    def test_auto_id(self):
        """Test automatic ID assignment."""
        b1 = Base()
        b2 = Base()
        self.assertEqual(b2.id, b1.id + 1)

    def test_custom_id(self):
        """Test custom ID assignment."""
        b = Base(89)
        self.assertEqual(b.id, 89)

    def test_to_json_string_none(self):
        """Test to_json_string with None."""
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json_string_empty(self):
        """Test to_json_string with empty list."""
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json_string_valid(self):
        """Test to_json_string with valid list of dicts."""
        d = [{'id': 12}]
        res = Base.to_json_string(d)
        self.assertEqual(res, '[{"id": 12}]')
        self.assertIsInstance(res, str)

    def test_from_json_string_none(self):
        """Test from_json_string with None."""
        self.assertEqual(Base.from_json_string(None), [])

    def test_from_json_string_empty(self):
        """Test from_json_string with empty string."""
        self.assertEqual(Base.from_json_string("[]"), [])

    def test_from_json_string_valid(self):
        """Test from_json_string with valid JSON string."""
        s = '[{"id": 89}]'
        res = Base.from_json_string(s)
        self.assertEqual(res, [{'id': 89}])
        self.assertIsInstance(res, list)


if __name__ == '__main__':
    unittest.main()
