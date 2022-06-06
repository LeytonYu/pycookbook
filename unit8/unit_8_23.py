"""循环引用数据结构的内存管理"""
import weakref


class Data:
    def __del__(self):
        print('Data.__del__')


class Node():
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return 'Node({!r:})'.format(self.value)

    # property that manages the parent as a weak-reference
    @property
    def parent(self):
        return None if self._parent is None else self._parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)    # 弱引用

    def add_child(self, child):
        self.children.append(child)
        child.parent = self
