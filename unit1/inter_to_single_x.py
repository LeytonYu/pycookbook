from collections import deque, defaultdict
import queue
import heapq

dict_ex = [{'name': 'leyton', 'score': 100},
           {'name': 'ggj', 'score': 89},
           {'name': 'ld', 'score': 1978},
           {'name': 'dk', 'score': 97},
           {'name': 'dfg', 'score': 12}]


def inter_to_single():
    record = ('leyton', 10, 13.23, (12, 23, 2021))
    name, *_, (*_, year) = record
    print(name, year)


def search(lines, pattern, history=5):
    """
    匹配文本，返回匹配行和最后检查过的N行文本
    :param lines: 多行文本
    :param pattern: 匹配文本
    :param history: 保留最近查找的历史记录
    :return:
    """
    previous_line = deque(maxlen=history)
    for line in lines:
        if pattern in line:
            yield line, previous_line
        previous_line.append(line)


def do_search():
    text = ['她喜欢唱歌', '她喜欢跳舞', '她喜欢逛街', '我喜欢旅游', 'nice老哥发把狙', 'python太慢了', 'python开发方便']
    res = search(text, 'python', history=3)
    for zpp in res:
        que: deque
        line, que = zpp
        ss = [i for i in que]
        print(line, ss)


def find_numbers():
    """
    找到最大或最小的N个元素
    :return:
    """
    nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
    print(heapq.nlargest(3, nums))
    print(heapq.nsmallest(3, nums))

    dict_ex = [{'name': 'leyton', 'score': 100},
               {'name': 'ggj', 'score': 89},
               {'name': 'ld', 'score': 1978},
               {'name': 'dk', 'score': 97},
               {'name': 'dfg', 'score': 12}]
    high = heapq.nlargest(3, dict_ex, key=lambda x: x['score'])
    low = heapq.nsmallest(3, dict_ex, key=lambda x: x['score'])
    print(high, '\n', low)


class MyPriorityQueue:
    """
    用heapq实现我的优先级队列
    """

    def __init__(self):
        self._queue = []
        self._index = 0  # 记录插入顺序

    def push(self, item, priority):
        heapq.heappush(self._queue, (-priority, self._index, item))  # 原本堆是小的在上，这里用“-”把大的放上面
        self._index += 1

    def pop(self):
        return heapq.heappop(self._queue)[-1]


class Item:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return 'Item{!r}'.format(self.name)

    def __eq__(self, other):  # 比较两个对象是否相等的函数
        return self.name == other.name

    def __ne__(self, other):  # 比较两个对象是否不相等的函数
        return self.name != other.name

    def __gt__(self, other):  # 大于函数
        return self.name > other.name

    def __ge__(self, other):  # 大于等于
        return self.name >= other.name

    def __lt__(self, other):  # 小于
        return self.name < other.name

    def __le__(self, other):  # 小于等于
        return self.name <= other.name


def make_que():
    """
    验证我的优先级队列
    :return:
    """
    # example = queue.PriorityQueue()
    q = MyPriorityQueue()
    q.push(Item('foo'), 1)
    q.push(Item('bar'), 5)
    q.push(Item('spam'), 4)
    q.push(Item('grok'), 1)
    print(q._queue)
    print(q.pop())
    print(q.pop())


def dict_to_inter():
    """
    字典映射多值（可迭代对象）
    :return:
    """
    pairs = [('name', 'yld'), ('age', 22), ('sex', 'male')]
    d = defaultdict(list)  # 自动初始化第一个值，无需判断key是否存在
    for key, value in pairs:
        d[key].append(value)
    print(type(d), '\n', dict(d))


def dedupe(items, key=None):
    """
    可迭代对象去重器(内容可哈希)
    :param key: 哈希转化函数
    :param items: 可迭代对象
    :return:
    """
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield val
            seen.add(val)


def inter_to_order():
    """
    列表有序去重
    :return:
    """
    a = [1, 2, 5, 2, 1, 9, 1, 5, 10]
    print(list(dedupe(a)))


def dict_order():
    """
    字典公共键排序
    :return:
    """
    from operator import itemgetter
    dict_ex = [{'name': 'leyton', 'score': 100},
               {'name': 'ggj', 'score': 89},
               {'name': 'ld', 'score': 1978},
               {'name': 'dk', 'score': 97},
               {'name': 'dfg', 'score': 12}]
    rows_by_name = sorted(dict_ex, key=itemgetter('name'))
    rows_by_score = sorted(dict_ex, key=itemgetter('score'), reverse=True)
    rows_by_score_v2 = sorted(dict_ex, key=lambda x: (x['name'], -x['score']))
    print(rows_by_name, '\n', rows_by_score)
    print(rows_by_score_v2)


def is_int(val):
    try:
        x = int(val)
        return True
    except ValueError:
        return False


def test_filter():
    values = ['1', '2', '-3', '-', '4', 'N/a']
    ivals = list(filter(is_int, values))
    print(ivals)


def test_something():
    min_score = min(dict_ex, key=lambda x: x['score'])
    print(min_score)


def this_mian():
    test_something()
    # dict_order()


if __name__ == '__main__':
    this_mian()
