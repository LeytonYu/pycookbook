class mclassmethod(object):

    def __init__(self, func):
        self._func = func

    def __get__(self, obj, klass=None):
        if klass is None:
            klass = type(obj)

        def wapper(*args):
            return self._func(klass, *args)

        return wapper

    @property
    def __func__(self):
        return self._func


class Apple(object):
    lowest_price = 10

    def __init__(self, price=15):
        self._price = price

    @mclassmethod
    def calc_lowest_total_price(cls, weight):
        return cls.lowest_price * weight


def test_one():
    print(Apple.calc_lowest_total_price(10))


if __name__ == '__main__':
    test_one()