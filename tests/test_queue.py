import unittest
from src import queue

test_queue = queue.Queue()
test_queue.enqueue('test_1')
test_queue.enqueue('test_2')
test_queue.enqueue('test_3')


class TestQueue(unittest.TestCase):
    def test_queue_enqueue(self):
        self.assertEqual(test_queue.head.data, 'test_1')
        self.assertEqual(test_queue.head.next_node.data, 'test_2')
        self.assertEqual(test_queue.head.next_node.next_node.data, 'test_3')
        self.assertEqual(test_queue.tail.data, 'test_3')
        self.assertEqual(test_queue.tail.next_node, None)
