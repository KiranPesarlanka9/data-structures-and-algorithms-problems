class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:

    def __init__(self):
        self.head = None

    def insertAtBegin(self, new_data):

        new_node = Node(new_data)
        new_node.next = self.head

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node

    def append(self, new_data):

        new_node = Node(new_data)
        new_node.next = None

        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return

        last = self.head
        while(last.next is not None):
            last = last.next

        last.next = new_node
        new_node.prev = last

        return
        
            def reverse(self):
        temp = None
        current = self.head

        while current is not None:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev

        if temp is not None:
            self.head = temp.prev

    def searchNode(self, value):
        i = 1
        flag = False
        current = self.head

        if(self.head == None):
            print("List is empty")
            return;

        while(current != None):
            if(current.data == value):
                flag = True
                break
            current = current.next
            i = i + 1

        if(flag):
            print("Node is present in the list at the position : " + str(i))
        else:
            print("Node is not present in the list")

    def remove(self, val):
        if self.head == val:
            self.head = self.head.next
            self.head.prev = None
            return

        tmp = self.head
        while tmp.next is not None:
            if tmp.data == val:
                tmp.next.prev = tmp.prev
                tmp.prev.next = tmp.next
            tmp = tmp.next
        return
            
    def printList(self, node):

        print("Traversal in forward direction")
        while(node is not None):
            print " % d" %(node.data),
            last = node
            node = node.next
        print("\n")

        print("Traversal in reverse direction")
        while(last is not None):
            print " % d" %(last.data),
            last = last.prev
        print("\n")

llist = DoublyLinkedList()
llist.append(6)
llist.insertAtBegin(7)
llist.insertAtBegin(1)
llist.append(4)

print("Created DLL is:")
llist.printList(llist.head)
llist.reverse()
print("list is reversed")
llist.printList(llist.head)
llist.searchNode(4)
