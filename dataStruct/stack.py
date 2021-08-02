"""
基于线性表和单向链表实现栈
"""

from dataStruct.linearList import LinearList
from dataStruct.singleLinkList import SingleLinkList

class Stack:
    def __init__(self, max_space_size=10):
        super(Stack, self).__init__()
        self.data = None
        self.max_space_size = max_space_size

    def __len__(self):
        return len(self.data)

    def __str__(self):
        return str(self.data)

    def isEmpty(self) -> bool:
        pass

    def push(self, val: object) -> bool:
        pass

    def pop(self) -> object:
        pass

class LinearStack(Stack):
    def __init__(self, max_space_size=10):
        super(LinearStack, self).__init__()

        self.max_space_size = max_space_size
        self.data = LinearList(self.max_space_size)

    def isEmpty(self) -> bool:
        return self.data.isEmpty()

    def push(self, val: object) -> bool:
        if len(self.data) == self.max_space_size:
            return False

        else:
            self.data.insert(0, val)
            return True

    def pop(self) -> object:
        if self.isEmpty():
            return None

        else:
            res = self.data.findByIndex(0)
            self.data.delete(1)
            return res

class LinkStack(Stack):
    def __init__(self, max_space_size=10):
        super(LinkStack, self).__init__()

        self.max_space_size = max_space_size
        self.data = SingleLinkList()

    def isEmpty(self) -> bool:
        return self.data.isEmpty()

    def push(self, val: object) -> bool:
        if len(self.data) == self.max_space_size:
            return False

        else:
            self.data.addAtHead(val)
            return True

    def pop(self) -> object:
        if self.isEmpty():
            return None

        else:
            res = self.data.getVal(0)
            self.data.delete(0)
            return res