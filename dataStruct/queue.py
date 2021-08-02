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
            res = self.data.findByIndex(0)
            self.data.delete(0)

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
            res = self.data.getVal(0)
            self.data.delete(0)
            return res

class BaseQueue(Queue):
    def __init__(self, max_space_size=10):
        self.data = [None] * (max_space_size + 1)
        self.max_space_size = max_space_size

        self.__front = 0
        self.__tail = 0

    def isEmpty(self) -> bool:
        return self.__front == self.__tail

    def isFull(self) -> bool:
        return self.__front == (self.__tail + 1) % (self.max_space_size + 1)

    def push(self, val: object) -> bool:
        if self.isFull():
            return False

        else:
            self.__tail = (self.__tail + 1) % (self.max_space_size + 1)
            self.data[self.__tail] = val
            return True

    def pop(self) -> object:
        if self.isEmpty():
            return None

        else:
            self.__front = (self.__front + 1) % (self.max_space_size + 1)

            return self.data[self.__front]