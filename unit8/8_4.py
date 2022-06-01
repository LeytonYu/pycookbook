# 创建大量对象时节省内存的方法


class MyDate:

    __slots__ = ['year', 'month', 'day']
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


