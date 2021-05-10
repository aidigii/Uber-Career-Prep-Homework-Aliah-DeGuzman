"""
void push(<Node> node) → Adds the node to the end of the list
<Node> pop() → Removes the last node at the end of the linked list, returns that data
void insert(uint index,<Node> node) → Adds a single node containing data to a chosen location in the list. If the index is above the size of the list, do nothing
void remove(uint index) → remove/delete a single node at the index location in the list. If the node doesn’t exist at the index, do nothing
<Node> elementAt(uint index) → Returns a pointer to the node at the index location in the list. If the node doesn’t exist at the index, return nil/null
uint size() → Returns the length of the list.
void printList() → Returns a string representation of the linked list

Implement a function to check if a linked list is a palindrome.

REVERSE LINKED LIST IN 3 WAYS:
1. ITERATIVELY
2. USING A STACK
3. RECURSIVELY
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def push(self, node):
        temp = self.tail.prev
        if temp:
            temp.next = node
            node.prev = temp
            node.next = self.tail
            self.tail.prev = node


    def pop(self):
        temp = self.tail.prev
        if temp and temp != self.head:
            prev = temp.prev
            prev.next = self.tail
            self.tail.prev = prev
        else:
            return Node("empty")
        return temp

    def insert(self, index,node):
        temp = self.head
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                return
        if temp.next:
            save = temp.next
            temp.next = node
            node.prev = temp
            node.next = save
            save.prev = node


    def remove(self, index):
        temp = self.head
        if index < 0:
            return
        for i in range(index):
            if temp:
                temp = temp.next
            else:
                return
        if temp:
            temp = temp.next
            if temp and temp.next and temp.prev:
                next = temp.next
                prev = temp.prev
                prev.next = next
                next.prev = prev

    def elementAt(self, index):
        temp = self.head
        index += 1
        for i in range(index):
            temp = temp.next
        if temp != self.head and temp != self.tail:
            return temp
        return Node("Empty")

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        count -= 2
        if count <= 0:
            return 0
        else:
            return count

    def printList(self):
        temp = self.head
        if not temp:
            print("Empty list")
        while temp:
            if temp != self.head and temp != self.tail:
                print(temp.val)
            temp = temp.next

    # iterative version of reversing a linked list
    def reverseLinkedList(self):

        if not self.head.next:
            return

        temp = self.head.next
        node = None

        while temp:
            save = temp.next
            temp.next = node
            node = temp
            temp = save

        self.head.next = node

list = LinkedList()
list.push(Node(1))
list.push(Node(2))
list.insert(3,Node(3))
list.push(Node(4))
list.push(Node(5))
list.printList()
print("--------")
list.remove(6)
list.printList()
print("aaaaaaaa")
print(list.elementAt(-1).val)
list.reverseLinkedList()
list.printList()

