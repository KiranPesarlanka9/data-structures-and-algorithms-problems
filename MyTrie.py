class Node:

    def __init__(self, char):
        self.char = char
        self.child = []
        self.has_next = False
        self.end_of_word = False

    def __str__(self):
        return self.char

def insert(node, string):
    for char in string:
        already_there = False
        for c in node.child:
            if char==c.char:
                already_there = True
                node = c
                break

        if not already_there:
            new_node = Node(char)
            node.child.append(new_node)
            node.has_next = True
            node = new_node
    node.end_of_word = True

root = Node('*')
insert(root, 'kiran')
insert(root, 'pesarlanka')
insert(root, 'karate')
insert(root, 'kir')
insert(root, 'kite')
insert(root, 'kebarbiq')
insert(root, 'car')

def get_remaining_chars(node, l=[]):
    for child in node.child:
        l.append(child.char)
        if not child.has_next:
            l.append('-')
        if child.has_next:
            l = get_remaining_chars(child)
    return l

def suggestions(node, prefix_string):
    for string in prefix_string:
        for child in node.child:
            if string==child.char:
                node = child
    end_strings = ''.join(get_remaining_chars(node))
    for end_string in filter(None, end_strings.split('-')):
        print "ki"+end_string

suggestions(root, 'ki')


"""
def display_trie(node):
    for child in node.child:
        print child.char
        if child.has_next:
            display_trie(child)

display_trie(root)
"""
