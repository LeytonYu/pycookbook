import csv
from collections import namedtuple
import dataclasses


@dataclasses.dataclass
class TestRow:
    name: str
    age: int
    sex: bool


def base_read():
    with open('stocks_list.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        print('csv头', headers)
        for row in f_csv:
            # row is a list
            print(row, type(row))


def namedtuple_read():
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        Row = namedtuple('Row', headers)
        for r in f_csv:
            row = Row(*r)
            print(row.Symbol)


def dict_read():
    with open('stocks.csv') as f:
        f_csv = csv.DictReader(f)
        for row in f_csv:
            print(row.get('Symbol'))


def test_row():
    a = TestRow(
        name='Leyton',
        age=23,
        sex=True,
    )
    print(a.name)


def write_csv_by_list():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [('AA', 39.48, '6/11/2007', '9:36am', -0.18, 181800),
            ('AIG', 71.38, '6/11/2007', '9:36am', -0.15, 195500),
            ('AXP', 62.58, '6/11/2007', '9:36am', -0.46, 935000),
            ]

    with open('stocks_list.csv', 'w', newline='') as f:  # newline=''目的：去除写入空行
        f_csv = csv.writer(f)
        f_csv.writerow(headers)
        f_csv.writerows(rows)


def write_csv_by_dict():
    headers = ['Symbol', 'Price', 'Date', 'Time', 'Change', 'Volume']
    rows = [{'Symbol': 'AA', 'Price': 39.48, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.18, 'Volume': 181800},
            {'Symbol': 'AIG', 'Price': 71.38, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.15, 'Volume': 195500},
            {'Symbol': 'AXP', 'Price': 62.58, 'Date': '6/11/2007',
             'Time': '9:36am', 'Change': -0.46, 'Volume': 935000},
            ]

    with open('stocks_dict.csv', 'w') as f:
        f_csv = csv.DictWriter(f, headers)
        f_csv.writeheader()
        f_csv.writerows(rows)


# csv数据格式只有字符串，入需额外处理，可以自行转换
def convert_csv_data():
    col_types = [str, float, str, str, float, int]
    with open('stocks.csv') as f:
        f_csv = csv.reader(f)
        headers = next(f_csv)
        for row in f_csv:
            # Apply conversions to the row items
            row = tuple(convert(value) for convert, value in zip(col_types, row))
            print(row)


# 转换特定值
def convert_cvs_data_dict():
    print('Reading as dicts with type conversion')
    field_types = [('Price', float),
                   ('Change', float),
                   ('Volume', int)]

    with open('stocks.csv') as f:
        for row in csv.DictReader(f):
            row.update((key, conversion(row[key]))
                       for key, conversion in field_types)
            print(row)


# 如果读取CSV数据的目的是做数据分析和统计的话，
# 可能需要看一看 Pandas 包。
# Pandas 包含了一个非常方便的函数叫 pandas.read_csv()，
# 它可以加载CSV数据到一个 DataFrame 对象中去。


if __name__ == '__main__':
    # base_read()
    # namedtuple_read()
    # dict_read()
    # test_row()
    # write_csv_by_list()
    # write_csv_by_dict()
    # convert_csv_data()
    convert_cvs_data_dict()
