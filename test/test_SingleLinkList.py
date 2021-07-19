import unittest
from dataStruct.singleLinkList import SingleLinkList

class SingleLinkListTest(unittest.TestCase):
    """
    单向链表单元测试类

    对单向链表的基本操作进行覆盖测试
    """

    def test_isEmpty(self):
        linkList = SingleLinkList()
        self.assertEqual(linkList.isEmpty(), True)

        linkList.addAtHead(2)
        self.assertEqual(linkList.isEmpty(), False)

    def test_addAtIndex(self):
        linkList = SingleLinkList()

        self.assertEqual(linkList.addAtIndex(0, 5), True)
        self.assertEqual(linkList.addAtIndex(1, 5), True)
        self.assertEqual(linkList.addAtIndex(3, 5), False)
        self.assertEqual(linkList.addAtIndex(1, 5), True)
        linkList.display()

    def test_addAtHead(self):
        linkList = SingleLinkList()

        linkList.addAtHead(2)
        linkList.addAtHead(3)

        self.assertEqual(linkList.length, 2)
        self.assertEqual(linkList.head.next.val, 3)

    def test_addAtTail(self):
        linkList = SingleLinkList()

        linkList.addAtTail(2)
        linkList.addAtTail(3)

        self.assertEqual(linkList.length, 2)
        self.assertEqual(linkList.head.next.val, 2)

    def test_delete(self):
        linkList = SingleLinkList()

        self.assertEqual(linkList.delete(2), True)

        linkList.addAtHead(2)
        self.assertEqual(linkList.delete(2), False)

        linkList.addAtTail(3)
        self.assertEqual(linkList.delete(2), True)

    def test_setVal(self):
        linkList = SingleLinkList()

        self.assertEqual(linkList.setVal(2, 1), False)

        linkList.addAtTail(3)
        self.assertEqual(linkList.setVal(2, 1), False)
        self.assertEqual(linkList.setVal(1, 1), True)

    def test_str(self):
        linkList = SingleLinkList()

        linkList.addAtTail(3)
        self.assertEqual(str(linkList), 'head -> 3 -> ')


if __name__ == '__main__':
    unittest.main()