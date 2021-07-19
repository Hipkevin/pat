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