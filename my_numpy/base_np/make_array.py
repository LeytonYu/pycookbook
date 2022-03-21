import numpy as np


a = np.array([2, 3, 4])
b = np.array('hello world')
c = np.zeros((5, ), dtype=np.float_)
d = np.ones((2, 3, 4), dtype=np.int32)
e = np.empty((2, 3))
f = np.full((3, 4), 6.66)
g = np.arange(10, 30, 5)    # 步长
h = np.linspace(0, 2, 9)    # 个数(等差数列)
i = np.linspace(0, 2*np.pi, 100)
j = np.sin(i)

lst = [a, b, c, d, e, f, g, h, i, j]
for value in lst:
    print(value)
    print('======')

print(np.sin(np.pi/2/2))