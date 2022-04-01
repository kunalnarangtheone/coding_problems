from listnode import ListNode

class CircularLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        ptr = self.head
        while ptr is not None:
            print(ptr.val)
            if ptr.next == self.tail:
                break
            ptr = ptr.next

    def create(self, value):
        node = ListNode(value)
        if self.head is None:
            node.next = node
            self.head = node
            self.tail = node

    def insert(self, location, value):
        node = ListNode(value)

        if self.head is None:
            return node

        else:
            if location == 0:



cll = CircularLinkedList()
cll.create(1)
cll.traverse()
