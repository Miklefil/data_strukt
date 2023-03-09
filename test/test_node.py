import unittest
#import pytest
from utils.node import Node, Queue


class Test_Node(unittest.TestCase):

    def SetUp(self):
        self.node = Node()
        self.node_10 = Node(10)

    def test_node__init__(self):
        self.node_10 = Node(10)
        self.assertIs(self.node_10.data, Node(10).data)

    def test__repr__(self):
        self.assertEqual(Node(10).data, 10)

    def test_next_node(self):
        self.node_10 = Node(10)
        self.node_20 = Node(20, self.node_10)
        self.assertEqual(self.node_20.next_node, self.node_10)


class TestQueue(unittest.TestCase):

    def test_enqueue(self):
        queue = Queue()
        queue.enqueue('data1')
        queue.enqueue('data2')
        queue.enqueue('data3')
        self.assertEqual(queue.top.data, 'data1')
        self.assertEqual(queue.top.next_node.data, 'data2')
        self.assertEqual(queue.tail.data, 'data3')
        self.assertEqual(queue.tail.next_node, None)
        with self.assertRaises(AttributeError):
            queue.tail.next_node.data()