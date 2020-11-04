"""
Your goal is to define a `Queue` class that uses two stacks. Your `Queue` class
should have an `enqueue()` method and a `dequeue()` method that ensures a
"first in first out" (FIFO) order.

As you write your methods, you should optimize for time on the `enqueue()` and
`dequeue()` method calls.

The Stack class that you will use has been provided to you.
"""
class Stack:
    def __init__(self):
        self.data = []
    
    def __len__(self):
        return len(self.data)
    def push(self, item):
        self.data.append(item)

    def pop(self):
        if len(self.data) > 0:
            return self.data.pop()
        return "The stack is empty"

class QueueTwoStacks:
    def __init__(self):
        # hold the elements from 'in' in reverse order
        self.out_stack = Stack()
        # holds incoming elements
        self.in_stack = Stack()

    def enqueue(self, item):
        self.in_stack.push(item)

    def dequeue(self):
        if len(self.out_stack) == 0:
            while len(self.in_stack) != 0:
                self.out_stack.push(self.in_stack.pop())
        return self.out_stack.pop()
        

#This is terrible
class QueueTwoStacks_Slow:
    def __init__(self):
        # Your code here
       self.data = []
        
    def enqueue(self, item):
        # Your code here
        self.data.append(item)

    def dequeue(self):
        # Your code here
        if len(self.data) > 0:
            return self.data.pop(0)
        return "The queue is empty"

from collections import deque

class Queue_with_deque:
    def __init__(self):
        self.data = deque()
        
    def enqueue(self, item):
        self.data.append(item)
    def dequeue(self):
        if len(self.data) > 0:
            return self.data.popleft()
        return "the queue is empty"

q = QueueTwoStacks()

for i in range(26):
    q.enqueue(chr(i+96))

for i in range(27):
    print(q.dequeue())
