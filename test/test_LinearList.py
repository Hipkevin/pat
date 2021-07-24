import unittest
from dataStruct.linearList import LinearList

class LinearListTest(unittest.TestCase):
    """
    单向链表单元测试类

    对单向链表的基本操作进行覆盖测试
    """

    def test_isEmpty(self):
        linearList = LinearList()
        self.assertEqual(linearList.isEmpty(), True)

        linearList.insert(0, 2)
        self.assertEqual(linearList.isEmpty(), False)

    def test_findByIndex(self):
        linearList = LinearList()

        self.assertEqual(linearList.findByIndex(0), None)

        linearList.insert(0, 2)
        linearList.insert(0, 4)
        self.assertEqual(linearList.findByIndex(0), 4)

    def test_findElementByVal(self):
        linearList = LinearList()

        self.assertEqual(linearList.findElementByVal(0), None)

        linearList.insert(0, 2)
        linearList.insert(0, 4)
        self.assertEqual(linearList.findElementByVal(2), 1)

    def test_findElementsByVal(self):
        linearList = LinearList()

        self.assertEqual(linearList.findElementsByVal(0), list())

        linearList.insert(0, 2)
        linearList.insert(0, 4)
        linearList.insert(0, 2)
        self.assertEqual(linearList.findElementsByVal(2), [0, 2])

    def test_delete(self):
        linearList = LinearList()

        linearList.insert(0, 2)
        linearList.insert(0, 4)
        self.assertEqual(linearList.findElementByVal(2), 1)

        linearList.delete(1)
        self.assertEqual(linearList.findElementByVal(2), None)

    def test_str(self):
        linearList = LinearList()

        linearList.insert(0, 1)
        linearList.insert(0, 2)
        self.assertEqual(str(linearList), '[2, 1]')


if __name__ == '__main__':
    unittest.main()