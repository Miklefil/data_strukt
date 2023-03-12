class Node():
    """Класс узла Node, содержащий два атрибута:
    - data - данные (любые полезные данные: число, строка, список и т.д.)
    - nex_node - ссылка на следующий узел
    метод __init__(self) - иницализация класса. Создаются атрибуты:
    data: данные (любой объект)
    и next_node : указатель на следующий узел
    метод __repr__(self) -> str: возвращает текстовое представление объекта Node
    метод next_node(self) -> Node: возвращает указатель на следующий элемент
    """

    def __init__(self, data, next_node=None) -> None:
        """инициализация пустого узла"""
        self.data = data
        self.next_node = next_node

    def __repr__(self) -> str:
        """представление экземпляра класса Node
        возвращает только данные data
        полное представление закомментировано для последущей реализации
        """
        return str(self.data)


class Queue:
    def __init__(self, top=None, tail=None):
        self.top = top
        self.tail = tail

    def enqueue(self, data):
        new_node = Node(data)
        if self.top is None:
            self.top = new_node
            self.tail = new_node
        else:
            self.tail.next_node = new_node
            self.tail = new_node


    def dequeue(self):
        if self.top is None:
            return
        value = self.top.data
        self.top = self.top.next_node
        return value

    # text = ""
    # for item in self.__dict__:
    #     text += f'Node({str(item)}={self.__dict__[item]}), '
    # text[:-2]
    # return text
