import unittest
from src.linked_list import Node, LinkedList

n = Node(1, 2)
test_linked_list = LinkedList()


class TestNode(unittest.TestCase):
    def test_node(self):
        self.assertEqual(n.data, 1)
        self.assertEqual(n.next_node, 2)


class TestLinkedList(unittest.TestCase):

    def test_insert_beginning(self):
        test_linked_list.insert_beginning({'a': 1})
        self.assertEqual(test_linked_list.head.data, {'a': 1})
        test_linked_list.insert_beginning({'a': 2})
        self.assertEqual(test_linked_list.head.data, {'a': 2})
        self.assertEqual(test_linked_list.head.next_node.data, {'a': 1})
        self.assertEqual(test_linked_list.tail.data, {'a': 1})

    def test_insert_at_end(self):
        test_linked_list.insert_at_end({'a': 3})
        self.assertEqual(test_linked_list.head.data, {'a': 3})
        self.assertEqual(test_linked_list.tail.data, {'a': 3})
        test_linked_list.insert_at_end({'a': 4})
        self.assertEqual(test_linked_list.head.data, {'a': 3})
        self.assertEqual(test_linked_list.tail.data, {'a': 4})
        test_linked_list.insert_at_end({'a': 5})
        self.assertEqual(test_linked_list.head.data, {'a': 3})
        self.assertEqual(test_linked_list.head.next_node.data, {'a': 4})
        self.assertEqual(test_linked_list.tail.data, {'a': 5})
        self.assertEqual(test_linked_list.tail.next_node, None)

    def test_str(self):
        self.assertEqual(str(test_linked_list), 'None')
        test_linked_list.insert_beginning({'a': 1})
        test_linked_list.insert_beginning({'a': 2})
        test_linked_list.insert_at_end({'a': 3})
        test_linked_list.insert_at_end({'a': 4})
        self.assertEqual(str(test_linked_list), "{'a': 2} -> {'a': 1} -> {'a': 3} -> {'a': 4} -> None")
