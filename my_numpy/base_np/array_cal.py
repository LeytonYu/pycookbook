import numpy as np

"""
对数组做基本的算术运算，将会对整个数组的所有元组进行逐一运算，并将运算结果保存在一个新的数组内，而不会破坏原始的数组。
另外，不同于数学中的矩阵乘法，使用星号做乘号时，numpy对数组的每个元素，一一对应的做乘法。如果要进行矩阵的乘法怎么办？使用@或者dot函数！
对于+=和 *= 这一类操作符，会修改原始的数组，而不是新建一个
当对两个不同类型的数组进行运算操作时，将根据精度，选择最复杂的作为结果的类型
"""


def main():
    a = np.array([20, 30, 40, 50])
    b = np.arange(4)
    c = a - b
    print(c)
    print(b ** 2)
    print(10 * np.sin(a))
    print(a < 35)


def main_2():
    """
    轴操作1：行，0：列
    :return:
    """
    
    a = np.ones((2, 3), dtype=np.int32)
    b = np.random.randint(low=1, high=10, size=(2, 3))
    c = a + b
    # print(c)
    # print(b.sum(), a.min(), a.max())  # 一元操作

    d = np.arange(12).reshape(3, 4)
    d1 = d.sum(axis=0)  # 对每一列进行求和
    d2 = d.min(axis=1)  # 找出每一行的最小值
    d3 = d.cumsum(axis=1)  # 对每行进行循环累加
    print(d, d1, d2, d3, sep='\n\n')


if __name__ == '__main__':
    # main()
    main_2()
