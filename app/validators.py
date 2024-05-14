"""
Custom validators for different data types.
"""

from numbers import Integral


class IntegerField:
    """Validator for integers."""

    def __init__(self, min_value=None, max_value=None):
        self.min_value = min_value
        self.max_value = max_value

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, Integral):
            raise TypeError(f'{self.name} must be an integer!')
        if self.min_value is not None and value < self.min_value:
            raise ValueError(f'{self.name} must be greater than {self.min_value}')
        if self.max_value is not None and value > self.max_value:
            raise ValueError(f'{self.name} must be less than {self.max_value}')

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name, None)
