class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class CircularQueue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, val):
        node = Node(val)
        if not self.head:
            self.head = node
            self.tail = node

        else:
            self.tail.next = node
            node.next = self.head
            self.tail = node

    def dequeue(self):
        if not self.head:
            return

        else:
            value = self.head.val
            temp = self.head.next
            self.head.next = None
            self.tail.next = temp
            self.head = temp
            return value

cir = CircularQueue()
cir.enqueue(1)
cir.enqueue(2)
cir.enqueue(3)

print(cir.dequeue())
print(cir.dequeue())
print(cir.dequeue())
