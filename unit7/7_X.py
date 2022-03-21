import math
from functools import partial
import logging
from multiprocessing import Pool


def lambda_arg():
    func = [lambda x, a=n: x + a for n in range(5)]

    for f in func:
        print(f(0))


def feel_partial():
    def spam(a, b, c, d):
        print(a, b, c, d)

    spam(1, 2, 3, 4)
    s1 = partial(spam, 1)
    s1(12, 23, 14)
    s2 = partial(spam, d=9)
    s2(5, 4, 3)


def cook_partial():
    def distance(p1, p2):
        x1, y1 = p1
        x2, y2 = p2
        return math.hypot(x1 - x2, y1 - y2)

    pt = (4, 3)
    points = [(1, 2), (3, 4), (5, 6), (7, 8)]
    points.sort(key=partial(distance, pt))
    print(points)


def output_result(result, log=None):
    if log is not None:
        log.debug('Got: %r', result)


# A sample function
def add(x, y):
    return x + y


def callback_partial():
    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger('leyton_test')

    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


def apply_async(func, args, *, callback):
    result = func(*args)

    callback(result)


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))

    return handler


def make_handler_gevent():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {}'.format(sequence, result))


def extra_callback():
    handler = make_handler()
    apply_async(add, (3, 4), callback=handler)
    apply_async(add, (7, 8), callback=handler)


def extra_callback_gevent():
    handler = make_handler_gevent()
    next(handler)
    apply_async(add, (3, 5), callback=handler.send)
    apply_async(add, ('hello', 'world'), callback=handler.send)


if __name__ == '__main__':
    # callback_partial()
    # feel_partial()
    # cook_partial()
    extra_callback_gevent()