import unittest
from utils.node import Node
from utils.stack import Stack


class Test_Stack(unittest.TestCase):
    def SetUp(self):
        self.stack = Stack()
        self.node = Node(10)

    def test_stack__init__(self):
        self.node_10 = Node(10)
        self.assertEqual(Node(10).data, self.node_10.data)

    def test_push(self):
        self.stack = Stack()
        self.node_10 = Node(10)
        self.node_20 = Node(20)
        self.stack.push(self.node_10)
        self.stack.push(self.node_20)

    def test_pop(self):
        self.stack = Stack()
        self.node_10 = Node(10)
        self.node_20 = Node(20)
        self.node_30 = Node(30)
        self.stack.push(self.node_10)
        self.stack.push(self.node_20)
        self.stack.push(self.node_30)
        self.assertEqual(len(self.stack.top), 3)
        self.stack.pop()
        self.assertEqual(len(self.stack.top), 2)
        self.stack.pop()
        self.assertEqual(len(self.stack.top), 1)
        self.assertEqual(self.stack.pop().data, self.node_10.data)
        self.assertEqual(len(self.stack.top), 0)
        self.assertIsNone(self.stack.pop())

    def test_data(self):
        self.node_10 = Node(10)
        self.stack = Stack()
        self.stack.push(self.node_10)
        self.assertEqual(str(self.stack.top.data), "10")

    def test_pop(self):
        stack = Stack()
        self.assertEqual(stack.pop(), None)
        stack.push('data1')
        stack.push('data2')
        self.assertEqual(stack.pop(), 'data2')
