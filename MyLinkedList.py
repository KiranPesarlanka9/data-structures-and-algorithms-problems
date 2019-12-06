class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def set_next(self, node):
        self.next_node = node

    def get_next(self):
        return self.next_node


class LinkedList:
    def __init__(self, head=None):
        self.head = head
        self.current = head
        self.counter = 0

    def search(self, data):
        if self.head.data==data: return True
        node = self.head
        while node.next_node:
            node = node.next_node
            if node.data == data:
                return True
        return False

    def insert(self, data):
        new_node = Node(data)
        if not self.current:
            self.head = new_node
            self.current = new_node
        else:
            self.current.next_node = new_node
            self.current = new_node
            self.counter += 1

    def size(self):
        return self.counter


    def insert_after(self, data, after_data):
        # experimental approach
        node = self.head
        found = False

        for i in xrange(self.counter):
            if node.data==after_data:
                found = True
                break
            node = node.next_node

        if not found:
            return "No such node--{0}".format(after_data)

        new_node = Node(data)
        temp = node.next_node
        node.next_node = new_node
        new_node.next_node = temp
        return "Inserted"



"""
>>> from MyLinkedList import LinkedList
>>>
>>> ll = LinkedList()
>>>
>>> ll.insert(1)
>>> ll.insert(4)
>>> ll.insert(3)
>>> ll.insert(6)
>>>
>>> ll.insert_after(9, 2)
'No such node--2'
>>>
>>> ll.insert_after(9, 1)
'Inserted'
>>>
>>> ll.search(9)
True
>>> ll.search(8)
False
>>>
>>>

"""
