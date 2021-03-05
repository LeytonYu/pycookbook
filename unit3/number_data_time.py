import calendar
import random
from decimal import localcontext
from decimal import Decimal
from fractions import Fraction
import numpy as np
from datetime import datetime, timedelta


def test_decimal():
    a = Decimal('1.3')
    b = Decimal('1.7')
    print(a/b)
    with localcontext() as ctx:
        ctx.prec = 3
        print(a/b)
    with localcontext() as ctx:
        ctx.prec = 50
        print(a/b)

    nums = [1.28e+18, 1, -1.28e+18]
    print(sum(nums))
    print(max(nums))


def test_format():
    x = 1234.56789
    print(format(x, '.2f'))
    print(format(x, '>10.1f'))
    print(format(x, '<10.1f'))
    print(format(x, '^10.1f'))
    print(format(x, ','))
    print(format(x, '0,.1f'))
    print('{:.2f}'.format(x))


def test_pack():
    data = b'\x00\x124V\x00x\x90\xab\x00\xcd\xef\x01\x00#\x004'
    print(data)


def complex_calculate():
    """
    复数计算
    :return:
    """
    a = complex(2,5)
    b = 3-5j
    print(a+b)


def test_fraction():
    """
    分数计算
    :return:
    """
    a = Fraction(5, 4)
    b = Fraction(7, 16)
    c: Fraction = a + b
    print({
        'res': c,
        'type': type(c)
    })
    print(c)
    pass


def test_numpy():
    """
    numpy初体验
    :return:
    """
    ax = np.array([1, 2, 3, 4])
    ay = np.array([5, 6, 7, 8])
    print(ax * 2)
    print(ax + 10)
    print(ax + ay)
    print(f(ax))


def f(x):
    return 3 * x ** 2 - 2 * x + 7


def random_choice():
    values = [i for i in range(10)]
    # [print(random.choice(values)) for i in range(10)]
    print(random.sample(values, 3))     # 返回各不相同的随机数若干
    random.shuffle(values)      # 原地洗牌


weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday',
            'Friday', 'Saturday', 'Sunday']


def get_previous_byday(dayname, start_date=None):
    """
    获取指定日期上一周的某一天
    :param dayname:
    :param start_date:
    :return:
    """
    if start_date is None:
        start_date = datetime.today()
    day_num = start_date.weekday()
    day_num_target = weekdays.index(dayname)
    days_ago = (7 + day_num - day_num_target) % 7
    if days_ago == 0:
        days_ago = 7
    target_date = start_date - timedelta(days=days_ago)
    return target_date


def get_month_range(start_date=None) -> tuple:
    """
    返回当前月的起止日期
    :param start_date:
    :return: (stime, etime)
    """
    if start_date is None:
        start_date = datetime.today().replace(day=1)
    _, days_in_month = calendar.monthrange(start_date.year, start_date.month)
    end_date = start_date + timedelta(days_in_month)
    return start_date, end_date


if __name__ == '__main__':
    # random_choice()
    # print(get_previous_byday('Sunday'))
    print(get_month_range())