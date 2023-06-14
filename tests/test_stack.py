import unittest
from src import stack

test_node_1 = stack.Node('test_1', 1)
test_node_2 = stack.Node('test_2', 2)


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertEqual(test_node_1.data, 'test_1')
        self.assertEqual(test_node_2.next_node, 2)
