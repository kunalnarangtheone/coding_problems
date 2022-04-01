from listnode import ListNode

class Queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if not self.head:
            return

        else:
            ptr = self.head
            while ptr:
                print(ptr.val)
                ptr = ptr.next

    def enqueue(self, val):
        node = ListNode(val)
        if not self.head:
            self.head = node
            self.tail = self.head

        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        if not self.head:
            return

        else:
            self.head = self.head.next

q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.traverse()

q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
q.dequeue()
q.traverse()
