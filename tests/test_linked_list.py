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
        self.assertEqual(str(test_list_3), "{'c': 2} -> {'c': 1} -> {'c': 3} -> {'c': 4} -> None")

    def test_to_list(self):
        test_list_4 = LinkedList()
        self.assertEqual(test_list_4.to_list(), [])
        test_list_4.insert_beginning({'d': 1})
        test_list_4.insert_beginning({'d': 2})
        test_list_4.insert_at_end({'d': 3})
        test_list_4.insert_at_end({'d': 4})
        self.assertEqual(test_list_4.to_list(), [{'d': 2}, {'d': 1}, {'d': 3}, {'d': 4}])

    def test_get_data_by_id(self):
        test_list_5 = LinkedList()
        test_list_5.insert_beginning({'id': 1, 'e': 'test_1'})
        test_list_5.insert_beginning({'id': 2, 'e': 'test_2'})
        test_list_5.insert_at_end({'id': 3, 'e': 'test_3'})
        test_list_5.insert_at_end({'id': 4, 'e': 'test_4'})
        self.assertEqual(test_list_5.get_data_by_id(2), {'id': 2, 'e': 'test_2'})
        self.assertEqual(test_list_5.get_data_by_id(4), {'id': 4, 'e': 'test_4'})
        # test_list_5.insert_at_end({'id': 6, 'e': 'test_6'})
        # test_list_5.insert_at_end({'e': 'test_7'})
        # test_list_5.insert_at_end('test_8')
        # self.assertRaises(TypeError, test_list_5.get_data_by_id(5))
        # self.assertRaises(test_list_5.get_data_by_id(7), TypeError)
        # self.assertRaises(test_list_5.get_data_by_id(8), TypeError)
