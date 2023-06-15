class Node:
    """Класс для узла очереди"""

    def __init__(self, data, next_node):
        """
        Конструктор класса Node

        :param data: данные, которые будут храниться в узле
        """
        self.data = data
        self.next_node = next_node


class Queue:
    """Класс для очереди"""

    def __init__(self):
        """Конструктор класса Queue"""
        self.head = None
        self.tail = None

    def __str__(self):
        if self.head is None:
            return ""
        else:
            result = [self.head.data]
            data_writer = self.head.next_node
            while True:
                if data_writer is not None:
                    result.append(data_writer.data)
                    data_writer = data_writer.next_node
                else:
                    break
            return '\n'.join(result)

    def enqueue(self, data):
        """
        Метод для добавления элемента в очередь

        :param data: данные, которые будут добавлены в очередь
        """
        data_node = Node(data, None)
        if self.head is None:
            self.head = data_node
            self.tail = data_node
        elif self.head.next_node is None:
            self.tail = data_node
            self.head.next_node = data_node
        else:
            self.tail.next_node = data_node
            self.tail = data_node

    def dequeue(self):
        """
        Метод для удаления элемента из очереди. Возвращает данные удаленного элемента

        :return: данные удаленного элемента
        """
        if self.head is not None:
            data_to_return = self.head.data
            self.head = self.head.next_node
            return data_to_return
