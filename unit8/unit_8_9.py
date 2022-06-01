"""创建新的类或实例属性"""


class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError('Expected an int')
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


class Point:
    x = Integer('x')
    y = Integer('y')

    def __init__(self, x, y):
        self.x = x
        self.y = y


def first_do():
    p = Point(2, 3)
    print(p.__dir__())
    print(p.x, p.y)


class Typed:
    def __init__(self, name, expect_type):
        self.name = name
        self.expect_type = expect_type

    def __get__(self, instance, owner):
        if instance:
            return instance.__dict__[self.name]
        else:
            return self

    def __set__(self, instance, value):
        if not isinstance(value, self.expect_type):
            raise TypeError(f"Expected {self.expect_type} for {self.name}")
        instance.__dict__[self.name] = value


def typeassert(**kwargs):
    def decorate(cls):
        for name, expect_type in kwargs.items():
            setattr(cls, name, Typed(name, expect_type))
        return cls

    return decorate


@typeassert(name=str, age=int, height=float, weight=float)
class People:
    def __init__(self, name, age, height, weight):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight

    def __call__(self, *args, **kwargs):
        return self.name, self.age, self.height, self.weight

    def __str__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight} from __str__"

    def __repr__(self):
        return f"{self.name}, {self.age}, {self.height}, {self.weight} from __repr__"


def second_do():
    mark = People(name='mark', age=24, height=174.5, weight=59.5)
    print(mark())
    print(mark)


if __name__ == '__main__':
    # first_do()
    second_do()
