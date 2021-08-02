import unittest
from dataStruct.stack import LinkStack, LinearStack

class StackTest(unittest.TestCase):
    def test_isEmpty(self):
        link_stack = LinkStack()
        linear_stack = LinearStack()

        self.assertEqual(link_stack.isEmpty(), True)
        self.assertEqual(linear_stack.isEmpty(), True)

        link_stack.push(2)
        linear_stack.push(2)

        self.assertEqual(link_stack.isEmpty(), False)
        self.assertEqual(linear_stack.isEmpty(), False)

    def test_push_pop(self):
        link_stack = LinkStack(1)
        linear_stack = LinearStack(1)

        self.assertEqual(link_stack.push(2), True)
        self.assertEqual(linear_stack.push(2), True)

        self.assertEqual(link_stack.push(3), False)
        self.assertEqual(linear_stack.push(3), False)

        self.assertEqual(link_stack.pop(), 2)
        self.assertEqual(linear_stack.pop(), 2)