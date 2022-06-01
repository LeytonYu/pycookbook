# 自定义字符串的格式化


_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class MyDate:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, format_spec):
        if format_spec == '':
            format_spec = 'ymd'
        fmt = _formats[format_spec]
        return fmt.format(d=self)


def main():
    mydate = MyDate(year=2022, month=3, day=29)
    print("Today is {}".format(mydate))
    print("Today is {:dmy}".format(mydate))


if __name__ == '__main__':
    main()
