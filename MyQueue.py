class MyQueue:

    def __init__(self):
        self.arr = []

    def enqueue(self, element):
        self.arr.append(element)

    def dequeue(self):
        if not self.arr: return None
        element = self.arr.pop(0)
        return element

"""
>>> from MyQueue import MyQueue
>>> queue = MyQueue()
>>>
>>>
>>> queue.enqueue(4)
>>> queue.enqueue(4)
>>> queue.enqueue(2)
>>> queue.enqueue(7)
>>>
>>> queue.dequeue()
4
>>> queue.dequeue()
4
>>> queue.dequeue()
2
>>> queue.dequeue()
7
"""
