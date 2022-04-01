from listnode import ListNode

class Stack:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return False if self.head else True

    def traverse(self):
        if self.is_empty():
            return

        else:
            ptr = self.head
            while ptr:
                print(ptr.val)
                ptr = ptr.next

    def push(self, val):
        node = ListNode(val)
        if self.is_empty():
            self.head = node

        else:
            node.next = self.head
            self.head = node


    def pop(self):
        if self.is_empty():
            return

        else:
            self.head = self.head.next

s = Stack()
s.push(1)
s.push(3)
s.push(2)
s.traverse()

s.pop()
s.traverse()
