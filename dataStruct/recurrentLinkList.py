from dataStruct.node import SingleLinkNode
from dataStruct.abstract import LinkList


class RecurrentLinkList(LinkList):
    def __init__(self):
        super(RecurrentLinkList, self).__init__()

        self.head = SingleLinkNode()
        self.head.next = self.head

    def __str__(self):
        string = 'head -> '

        if not self.isEmpty():
            current = self.head.next
            for i in range(self.length):
                string += str(current.val) + ' -> '
                current = current.next

        return string + 'head'

    def isEmpty(self) -> bool:
        """
        Time: O(1)
        Space: O(1)

        :return: empty->Ture | ^empty->False
        """
        return self.head.next is self.head

    def addAtIndex(self, index: int, val: object) -> bool:
        """
        在指定位置插入新节点

        插入过程与单向链表相同（写法完全相同）
        尾节点指向头节点

        :param index: 插入位置
        :param val: 新节点值
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
        与单向链表完全一致

        :param val: 新节点的值
        """
        new_node = SingleLinkNode(val)

        new_node.next = self.head.next
        self.head.next = new_node

        self._set_length += 1

    def addAtTail(self, val: object) -> None:
        """
        修改while写法为for
        尾节点指向头节点

        :param val: 新节点值
        """
        new_node = SingleLinkNode(val)

        # 移动current指针至最后一个节点
        current = self.head
        for i in range(self.length):
            current = current.next

        current.next = new_node
        new_node.next = self.head

        self._set_length += 1

    def delete(self, index: int) -> bool:
        if self.isEmpty():
            return True

        if index < 1 or index > self._length:
            return False

        else:
            # current指针从头节点出发，移动至index-1
            current = self.head
            for i in range(0, index - 1):
                current = current.next

            current.next = current.next.next

        self._set_length -= 1
        return True

    def display(self):
        print('head -> ', end='')

        if not self.isEmpty():
            current = self.head.next
            for i in range(self.length):
                print(current.val, '-> ', end='')
                current = current.next

            print('head')