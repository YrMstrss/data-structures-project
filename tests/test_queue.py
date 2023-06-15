import unittest
from src import queue

test_queue = queue.Queue()
test_queue.enqueue('test_1')
test_queue.enqueue('test_2')
test_queue.enqueue('test_3')
test_queue.enqueue('test_4')


class TestQueue(unittest.TestCase):
    def test_queue_enqueue(self):
        self.assertEqual(test_queue.head.data, 'test_1')
        self.assertEqual(test_queue.head.next_node.data, 'test_2')
        self.assertEqual(test_queue.head.next_node.next_node.data, 'test_3')
        self.assertEqual(test_queue.head.next_node.next_node.next_node.data, 'test_4')
        self.assertEqual(test_queue.tail.data, 'test_4')
        self.assertEqual(test_queue.tail.next_node, None)

    def test_queue_str(self):
        new_test_queue = queue.Queue()
        self.assertEqual(str(new_test_queue), "")
        new_test_queue.enqueue('test_1')
        new_test_queue.enqueue('test_2')
        self.assertEqual(str(new_test_queue), "test_1\ntest_2")

    def test_queue_dequeue(self):
        self.assertEqual(test_queue.dequeue(), "test_1")
        self.assertEqual(test_queue.dequeue(), "test_2")
        self.assertEqual(test_queue.dequeue(), "test_3")
        self.assertEqual(test_queue.dequeue(), "test_4")
        self.assertIs(test_queue.dequeue(), None)
