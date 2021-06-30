"""
内存映射的二进制文件

需要强调的一点是，内存映射一个文件并不会导致整个文件被读取到内存中。
也就是说，文件并没有被复制到内存缓存或数组中。
相反，操作系统仅仅为文件内容保留了一段虚拟内存。
当你访问文件的不同区域时，这些区域的内容才根据需要被读取并映射到内存区域中。
而那些从没被访问到的部分还是留在磁盘上。所有这些过程是透明的，在幕后完成！

如果多个Python解释器内存映射同一个文件，得到的 mmap 对象能够被用来在解释器直接交换数据。
也就是说，所有解释器都能同时读写数据，并且其中一个解释器所做的修改会自动呈现在其他解释器中。
很明显，这里需要考虑同步的问题。但是这种方法有时候可以用来在管道或套接字间传递数据。
"""
import mmap
import os


def memory_map(filename: str, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


def make_file(size: int, filename: str):
    with open(filename, 'wb') as f:
        f.seek(size - 1)
        f.write(b'\x00')


def try_memory_map():
    m = memory_map('初始化文件')
    print(len(m))
    print(m[:10])
    print(m[0])
    m[0: 11] = b'hello world'
    m.close()
    with open('初始化文件', 'rb') as f:
        print(f.read(11))

    with memory_map('初始化文件') as f:
        print(f.read(11))


def try_again():
    m = memory_map('初始化文件')
    v = memoryview(m).cast('I')
    print(v[0])


if __name__ == '__main__':
    # make_file(size=1000000, filename='初始化文件')
    # try_memory_map()
    try_again()
