import datetime
from collections import deque
from typing import Iterable


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


def test_node():
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(5))
    for ch in root.depth_first():
        print(ch)


class CountDown:
    """
    返回指定的自然数
    """

    def __init__(self, start):
        self.start = start

    def __iter__(self):
        n = self.start
        while n > 0:
            yield n
            n -= 1

    # 反向迭代
    def __reversed__(self):
        n = 1
        while n <= self.start:
            yield n
            n += 1


def test_countdown():
    for num in CountDown(20):
        print(num)

    for num in reversed(CountDown(20)):
        print(num)


class LineHistory:
    """
    查询指定文本关联行
    """

    def __init__(self, lines, hislen=3):
        self.lines = lines
        self.history = deque(maxlen=hislen)

    def __iter__(self):
        for lineno, line in enumerate(self.lines):
            # 此处保存line带有\n换行符
            self.history.append((lineno, line))
            yield line

    def clear(self):
        self.history.clear()


def test_linehistory():
    with open('yld_1.txt') as f:
        lines = LineHistory(f)
        for line in lines:
            if 'yld' in line:
                for lineno, hline in lines.history:
                    print('{}:{}'.format(lineno, hline), end='')
                break
        print(lines.history)


def iter_count(n):
    while True:
        yield n
        n += 1


def teat_iter_count():
    import itertools
    c = iter_count(0)
    for x in itertools.islice(c, 10, 20):
        print(x)


def test_something():
    s = '2021-3-9 0:0:0'
    dt = datetime.datetime.strptime(s, '%Y-%m-%d %H:%M:%S')
    print(dt)


def test_4_8():
    from itertools import dropwhile, islice
    split = '=' * 30
    with open('yld_1.txt', encoding='utf8') as f:
        for line in dropwhile(lambda x: x.startswith('#'), f):
            # 跳过指定字符开头的行，后面再次遇到次字符，不再跳过
            print(line, end='')
    print('\n', split, '\n')
    items = ['a', 'b', 'c', 1, 2, 3, 4, 5]
    for i in islice(items, 3, 5):
        print(i)


def test_4_9():
    """
    迭代所有可能的组合或排列
    :return:
    """
    from itertools import permutations, combinations, combinations_with_replacement
    items = ['a', 'b', 'c']
    for p in permutations(items):
        # 全排列
        print('全排列')
        print(p)

    for p in permutations(items, 2):
        # 可选参数--全排列
        print('可选参数--全排列')
        print(p)

    for c in combinations(items, 3):
        # 全组合
        print('全组合-全参数')
        print(c)

    for c in combinations(items, 2):
        # 全组合
        print('全组合-2参数')
        print(c)

    for c in combinations_with_replacement(items, 3):
        # 可重复--全组合
        print('可重复--全组合')
        print(c)


def test_enumerate_zip():
    # zip会创建迭代器对象，最短匹配
    from itertools import zip_longest, chain
    data = [(1, 2, 7), (3, 4, 8), (5, 6, 9)]
    for i, (a, b, c) in enumerate(data):
        # print(x, y)
        print(a, b, c)
    print('=======================')
    xp = [1, 2, 3, 4, 5, 6, 7]
    yp = [7, 6, 5, 4, 3, 2, 1, 12, 31]
    dp = ['a', 'b', 'c', 1]
    qp = {1, 3, 4}
    iobj = zip(xp, yp)
    print('迭代器对象', iobj)
    for x, y in iobj:
        print(x, y)
    dic = dict(iobj)
    print(dic)  # 迭代完后，对象生命结束，返回为空
    for i in zip_longest(dp, xp, yp, fillvalue='ggj'):  # fillvalue 参数可填充None值
        print(i)
    print('===================')
    # chain可以连接不同类型的迭代对象, 生成迭代器
    for i in chain(qp, dp):
        print(i)


def flatten(items, ignore_types=(str, bytes)):
    for x in items:
        if isinstance(x, Iterable) and not isinstance(x, ignore_types):
            yield from flatten(x)
        else:
            yield x


def test_loop_iter():
    items = [1, 2, [3, [4, 5], 6, 7], 8, 'adfa']
    for x in flatten(items):
        print(x)


def test_heapq():
    """
    顺序迭代合并后的排序迭代对象
    # heapq。merge类似归并排序的合并
    :return:
    """
    import heapq
    a = [1, 3, 90, 20, 12, 0]
    b = [123, 49856, 53, 4, 7]
    a.sort()
    b.sort()
    print(a, b)
    for c in heapq.merge(a, b):
        print(c)


if __name__ == '__main__':
    test_heapq()
    # test_something()
