from dataStruct.node import SingleLinkNode
from dataStruct.abstract import LinkList


class RecurrentLinkList(LinkList):
    def __init__(self):
        super(RecurrentLinkList, self).__init__()

        self.head = SingleLinkNode()

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