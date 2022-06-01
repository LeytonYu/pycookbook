"""使用延迟计算属性"""
import math
from time import time


class Lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


def lazyproperty(func):
    """
    不可修改的懒加载，因为property是只读的
    由于使用getattr，性能弱于可修改的类装饰器
    :param func:
    :return:
    """
    name = '_lazy_' + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


def test_decorate(func):
    @property
    def inner(self):
        print('我就看看')
        return func(self)

    return inner


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @Lazyproperty
    def area(self):
        print('Computing area')
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print('Computing perimeter')
        return 2 * math.pi * self.radius

    @property
    def debug(self):
        return self.radius * 100


def death_wink(ins):
    print('death wink')
    return math.pi * ins.radius ** 2


def first_do():
    circle = Circle(5)
    print('xiha')
    stime = time()
    for i in range(1000000):
        a = circle.area
    ttime = time()
    print('类装饰器懒加载：', ttime - stime)

    stime = time()
    for i in range(1000000):
        b = circle.perimeter
    ttime = time()
    print('函数装饰器不可修改懒加载：', ttime - stime)


if __name__ == '__main__':
    first_do()
