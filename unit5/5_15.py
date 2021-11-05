"""
打印不合法文件名
"""
import os


def bad_filename(filename):
    # 怎么补救看自己了
    return repr(filename)[1:-1]


def print_bad_filename():
    files = os.listdir('.')
    for filename in files:
        try:
            print(filename)
        except UnicodeEncodeError:
            print('hey, encode wrong!')
            print(bad_filename(filename))


def create_funny_file():
    with open('b\udce4d.txt', 'wb') as f:
        f.write(b'this is wrong')


if __name__ == '__main__':
    # create_funny_file()
    print_bad_filename()