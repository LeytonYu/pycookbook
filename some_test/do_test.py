class myproperty:

    def __init__(self, f_get, f_set=None, f_del=None):
        self._f_get = f_get
        self._f_set = f_set
        self._f_del = f_del

    def __get__(self, instance, owner):
        return self._f_get(instance)

    def __set__(self, instance, value):
        if not hasattr(self._f_set, '__call__'):
            raise AttributeError('Readonly attribute')
        self._f_set(instance, value)

    def __delete__(self, obj):
        if not hasattr(self._f_del, '__call__'):
            raise AttributeError('Can not delete this attribute')
        self._f_del(obj)

    def setter(self, function):
        self._f_set = function
        return self

    def deleter(self, function):
        self._f_del = function
        return self


class MyFurther:

    def __init__(self, v):
        self._value = v

    @myproperty
    def value(self):
        return self._value

    @value.setter
    def value(self, v):
        self._value = v

    @value.deleter
    def value(self):
        del self._value
        print('delete function')


def test_one():
    obj = MyFurther(10)
    print(obj.value)
    obj.value = 11
    print(obj.value)
    del obj.value


if __name__ == '__main__':
    test_one()
