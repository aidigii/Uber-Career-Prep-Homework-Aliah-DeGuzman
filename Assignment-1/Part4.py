
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




