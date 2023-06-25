class Node:
    """Класс для узла односвязного списка"""

    def __init__(self, data, next_node):
        self.data = data
        self.next_node = next_node


class LinkedList:
    """Класс для односвязного списка"""

    def __init__(self):
        self.head = None
        self.tail = None

    def insert_beginning(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в начало связанного списка"""
        if self.head == self.tail is None:
            self.head = Node(data, None)
            self.tail = self.head
        else:
            self.head = Node(data, self.head)

    def insert_at_end(self, data: dict) -> None:
        """Принимает данные (словарь) и добавляет узел с этими данными в конец связанного списка"""

        new_node = Node(data, None)

        if self.head == self.tail is None:
            self.head = new_node
            self.tail = new_node
        elif self.head.next_node is None:
            self.head.next_node = new_node
            self.tail = new_node
        else:
            current_tail = self.tail
            current_tail.next_node = new_node
            self.tail = new_node

    def __str__(self) -> str:
        """Вывод данных односвязного списка в строковом представлении"""
        node = self.head
        if node is None:
            return str(None)

        ll_string = ''
        while node:
            ll_string += f'{str(node.data)} -> '
            node = node.next_node

        ll_string += 'None'
        return ll_string

    def to_list(self):
        """Возвращает список с данными, содержащимися в односвязном списке"""
        node = self.head
        if node is None:
            return []

        ll_list = []
        while node:
            ll_list.append(node.data)
            node = node.next_node

        return ll_list

    def get_data_by_id(self, id_item):
        """Возвращает первый найденный в `LinkedList` словарь с ключом 'id',
           значение которого равно переданному в метод значению"""

        ll = self.to_list()

        for data in ll:
            try:
                if data['id'] == id_item:
                    return data
            except TypeError:
                print("Данные не являются словарем или в словаре нет id.")
