# 让对象支持上下文管理
from functools import partial
from socket import socket, AF_INET, SOCK_STREAM


class LazyConnection:
    def __init__(self, address, family=AF_INET, stype=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = stype
        self.socket = None

    def __enter__(self):
        if self.socket is not None:
            raise RuntimeError('Already exists socket')
        self.socket = socket(family=self.family, type=self.type)
        self.socket.connect(self.address)
        return self.socket

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.socket.close()
        self.socket = None


class LazyConnectionPool:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


def main():
   conn = LazyConnection(address=('www.python.org', 80))
   with conn as s:
       s.send(b'GET /index.html HTTP/1.0\r\n')
       s.send(b'Host: www.python.org\r\n')
       s.send(b'\r\n')
       resp = b''.join(iter(partial(s.recv, 8192), b''))
       print(resp)


def test_pool():
    # 连接池，s和s2是互相独立的连接
    conn = LazyConnectionPool(address=('www.python.org', 80))
    with conn as s:
        s.send(b'GET /index.html HTTP/1.0\r\n')
        s.send(b'Host: www.python.org\r\n')
        s.send(b'\r\n')
        resp = b''.join(iter(partial(s.recv, 8192), b''))
        print(resp)
        with conn as s2:
            s2.send(b'GET /index.html HTTP/1.0\r\n')
            s2.send(b'Host: www.python.org\r\n')
            s2.send(b'\r\n')
            resp = b''.join(iter(partial(s2.recv, 8192), b''))
            print(resp)


if __name__ == '__main__':
    # main()
    test_pool()