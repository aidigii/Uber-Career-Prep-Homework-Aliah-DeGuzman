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