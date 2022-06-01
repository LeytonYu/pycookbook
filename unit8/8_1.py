# 改变对象的字符串显示


class Pair:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Pair({0.x}, {0.y})".format(self)

    def __str__(self):
        return "({0.x}, {0.y})".format(self)


def main():
    p = Pair(3, 4)
    print(p)
    print("{!r}".format(p))


if __name__ == '__main__':
    main()