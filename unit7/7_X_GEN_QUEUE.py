from queue import Queue


def foo(func, args, *, callback):
    # 计算第一个函数结果
    result = func(*args)
    # 调用回调函数
    callback(result)


def bar(x, y):
    return x + y


def bar01(a, b):
    return max(a, b)


def bar02(a, b):
    return min(a, b)


def bar03(a, b):
    return a - b


def foo05():
    print('Begin')
    r = yield bar, (2, 3)
    print(r)
    r = yield bar01, (2, 3)
    print(r)
    r = yield bar02, (2, 3)
    print(r)
    print('Goodbye')


# 这里面实现了控制yeild与send的管理流程
f = foo05()
result_queue = Queue()
# 初始一个None,主要是用来启动生成器，
result_queue.put(None)
while True:
    try:
        a = f.send(result_queue.get())
        foo(a[0], a[1], callback=result_queue.put)
    except StopIteration:
        break
