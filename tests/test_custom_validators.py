"""
Tests for custom validators classes.
Command line: python -m unittest tests.test_custom_validators -v
"""

from unittest import TestCase
from app.validators import IntegerField


class Point:
    x = IntegerField(min_value=1, max_value=100)

    def __init__(self, x):
        self.x = x


class TestIntegerField(TestCase):
    """Tests for IntegerField objects."""

    def setUp(self):
        self.prop_name = 'x'
        self.prop_value = 8
        self.prop_min = 1
        self.prop_max = 100

    def test_set_name(self):
        """Test set property name."""

        p = Point(self.prop_value)

        self.assertIn(self.prop_name, p.__dict__)

    def test_set_value_success(self):
        """Test set property value successfully."""

        p = Point(self.prop_value)

        self.assertEqual(p.x, self.prop_value)

    def test_get_property_value(self):
        """Test getting property value."""

        p = Point(self.prop_value)
        value = p.x

        self.assertEqual(value, self.prop_value)

    def test_min_max_values_success(self):
        """Test set minimum and maximum values successfully."""

        self.assertEqual(Point.x.min_value, self.prop_min)
        self.assertEqual(Point.x.max_value, self.prop_max)

    def test_non_integer_value_error(self):
        """Test set non integer value raises TypeError."""

        with self.assertRaises(TypeError):
            Point(3.5)

    def test_wrong_min_value_error(self):
        """Test set value less than minimum raises ValueError."""

        with self.assertRaises(ValueError):
            Point(-1)

    def test_wrong_max_value_error(self):
        """Test set value greater than maximum raises ValueError."""

        with self.assertRaises(ValueError):
            Point(200)
