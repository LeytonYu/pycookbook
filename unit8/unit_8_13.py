"""实现数据模型的类型约束"""
import json


class Descriptor:
    def __init__(self, name=None, **opts):
        self.name = name
        for key, value in opts.items():
            setattr(self, key, value)

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class Typed(Descriptor):
    expected_type = type(None)

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected {} type, error value {}".format(self.expected_type, value))
        super(Typed, self).__set__(instance, value)


class Unsigned(Typed):

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError('Expected >= 0')
        super(Unsigned, self).__set__(instance, value)


class MaxSized(Descriptor):
    expected_type = str

    def __init__(self, name=None, **opt):
        if 'size' not in opt:
            raise TypeError('missing size option')
        super(MaxSized, self).__init__(name, **opt)

    def __set__(self, instance, value):
        if len(value) > self.size:
            raise ValueError(f'size must be < {self.size}')
        super(MaxSized, self).__set__(instance, value)


class Integer(Typed):
    expected_type = int


class UnsignedInteger(Integer, Unsigned):
    pass


class Float(Typed):
    expected_type = float


class UnsignedFloat(Float, Unsigned):
    pass


class String(Typed):
    expected_type = str


class SizedString(String, MaxSized):
    pass


class Stock:
    # Specify constraints
    name = SizedString('name', size=58)
    shares = UnsignedInteger('shares')
    price = UnsignedFloat('price')

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}: {json.dumps(self.__dict__)}"


def first_do():
    s = Stock(name='NVIDIA', shares=12, price=23.5)
    print(s)


# Class decorator to apply constraints
def check_attributes(**kwargs):
    def decorate(cls):
        for key, value in kwargs.items():
            if isinstance(value, Descriptor):
                value.name = key
                setattr(cls, key, value)
            else:
                setattr(cls, key, value(key))
        return cls

    return decorate


@check_attributes(name=MaxSized(size=50),
                  author=MaxSized(size=50),
                  publisher=MaxSized(size=50),
                  price=UnsignedFloat)
class Book:
    def __init__(self, name, author, publisher, price, year):
        self.name = name
        self.author = author
        self.publish = publisher
        self.price = price
        self.year = year

    def __repr__(self):
        return f"{self.__class__.__name__}:{json.dumps(self.__dict__)}"


def second_do():
    book = Book(name='python cookbook',
                author='Leyton Yu',
                publisher='ZhuJi',
                price=49.99,
                year=2013.1)
    print(book)


# A metaclass that applies checking
class checkedmeta(type):
    def __new__(cls, clsname, bases, methods):
        # Attach attribute names to the descriptors
        for key, value in methods.items():
            if isinstance(value, Descriptor):
                value.name = key
        return type.__new__(cls, clsname, bases, methods)


# Example
class Stock2(metaclass=checkedmeta):
    name = SizedString(size=8)
    shares = UnsignedInteger()
    price = UnsignedFloat()

    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

    def __repr__(self):
        return f"{self.__class__.__name__}:{json.dumps(self.__dict__)}"


def third_do():
    s = Stock2(name='NVIDIA', shares=123, price=23.5)
    print(s)


if __name__ == '__main__':
    # first_do()
    # second_do()
    third_do()
