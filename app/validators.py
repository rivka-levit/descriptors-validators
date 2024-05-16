"""
Custom validators for different data types.
"""

from numbers import Integral


class BaseValidator:
    """Base class for all validators."""

    def __init__(self, type_, min_value=None, max_value=None,
                 msg_min=None, msg_max=None):
        self.name = None
        self.min_value = min_value
        self.max_value = max_value
        self._type = type_

        if msg_min is None:
            self.msg_min = f'{self.name} must be at least {self.min_value}!'
        else:
            self.msg_min = msg_min

        if msg_max is None:
            self.msg_max = (f'{self.name} can not be greater '
                            f'than {self.max_value}')
        else:
            self.msg_max = msg_max

    def __set_name__(self, owner, name):
        self.name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._type):
            raise TypeError(f'{self.name} must be of type {self._type}!')
        self.validate_size(value)

        instance.__dict__[self.name] = value

    def __get__(self, instance, owner):
        if instance is None:
            return self

        return instance.__dict__.get(self.name, None)

    def validate_size(self, value):
        if self.min_value is not None and value < self.min_value:
            raise ValueError(self.msg_min)
        if self.max_value is not None and value > self.max_value:
            raise ValueError(self.msg_max)


class IntegerField(BaseValidator):
    """Validator for integers."""

    def __init__(self, min_value=None, max_value=None):
        super().__init__(type_=Integral,
                         min_value=min_value,
                         max_value=max_value)


class CharField(BaseValidator):
    """Validator for strings."""

    def __init__(self, min_value=None, max_value=None):
        if min_value is not None and min_value < 1:
            raise ValueError('Minimum value of string length must be at '
                             'least 1 character.')
        super().__init__(
            type_=str,
            min_value=min_value,
            max_value=max_value
        )

        self.msg_min = f'The length of {self.name} must be at least {min_value}'
        self.msg_max = (f'The length of {self.name} can not be greater '
                        f'than {max_value}')

    def validate_size(self, value):
        if self.min_value is not None and len(value) < self.min_value:
            raise ValueError(self.msg_min)
        if self.max_value is not None and len(value) > self.max_value:
            raise ValueError(self.msg_max)
