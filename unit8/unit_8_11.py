"""简化数据结构的初始化"""
import json
import math


class Structure3:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError('Expected {} arguments'.format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))

        if kwargs:
            raise TypeError('Duplicate values for {}'.format(','.join(kwargs)))

    def __repr__(self):
        return f"{self.__class__.__name__} has vars: {json.dumps(self.__dict__)}"


class Stock(Structure3):
    _fields = ['name', 'shares', 'price']


class Point(Structure3):
    _fields = ['x', 'y']


class Circle(Structure3):
    _fields = ['radius']

    def area(self):
        return math.pi * self.radius ** 2


def first_do():
    s1 = Stock('ACME', 50, 91.1)
    s2 = Stock('ACME', 50, 91.1, date='2022-5-31')
    print(s1)
    print(s2)


if __name__ == '__main__':
    first_do()
