import unittest
from dataStruct.tree import BinaryTree, BinaryLinkNode

class BinaryTreeTest(unittest.TestCase):

    def setUp(self) -> None:
        self.tree = BinaryTree()

        nodeSet = [BinaryLinkNode(1), BinaryLinkNode(2), BinaryLinkNode(3), BinaryLinkNode(4)]
        self.tree.makeTree(self.tree.root, nodeSet[0], nodeSet[1])
        self.tree.makeTree(nodeSet[0], nodeSet[2], nodeSet[3])

    def test_getHeight(self):
        self.assertEqual(self.tree.getHeight(), 3)

    def test_count(self):
        self.assertEqual(self.tree.getCount(), 5)

    def test_recursiveTraverse(self):
        self.assertEqual(self.tree.preOrderRecursive(), [0, 1, 3, 4, 2])
        self.assertEqual(self.tree.inOrderRecursive(), [3, 1, 4, 0, 2])
        self.assertEqual(self.tree.postOrderRecursive(), [3, 4, 1, 2, 0])

    def test_delete(self):
        self.tree.root.right = self.tree.deleteTree(self.tree.root.right)

        self.assertEqual(self.tree.preOrderRecursive(), [0, 1, 3, 4])
        self.assertEqual(self.tree.inOrderRecursive(), [3, 1, 4, 0])
        self.assertEqual(self.tree.postOrderRecursive(), [3, 4, 1, 0])