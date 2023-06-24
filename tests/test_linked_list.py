import unittest
from src.linked_list import Node, LinkedList

n = Node(1, 2)


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next_node, 2)


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        test_list_1 = LinkedList()
        test_list_1.insert_beginning({'a': 1})
        self.assertEqual(test_list_1.head.data, {'a': 1})
        test_list_1.insert_beginning({'a': 2})
        self.assertEqual(test_list_1.head.data, {'a': 2})
        self.assertEqual(test_list_1.head.next_node.data, {'a': 1})
        self.assertEqual(test_list_1.tail.data, {'a': 1})

    def test_insert_at_end(self):
        test_list_2 = LinkedList()
        test_list_2.insert_at_end({'b': 3})
        self.assertEqual(test_list_2.head.data, {'b': 3})
        self.assertEqual(test_list_2.tail.data, {'b': 3})
        test_list_2.insert_at_end({'b': 4})
        self.assertEqual(test_list_2.head.data, {'b': 3})
        self.assertEqual(test_list_2.tail.data, {'b': 4})
        test_list_2.insert_at_end({'b': 5})
        self.assertEqual(test_list_2.head.data, {'b': 3})
        self.assertEqual(test_list_2.head.next_node.data, {'b': 4})
        self.assertEqual(test_list_2.tail.data, {'b': 5})
        self.assertEqual(test_list_2.tail.next_node, None)

    def test_str(self):
        test_list_3 = LinkedList()
        self.assertEqual(str(test_list_3), 'None')
        test_list_3.insert_beginning({'c': 1})
        test_list_3.insert_beginning({'c': 2})
        test_list_3.insert_at_end({'c': 3})
        test_list_3.insert_at_end({'c': 4})
        self.assertEqual(str(test_list_3), " {'c': 2} -> {'c': 1} -> {'c': 3} -> {'c': 4} -> None")
