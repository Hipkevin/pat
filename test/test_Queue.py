import unittest
from dataStruct.queue import LinkQueue, LinearQueue, BaseQueue

class QueueTest(unittest.TestCase):

    def test_isEmpty(self):
        link_q = LinkQueue()
        linear_q = LinearQueue()
        base_q = BaseQueue()

        self.assertEqual(link_q.isEmpty(), True)
        self.assertEqual(linear_q.isEmpty(), True)
        self.assertEqual(base_q.isEmpty(), True)

        link_q.push(1)
        linear_q.push(1)
        base_q.push(1)

        self.assertEqual(link_q.isEmpty(), False)
        self.assertEqual(linear_q.isEmpty(), False)
        self.assertEqual(base_q.isEmpty(), False)

    def test_push_pop(self):
        link_q = LinkQueue(2)
        linear_q = LinearQueue(2)
        base_q = BaseQueue(2)

        link_q.push(1)
        linear_q.push(1)
        base_q.push(1)

        self.assertEqual(link_q.push(2), True)
        self.assertEqual(linear_q.push(2), True)
        self.assertEqual(base_q.push(2), True)

        self.assertEqual(link_q.push(3), False)
        self.assertEqual(linear_q.push(3), False)
        self.assertEqual(base_q.push(3), False)

        self.assertEqual(link_q.pop(), 1)
        self.assertEqual(linear_q.pop(), 1)
        self.assertEqual(base_q.pop(), 1)

    def test_baseStack(self):
        base_q = BaseQueue(3)

        base_q.push(1)
        base_q.push(2)
        base_q.push(3)

        self.assertEqual(base_q.push(4), False)

        self.assertEqual(base_q.pop(), 1)
        self.assertEqual(base_q.pop(), 2)

        base_q.push(4)
        base_q.push(5)

        self.assertEqual(base_q.push(6), False)