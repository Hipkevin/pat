from dataStruct.node import DoubleLinkNode
from dataStruct.abstract import LinkList


class DoubleLinkList(LinkList):
    def __init__(self):
        super(DoubleLinkList, self).__init__()

        self.head = DoubleLinkNode()

    def __str__(self):
        string = 'head <-> '

        if not self.isEmpty():
            current = self.head.next
            while current is not None:
                string += str(current.val) + ' <-> '
                current = current.next

        return string

    def isEmpty(self) -> bool:
        """
        Time: O(1)
        Space: O(1)

        :return: empty->Ture | ^empty->False
        """
        return self.head.next is None and self.head.pre is None

    def addAtIndex(self, index: int, val: object) -> bool:
        """
        在index节点后插入新节点

        空表判断和越界判断与单向链表相同

        插入新节点时，通过current指针移动到index位置

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

        new_node = DoubleLinkNode(val)

        # 下标从0开始，current指针位于头节点上
        # 移动current指针至index
        current = self.head
        for i in range(0, index):
            current = current.next

        # 填写new_node的链接域
        new_node.next = current.next
        new_node.pre = current

        # 将当前节点的next指向new_node
        # 必须先将current的后置节点的pre指针指向new_node
        if current.next:
            current.next.pre = new_node
        current.next = new_node

        self._set_length += 1
        return True

    def addAtHead(self, val: object) -> None:
        """
        在头部插入新节点

        插入过程与在指定位置插入相同

        :param val: 新节点值
        """
        new_node = DoubleLinkNode(val)

        new_node.next = self.head.next
        new_node.pre = self.head

        if not self.isEmpty():
            self.head.next.pre = new_node

        self.head.next = new_node

        self._set_length += 1

    def addAtTail(self, val: object) -> None:
        """
        在链表结尾插入新节点

        :param val: 新节点值
        """
        new_node = DoubleLinkNode(val)

        # 移动current指针至最后一个节点
        current = self.head
        while current.next is not None:
            current = current.next

        new_node.pre = current
        current.next = new_node

        self._set_length += 1

    def delete(self, index: int) -> bool:
        """
        删除指定位置的节点

        :param index: 待删除的节点位置
        :return: 是否删除成功
        """
        if self.isEmpty():
            return True

        if index < 1 or index > self._length:
            return False

        else:
            # current指针从头节点出发，移动至index-1
            current = self.head
            for i in range(0, index - 1):
                current = current.next

            # 最后操作current指针
            # 否则current指针改变，后续修改会发生错误
            if current.next.next:
                current.next.next.pre = current

            current.next = current.next.next

        self._set_length -= 1
        return True

    def display(self) -> None:
        print('head <-> ', end='')

        if not self.isEmpty():
            current = self.head.next
            while current is not None:
                print(current.val, '<-> ', end='')
                current = current.next

            print()
