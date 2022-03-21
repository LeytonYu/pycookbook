import numpy as np

"""
ndarray具有以下重要属性：

ndarray.ndim：数组的轴数量
ndarray.shape：数组的形状。这是一个整数元组。比如对于n行m列的矩阵，其shape形状就是(n,m)。而shape元组的长度则恰恰是上面的ndim值，也就是轴数。
ndarray.size：数组中所有元素的个数。这恰好等于shape中元素的乘积。
ndarray.dtype：数组中元素的数据类型。除了标准的Python类型，Numpy还提供一些自有的类型。
ndarray.itemsize：元素的字节大小。比如float64类型的itemsize为8（=64/8），而complex32的itemsize为4（=32/8）。
ndarray.data：包含数组实际元素的缓冲区。通常我们不需要使用这个属性，因为我们将使用索引工具访问数组中的元素。
ndarray.flags: 数组对象的一些状态指示或标签
"""
a: np.ndarray = np.arange(15).reshape(3, 5)  # 创建一个数组并调整为3行5列
print(type(a))
print(a)
print(a.ndim)  # dimension 维度
print(a.dtype.name)
print(a.itemsize)
print(a.size)

print("==============")
b = np.array([6, 7, 8])     # 另一种方式创建数组
print(b)
