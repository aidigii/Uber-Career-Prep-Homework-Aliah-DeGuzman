"""
STACK
push() → Pushes an integer on top of the stack
pop() → Removes what is on the top of the stack, and returns that value to the caller
top() → Looks at the top value, and returns it. Does not manipulate the stack
isEmpty() → Returns True or False if the stack is Empty or not, respectively
size() → Returns an integer value with the count of elements in the stack

new method to your Stack class called min(), which returns the minimum element of
the stack in O(1) time, as opposed to O(n) time.

Allow your stack to handle any type of object as input type, not just integers

enqueue() → adds an item to the queue
dequeue() → removes an item from the queue
rear() → returns the item at the end of the queue
front() → returns the item at the front of the queue
size() → returns the size of the queue
isEmpty() → returns whether or not the queue is empty

Allow your queue to handle any type of object as input type, not just integers.
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.prev = None

class Stack:

    def __init__(self):
        self.head = Node(0) # dummy node

    def push(self, val):
        temp = self.head.next
        self.head.next = Node(val)
        self.head.next.next = temp

    def pop(self):
        temp = self.head.next
        if temp:
            self.head.next = temp.next
            temp.next = None
        return temp

    def top(self):
        temp = self.head.next
        if temp:
            newNode = Node(temp.val)
            return newNode
        return temp # returns null if stack is empty

    def isEmpty(self):
        temp = self.head.next
        if temp:
            return False
        return True

    def size(self):
        count = 0
        temp = self.head
        while temp:
            count += 1
            temp = temp.next
        return count

    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next



class Queue:
    def __init__(self):
        self.head = Node(0)
        self.tail = Node(0)
        self.head.next = self.tail
        self.tail.prev  = self.head

    def enqueue(self, val):
        temp = Node(val)
        save = self.head.next
        self.head.next = temp
        temp.prev = self.head
        temp.next = save
        save.prev = temp

    def dequeue(self):
        temp = self.tail.prev
        if temp:
            temp.prev.next = self.tail
            self.tail.prev = temp.prev


    def rear(self):
        if self.head.next and self.head.next != self.tail:
            temp = Node(self.head.next.val)
            return temp
        return Node("empty")

    def front(self):
        if self.tail.prev and self.tail.prev != self.head:
            temp = Node(self.tail.prev.val)
            return temp
        return Node("empty")

    def size(self):
        temp = self.head
        count = 0
        while temp.next:
            temp = temp.next
            count += 1
        return count


    def isEmpty(self):
        if self.head.next == self.tail:
            return True
        return False
    def print(self):
        temp = self.head
        while temp:
            print(temp.val)
            temp = temp.next


