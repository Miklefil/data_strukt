from utils.stack import Stack
from utils.node import Node, Queue

queue = Queue()
queue.enqueue('data1')
queue.enqueue('data2')
queue.enqueue('data3')

print(queue.top.data)
print(queue.top.next_node.data)
print(queue.tail.data)
print(queue.tail.next_node)
print(queue.tail.next_node.data)



#stack = Stack()
#stack.push('data1')
#data = stack.pop()

# стэк стал пустой
#print(stack.top)


# pop() удаляет элемент и возвращает данные удаленного элемента
#print(data)



#stack = Stack()
#stack.push('data1')
#stack.push('data2')
#data = stack.pop()

# теперь последний элемента содержит данные data1
#print(stack.top.data)


# данные удаленного элемента
#print(data)

