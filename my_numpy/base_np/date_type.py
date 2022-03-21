import numpy as np

# np.astype:显式地转换数据类型, 生成一个新的数组

a: np.ndarray = np.arange(1, 6)
print(a, a.dtype, sep='\n')

float_a = a.astype(np.float_)
print(float_a, float_a.dtype, sep='\n')

# 字符串转浮点
numeric_string = np.array(['1.23', '-1.20', '33'], dtype=np.string_)
print(numeric_string, numeric_string.dtype)
float_numeric = numeric_string.astype(np.float_)
print(float_numeric)

# 使用其它数组的dtype
int_array = np.arange(4)
old = np.array([3.4, 2.4, 11.3])
new = old.astype(int_array.dtype)
print(old, new, sep='\n')

print("=======")
a = np.array([np.nan, 1, 2, np.nan, 3, 4, 5])
print(a[~np.isnan(a)])

b = np.array([1, 2 + 6j, 5, 3.5 + 5j])
print(b[np.iscomplex(b)])

print('特殊值')
a = np.array([np.nan, np.pi, 2, np.e, 3, 4, 5])
print(a, a[~np.isnan(a)], sep='\n')
b = np.array([1, 2+6j, 5, 4.3+5j])
print(b, b[np.iscomplex(b)], sep='\n')