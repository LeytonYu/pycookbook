import os


def usual_os_option():
    path = r'D:\my_code\pycookbook\unit5\somefile.txt'
    print(os.path.basename(path))   # 获取文件名
    print(os.path.dirname(path))    # 获取文件夹路径
    print(os.path.join('D:\my_code', 'pycookbook', 'some_util.zip'))

    path2 = '~\data\data.csv'
    print(os.path.expanduser(path2))
    print(os.path.splitext(path))


if __name__ == '__main__':
    usual_os_option()