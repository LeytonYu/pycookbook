import gzip
import bz2


text = '这是默认文本。\n' \
       'This is default text。\n' \
       'これがデフォルトテキストです。\n'


def write_gzip():
    with gzip.open('somefile.gz', 'wt') as f:
        f.write(text)


def open_gzip():
    with gzip.open('somefile.gz', 'rt') as f:
        print(f.read())


def eat_open():
    f = open('somefile.gz', 'rb')
    with gzip.open(f, 'rt') as g:
        tt = g.read()
        print(tt)


if __name__ == '__main__':
    # write_gzip()
    # open_gzip()
    eat_open()