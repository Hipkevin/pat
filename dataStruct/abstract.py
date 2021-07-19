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

    def setVal(self, index: int, val: object) -> bool:
        pass

    def getVal(self, index: int) -> object:
        pass