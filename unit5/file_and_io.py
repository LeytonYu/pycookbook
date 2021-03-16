import io
import os


def test_rt():
    # Read the entire file as a single string
    with open('test_sth', 'rt', encoding='utf8') as f:
        data = f.read()
        print(data)

    # Iterate over the lines of the file
    with open('test_sth', 'rt', encoding='utf8') as f:
        for line in f:
            print(line)


def test_wt():
    # Write chunks of text data
    with open('somefile.txt', 'wt') as f:
        f.write('哈哈哈哈哈哈哈哈哈哈')
        f.write('xxxxxxxxxxxxxxxxxx')
        ...

    # Redirected print statement
    with open('somefile.txt', 'w') as f:
        # 打印输出至文件中,文件必须是以文本模式打开,不能以二进制格式
        print('one', file=f)
        print('two', file=f)


def test_file_print(path):
    with open(path, 'rt', encoding='utf8', errors='ignore', newline='') as f:
        print(f.read())


def test_print():
    a = ['ggj', 12, 12.6, (12, 98)]
    print(*a, sep=':', end='^^\n')
    print(a)
    print(*a)


def test_bin_file():
    with open('somefile.bin', 'wb') as f:
        text = 'Hello World'
        f.write(text.encode('utf-8'))

    with open('somefile.bin', 'rb') as f:
        data = f.read(16)
        text = data.decode('utf-8')
        print(text)

    import array
    nums = array.array('i', [1, 2, 3, 4])
    with open('data.bin', 'wb') as f:
        f.write(nums)
    a = array.array('i', [0, 0, 0, 0])
    with open('data.bin', 'rb') as f:
        f.readinto(a)

    print(a)


def opt_exists_file():
    with open('somefile.txt', 'xt') as f:
        f.write('重写已存在的文件')


def opt_exists_file_v2(path):
    if not os.path.exists(path):
        with open(path, 'wt') as f:
            f.write('写入不存在的文件')
    else:
        print('文件已存在')


def str_io():
    s = io.StringIO()
    s.write('something fantastic!\n')
    ss = s.getvalue()
    print(ss, end='')

    a = io.StringIO('Hello\nWorld\n')
    b = a.read(5)
    print(b)
    print(a.read())

    m = io.BytesIO()
    m.write(b'binary data')
    print(m.getvalue())


if __name__ == '__main__':
    # test_wt()
    # test_file_print('somefile.txt')
    # test_print()
    # test_bin_file()
    # opt_exists_file()
    # opt_exists_file_v2()
    str_io()