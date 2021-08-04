class LinkList:
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

    [归纳总结]
    对链表进行增删改查时，首先注意表空以及索引越界问题；
    之后的操作若包含拆除指针，应该先填写新节点，之后拆除旧链接。
    """

    def __init__(self):
        self.head = None
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

        current = self.head.next
        for i in range(0, index):
            current = current.next

        return current.val

    def addAtIndex(self, index: int, val: object) -> bool:
        pass

    def addAtHead(self, val: object) -> None:
        pass

    def addAtTail(self, val: object) -> None:
        pass

    def delete(self, index: int) -> bool:
        pass


class Graph:
    """
    基类图ADT设计

    Graph:
        data: object
        adjacent: object

        DFSTraverse() -> list
        BFSTraverse() -> list
    """

    def __init__(self):
        super(Graph, self).__init__()

        self._adjacent = None
        self.data = None

    @property
    def adjacent(self):
        return self._adjacent

    def DFSTraverse(self, start) -> list:
        pass

    def BFSTraverse(self, start) -> list:
        pass