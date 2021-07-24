"""
基于线性表和单向链表的队列
"""

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