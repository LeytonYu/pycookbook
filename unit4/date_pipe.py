import os
import fnmatch
import gzip
import bz2
import re


def gen_find(filepat, top):
    """
    查找目录树中与shell通配符模式匹配的所有文件名
    :param filepat:
    :param top:
    :return:
    """
    for path, dirlist, filelist in os.walk(top):
        # print(f'{path}-{dirlist}-{filelist}')
        for name in fnmatch.filter(filelist, filepat):
            yield os.path.join(path, name)


def gen_opener(filenames):
    """
    每次打开一个文件名序列，生成一个file对象。当继续进行下一次迭代时，该文件将立即关闭。
    :param filenames:
    :return:
    """
    for filename in filenames:
        if filename.endswith('.gz'):
            f = gzip.open(filename, 'rt')
        elif filename.endswith('.bz2'):
            f = bz2.open(filename, 'rt')
        else:
            f = open(filename, encoding='utf8')
        yield f
        f.close()


def gen_concatenate(iterators):
    """
    将一系列迭代器链接成单个序列
    :param iterators:
    :return:
    """
    for it in iterators:
        yield from it


def gen_grep(pattern, lines):
    """
    搜寻符合正则匹配的行
    :param pattern:
    :param lines:
    :return:
    """
    pat = re.compile(pattern)
    for line in lines:
        if pat.search(line):
            yield line


def test_pipe():
    path = r'D:\my_code\pycookbook\unit4'
    lognames = gen_find('errors*', path)
    files = gen_opener(lognames)
    lines = gen_concatenate(files)
    mysql_lines = gen_grep('pymysql\.err', lines)
    for lineno, line in enumerate(mysql_lines):
        print(f'lineno:{lineno}, value:{line}')


def test_open_file():
    path = r'D:\\my_code\\pycookbook\\unit4\\errors.log'
    f = open(path, encoding='utf-8')
    print(type(f))
    for lineno, line in enumerate(f):
        if lineno < 100:
            print(f'lineno:{lineno}, value:{line}')
        else:
            break


if __name__ == '__main__':
    # test_open_file()
    test_pipe()
