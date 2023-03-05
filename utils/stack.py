from utils.node import Node


class Stack():
    """
    класс Stack реализует структуру данных, представляющую стэк - упорядоченный
    набор элементов, в которой добавление новых элементов и удаление
    существующих производится с одного конца, называемого вершиной стека.
    Первым из стека удаляется элемент, который был помещен туда последним,
    то есть в стеке реализуется стратегия «последним вошел — первым вышел»
    (last-in, first-out — LIFO).
    метод __init__(self) - иницализация класса. Создаются атрибуты
    elements-> list: для хранения объектов класса Node
     и top ->: Node указатель на последний элемент стэка
    метод push(self, data) -> Node - добавляет в стэк элемент в виде узла
    и возвращает объект Node, содержащий data
    метод pop(self) -> Node - удаляет последний элемент из в стэка
    и возвращает его данные
    метод data(self) -> object - возвращает объект data, хранящийся в узле Node
    """

    def __init__(self, top=None):
            self.top = top

    def push(self, data):
            """Добавляет данные в стек"""
            new_node = Node(data)
            new_node.next_node = self.top
            self.top = new_node

    def pop(self):
            remove = self.top
            self.top = self.top.next_node
            return remove.data