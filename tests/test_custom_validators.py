"""
Tests for custom validators classes.
Command line: python -m unittest tests.test_custom_validators -v
"""

from unittest import TestCase
from app.validators import IntegerField, CharField


class TestIntegerField(TestCase):
    """Tests for IntegerField objects."""

    class Point:
        x = IntegerField(min_value=1, max_value=100)

        def __init__(self, x):
            self.x = x

    def setUp(self):
        self.prop_name = 'x'
        self.prop_value = 8
        self.prop_min = 1
        self.prop_max = 100

    def test_set_name(self):
        """Test set property name."""

        p = self.Point(self.prop_value)

        self.assertIn(self.prop_name, p.__dict__)

    def test_set_value_success(self):
        """Test set property value successfully."""

        p = self.Point(self.prop_value)

        self.assertEqual(p.x, self.prop_value)

    def test_get_property_value(self):
        """Test getting property value."""

        p = self.Point(self.prop_value)
        value = p.x

        self.assertEqual(value, self.prop_value)

    def test_min_max_values_success(self):
        """Test set minimum and maximum values successfully."""

        self.assertEqual(self.Point.x.min_value, self.prop_min)
        self.assertEqual(self.Point.x.max_value, self.prop_max)

    def test_non_integer_value_error(self):
        """Test set non integer value raises TypeError."""

        with self.assertRaises(TypeError):
            self.Point(3.5)

    def test_wrong_min_value_error(self):
        """Test set value less than minimum raises ValueError."""

        with self.assertRaises(ValueError):
            self.Point(-1)

    def test_wrong_max_value_error(self):
        """Test set value greater than maximum raises ValueError."""

        with self.assertRaises(ValueError):
            self.Point(200)


class TestCharField(TestCase):
    """Tests for CharField objects."""

    class Person:
        name = CharField(min_value=1, max_value=10)

        def __init__(self, name):
            self.name = name

    def setUp(self):
        self.prop_name = 'name'
        self.prop_value = 'Alex'
        self.prop_min = 1
        self.prop_max = 10

    def test_set_name(self):
        """Test set property name."""

        p = self.Person(self.prop_value)

        self.assertIn(self.prop_name, p.__dict__)

    def test_set_value_success(self):
        """Test set property value successfully."""

        p = self.Person(self.prop_value)

        self.assertEqual(p.name, self.prop_value)

    def test_get_property_value(self):
        """Test getting property value."""

        p = self.Person(self.prop_value)
        value = p.name

        self.assertEqual(value, self.prop_value)

    def test_min_max_values_success(self):
        """Test set minimum and maximum values successfully."""

        self.assertEqual(self.Person.name.min_value, self.prop_min)
        self.assertEqual(self.Person.name.max_value, self.prop_max)

    def test_non_string_value_error(self):
        """Test set non string value raises TypeError."""

        with self.assertRaises(TypeError):
            self.Person(10)

    def test_empty_string_error(self):
        """Test set empty string raises ValueError."""

        with self.assertRaises(ValueError):
            self.Person('')

    def test_wrong_max_value_error(self):
        """Test set value greater than maximum length raises ValueError."""

        with self.assertRaises(ValueError):
            self.Person('Eadfgvsdvjkl')
