import os
import sys


def write_file():
    with open('jalape\xf1o.txt', 'w') as f:
        f.write('Spicy!')


def read_file():
    dirs = os.listdir('.')
    print(dirs)
    dirs_v2 = os.listdir(b'.')
    print(dirs_v2)
    with open(b'jalape\xc3\xb1o.txt') as f:
        print(f.read())


if __name__ == '__main__':
    # write_file()
    read_file()