class MyStack:
    def __init__(self):
        self.arr = []
        self.top = -1

    def insert(self, element):
        self.top += 1
        self.arr.append(element)

    def pop(self):
        if self.top < 0: return None
        element = self.arr.pop(self.top)
        self.top -= 1
        return element
    
    def top_position(self):
        return self.top

"""
>>> from MyStack import MyStack
>>> stack = MyStack()
>>>
>>> stack.insert(6)
>>> stack.insert(2)
>>> stack.insert(1)
>>> stack.insert(7)
>>> stack.insert(3)
>>>
>>> stack.pop()
3
>>> stack.pop()
7
>>> stack.pop()
1
>>> stack.pop()
2
"""
