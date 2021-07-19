"""
单向链表、双向链表、循环链表的py实现

@author: kevin
"""

"""
链表节点ADT设计

SingleLinkNode:
    next: SingleLinkNode  # 链接域
    val: object  # 数据域

DoubleLinkNode:
    pre: DoubleLinkNode  # 前置节点
    next: DoubleLinkNode  # 后置节点
    val: Object
"""

class SingleLinkNode:
    def __init__(self, *args):
        super(SingleLinkNode, self).__init__()

        self.next = None

        if args:
            self.val = args[0]
        else:
            self.val = None

class DoubleLinkNode:
    def __init__(self, *args):
        super(DoubleLinkNode, self).__init__()

        self.pre = None
        self.next = None

        if args:
            self.val = args[0]
        else:
            self.val = None


"""
基类链表ADT设计

[NOTE] 头节点链接域为空时，认为链表为空，长度为0；头节点为第0个元素

LinkList:
    head: *LinkNode
    val: object
    length: int
    
    isEmpty() -> bool
    display() -> None
    
    addAtIndex(index: int, val: object) -> bool
    addAtHead(val: object) -> None
    addAtTail(val: object) -> None
    
    delete(index: int) -> bool
    
    setVal(index: int, val: object) -> bool
    
    getVal(index: int) -> object
    
"""

class LinkList:
    def __init__(self):
        self.head = None
        self.val = None
        self._length = 0

    @property
    def length(self):
        return self._length

    @length.setter
    def _set_length(self, l):
        self._length = l

    def __len__(self):
        return self._length

    def isEmpty(self) -> bool:
        """
        Time: O(1)
        Space: O(1)

        :return: empty->Ture | ^empty->False
        """
        return self.head.next is None

    def addAtIndex(self, index: int, val: object) -> bool:
        pass

    def addAtHead(self, val: object) -> None:
        pass

    def addAtTail(self, val: object) -> None:
        pass

    def delete(self, index: int) -> bool:
        pass

    def setVal(self, index:int, val: object) -> bool:
        pass

    def getVal(self, index: int) -> object:
        pass

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

        :param val: 新节点值
        """
        new_node = SingleLinkNode(val)

        new_node.next = self.head.next
        self.head.next = new_node

        self._set_length += 1

    def addAtTail(self, val: object) -> None:
        """
        在链表结尾插入节点

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
        :param index: 待删除节点的位置
        :return:
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

