import gzip
import bz2
import os

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


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


def talk_readinto():
    record_size = 32    # Size of each record (adjust value)

    buf = bytearray(record_size)
    with open('somefile.txt', 'rb') as f:
        while True:
            n = f.readinto(buf)
            if n < record_size:
                break
    print(buf)
    buf = buf.decode('utf8')
    print(buf)


def memoryview_opt():
    buf = bytearray('Hello World', encoding='utf8')
    m1 = memoryview(buf)
    m2 = m1[-5:]
    print(m2)
    m2[:] = b'WORLD'
    print(buf)


def test_sth():
    print('ggj')


if __name__ == '__main__':
    # write_gzip()
    # test_sth()
    # talk_readinto()
    memoryview_opt()