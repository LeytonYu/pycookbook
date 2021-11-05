import datetime
import fnmatch
import glob
import os
import time


def usual_os_option():
    path = r'D:\my_code\pycookbook\unit5\somefile.txt'
    print(os.path.basename(path))   # 获取文件名
    print(os.path.dirname(path))    # 获取文件夹路径
    print(os.path.join('D:\my_code', 'pycookbook', 'some_util.zip'))

    path2 = '~\data\data.csv'
    print(os.path.expanduser(path2))
    print(os.path.splitext(path))


def check_file_exists(path: str):
    print(os.path.exists(path))
    print(os.path.isfile(path))
    print(os.path.isdir(path))
    print(os.path.islink(path))
    print(os.path.realpath(path))   # 绝对路径

    print(os.path.getsize(path))
    print(os.path.getmtime(path), time.ctime(os.path.getmtime(path)))   # 创建时间


def list_file(path: str):
    names = os.listdir(path)
    file_names = [name for name in os.listdir(path) if os.path.isfile(os.path.join(path, name))]
    dir_names = [name for name in os.listdir(path) if os.path.isdir(os.path.join(path, name))]
    endswith_names = [name for name in os.listdir(path) if name.endswith('.7z')]
    glob_name = glob.glob(f'{path}/*.7z')
    fnmatch_name = [name for name in os.listdir(path) if fnmatch.fnmatch(name, '*.7z')]
    print(f'所有文件和文件夹：{names}')
    print(f'所有文件：{file_names}')
    print(f'所有文件夹：{dir_names}')
    print(f'所有.7z结尾的文件：{endswith_names}')
    print(f'glob_name(全路径): {glob_name}')
    print(f'fnmatch_name: {fnmatch_name}')

    file_metadata = [(name, os.stat(name)) for name in glob_name]
    for name, meta in file_metadata:
        print('嘿嘿嘿', name, meta.st_size, meta.st_mtime)
        print('转义', name, f'{meta.st_size/ 1024 /1024} mb', datetime.datetime.fromtimestamp(meta.st_mtime))


if __name__ == '__main__':
    # usual_os_option()
    a = "D:\图片\Saved Pictures\不敢吱声.jpg"
    # check_file_exists(a)
    list_file('D:\my_code')