import unittest
from src.linked_list import Node, LinkedList

n = Node(1, 2)
test_linked_list = LinkedList()


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next_node, 2)


class TestLinkedList(unittest.TestCase):
    pass
