"""
二叉树的py实现
链式存储+顺序存储
"""

from dataStruct.node import BinaryLinkNode

class BinaryTree:
    def __init__(self, *args):
        super(BinaryTree, self).__init__()

        if not args:
            self.root = BinaryLinkNode(0)
        else:
            self.root = BinaryLinkNode(args[0])

    @staticmethod
    def makeTree(root: BinaryLinkNode, left, right):
        root.left = left
        root.right = right

    def deleteTree(self, root):
        if root:
            self.deleteTree(root.left)
            self.deleteTree(root.right)

        root = None
        return root

    def _recurrentHeight(self, root):
        # 递归出口
        if not root:
            return 0

        else:
            left_h = self._recurrentHeight(root.left)
            right_h = self._recurrentHeight(root.right)

            if left_h > right_h:
                left_h += 1
                return left_h
            else:
                right_h += 1
                return right_h

    def getHeight(self):
        return self._recurrentHeight(self.root)

    def _recurrentCount(self, root, count):
        # 递归出口
        if not root:
            return 0

        else:
            count += 1

            count += self._recurrentCount(root.left, 0)
            count += self._recurrentCount(root.right, 0)

            return count

    def getCount(self):
        return self._recurrentCount(self.root, 0)

    def _preRecurrent(self, root, res: list):
        if not root:
            return []

        else:
            res.append(root.val)
            res += self._preRecurrent(root.left, [])
            res += self._preRecurrent(root.right, [])

            return res

    def _inRecurrent(self, root, res: list):
        if not root:
            return []

        else:
            res += self._inRecurrent(root.left, [])
            res.append(root.val)
            res += self._inRecurrent(root.right, [])

            return res

    def _postRecurrent(self, root, res: list):
        if not root:
            return []

        else:
            res += self._postRecurrent(root.left, [])
            res += self._postRecurrent(root.right, [])
            res.append(root.val)

            return res

    def preOrderRecursive(self):
        return self._preRecurrent(self.root, [])

    def inOrderRecursive(self):
        return self._inRecurrent(self.root, [])

    def postOrderRecursive(self):
        return self._postRecurrent(self.root, [])