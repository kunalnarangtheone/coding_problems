from random import randint

class ListNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None

    def __str__(self):
        return f"{self.value} -> {self.next}"

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self) -> list[int]:
        ptr = self.head
        values = []

        while ptr:
            values.append(ptr.value)
            ptr = ptr.next

        return values

    def __str__(self):
        values = self.traverse()
        return " -> ".join([str(value) for value in values])

    def __len__(self):
        length = 0

        ptr = self.head
        while ptr:
            ptr = ptr.next
            length +=1

        return length

    def add(self, location: int, value: int):
        node = ListNode(value)
        if self.head is None:
            self.head = node

        else:
            if location == 0:
                node.next = self.head
                self.head = node

            elif location == -1:
                ptr = self.head

                while ptr.next:
                    ptr = ptr.next
                ptr.next = node

            else:
                raise ValueError("This location is not supported!")


    def generate(self, n: int = 5):
        """Generates from the end of the list"""
        self.head = None

        # for i in range(n):
        #     # self.add(-1, randint(1, 20))
        self.add(-1, 1)
        self.add(-1, 3)
        self.add(-1, 2)
        self.add(-1, 1)
        self.add(-1, 4)
        self.add(-1, 2)

        return self
