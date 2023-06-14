import unittest
from src import stack

test_node_1 = stack.Node('test_1', 1)
test_node_2 = stack.Node('test_2', 2)


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertEqual(test_node_1.data, 'test_1')
        self.assertEqual(test_node_2.next_node, 2)


test_stack = stack.Stack()
test_stack.push('data1')
test_stack.push('data2')
test_stack.push('data3')


class TestStack(unittest.TestCase):
    def test_stack_push(self):
        self.assertEqual(test_stack.top.data, 'data3')
        self.assertEqual(test_stack.top.next_node.data, 'data2')
        self.assertEqual(test_stack.top.next_node.next_node.data, 'data1')

    def test_stack_pop(self):
        self.assertEqual(test_stack.pop(), 'data3')
        self.assertEqual(test_stack.top.data, 'data2')
        self.assertEqual(test_stack.top.next_node.data, 'data1')
