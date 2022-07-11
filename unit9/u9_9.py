import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, cls):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


def profiled(func):
    ncalls = 0
    @wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal ncalls
        ncalls += 1
        return func(*args, **kwargs)
    wrapper.ncalls = lambda: ncalls
    return wrapper


@profiled
def add_v2(x, y):
    return x + y


@Profiled
def add(x, y):
    return x + y


class Spam:
    @profiled
    def bar(self, x):
        print(self, x)


def test_one():
    add(1, 2)
    add(2, 3)
    f = add.ncalls
    print(f)


def test_two():
    s = Spam()
    s.bar(1)
    s.bar(2)


if __name__ == '__main__':
    # test_one()
    test_two()