"""
单向链表的py实现

@author: kevin
"""

from node import SingleLinkNode
from abstract import LinkList


class SingleLinkList(LinkList):
    def __init__(self):
        super(SingleLinkList, self).__init__()

        # 初始化头节点
        self.head = SingleLinkNode()

    def __str__(self):
        string = 'head -> '

        if not self.isEmpty():
            current = self.head.next
            while current is not None:
                string += str(current.val) + ' -> '
                current = current.next

        return string

    def addAtIndex(self, index: int, val: object) -> bool:
        """
        将新元素插入第index位之后
        index范围是[0, length]

        表为空：作为第一个元素
        表非空 && 未越界：插入指定位置并返回True，否则返回False

        Time: O(n)
        Space: O(1)

        :param index: 插入位置
        :param val: 新节点的值
        :return: 是否插入成功
        """

        if index < 0 or index > self._length:
            # 表非空 && 越界 -> 插入失败
            if not self.isEmpty():
                return False

            # 表空 && 越界 -> 插入头节点
            else:
                index = 0

        new_node = SingleLinkNode(val)

        # 下标从0开始，current指针位于头节点上
        # 移动current指针至index
        current = self.head
        for i in range(0, index):
            current = current.next

        new_node.next = current.next
        current.next = new_node

        self._set_length += 1
        return True

    def addAtHead(self, val: object) -> None:
        """
        在表头节点后插入节点

        Time: O(1)
        Space: O(1)

        :param val: 新节点值
        """
        new_node = SingleLinkNode(val)

        new_node.next = self.head.next
        self.head.next = new_node

        self._set_length += 1

    def addAtTail(self, val: object) -> None:
        """
        在链表结尾插入节点

        Time: O(n)
        Space: O(1)

        :param val: 新节点值
        """
        new_node = SingleLinkNode(val)

        # 移动current指针至最后一个节点
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node

        self._set_length += 1

    def delete(self, index: int) -> bool:
        """
        删除指定位置的节点

        表为空：返回True
        表非空 && 未越界：删除指定位置元素并返回True，否则返回False

        Time: O(n)
        Space: O(1)

        :param index: 待删除节点的位置
        :return: 是否删除成功
        """
        if self.isEmpty():
            return True

        if index < 1 or index > self._length:
            return False

        else:
            # current指针从头节点出发，移动至index-1
            current = self.head
            for i in range(0, index-1):
                current = current.next

            current.next = current.next.next

        self._set_length -= 1
        return True

    def setVal(self, index: int, val: object) -> bool:
        # 表空 -> 设置失败
        if self.isEmpty():
            return False

        # 表非空 && 越界 -> 设置失败
        if index < 0 or index > self._length:
            return False

        current = self.head
        for i in range(0, index):
            current = current.next

        current.val = val

        return True

    def getVal(self, index: int) -> object:
        # 表非空 && 越界
        if not self.isEmpty() and (index < 0 or index > self._length):
            return False

        current = self.head
        for i in range(0, index):
            current = current.next

        return current.val

    def display(self) -> None:
        print('head -> ', end='')

        if not self.isEmpty():
            current = self.head.next
            while current is not None:
                print(current.val, '-> ', end='')
                current = current.next

            print()