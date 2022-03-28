import sys


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals
        # Update instance dictionary with callables
        self.__dict__.update((key, value) for key, value in locals.items()
                             if callable(value))

    # Redirect special methods
    def __len__(self):
        return self.__dict__['__len__']()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop():
        return items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


def main():
    s = Stack()
    s.push('first')
    s.push('leyton')
    s.push('haha')
    length = len(s)
    while length > 0:
        length -= 1
        print(s.pop())


if __name__ == '__main__':
    main()