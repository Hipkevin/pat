"""
基于线性表和单向链表的队列
"""

from dataStruct.linearList import LinearList
from dataStruct.singleLinkList import SingleLinkList


class Queue:
    def __init__(self, max_space_size=10):
        self.data = None
        self.max_space_size = max_space_size

    def __str__(self):
        return str(self.data)

    def isEmpty(self) -> bool:
        pass

    def push(self, val: object) -> bool:
        pass

    def pop(self) -> object:
        pass


class LinearQueue(Queue):
    def __init__(self, max_space_size=10):
        super(LinearQueue, self).__init__()

        self.max_space_size = max_space_size
        self.data = LinearList(max_space_size)

    def isEmpty(self) -> bool:
        return self.data.isEmpty()

    def push(self, val: object) -> bool:
        if self.data.length == self.max_space_size:
            return False

        else:
            self.data.insert(self.data.length, val)
            return True

    def pop(self) -> object:
        if self.data.isEmpty():
            return None

        else:
            res = self.data.findByIndex(self.data.length-1)
            self.data.delete(self.data.length-1)

            return res

class LinkQueue(Queue):
    def __init__(self, max_space_size=10):
        super(LinkQueue, self).__init__()

        self.max_space_size = max_space_size
        self.data = SingleLinkList()

    def isEmpty(self) -> bool:
        return self.data.isEmpty()

    def push(self, val: object) -> bool:
        if self.data.length == self.max_space_size:
            return False

        else:
            self.data.addAtTail(val)
            return True

    def pop(self) -> object:
        if self.data.isEmpty():
            return None

        else:
            res = self.data.getVal(self.data.length)
            self.data.delete(self.data.length)
            return res