import weakref


class Singleton(type):
    # 用元类实现单例
    def __init__(self, *args, **kwargs):
        self._instance = None
        super(Singleton, self).__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super(Singleton, self).__call__(*args, **kwargs)
        return self._instance


class SingleSus:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            cls._instance = super().__new__(cls)
        return cls._instance


class Cached(type):
    def __init__(self, *args, **kwargs):
        super(Cached, self).__init__(*args, **kwargs)
        self._pool = weakref.WeakValueDictionary()

    def __call__(self, *args, **kwargs):
        if args not in self._pool:
            obj = super().__call__(*args, **kwargs)
            self._pool[args] = obj
            return obj
        return self._pool[args]


class Spam(metaclass=Singleton):
    def __init__(self):
        print('oh yeah!')


class SpamNew(SingleSus):
    def __init__(self, dog, cat):
        if not hasattr(self, '_no_init'):
            print('on yeah! oh right!')
            self.dog = dog
            self.cat = cat
            self._no_init = True


class Player(metaclass=Cached):
    def __init__(self, name, sex):
        self.name = name
        self.sex = sex
        print(name, sex)


def test_one():
    a = Spam()
    b = Spam()
    c = Spam()


def test_two():
    tp = []
    for i in range(3):
        tp.append(SpamNew(dog='Doudou', cat='Miaomiao'))
    print(tp[0], tp[1], tp[-1].cat)


def test_three():
    tp = []
    for i in range(3):
        tp.append(Player("Leyton", 'male'))
        tp.append(Player('Guguji', 'female'))
    print(tp)


if __name__ == '__main__':
    # test_one()
    # test_two()
    test_three()