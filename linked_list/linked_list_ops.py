from listnode import ListNode

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def traverse(self):
        if self.head is None:
            print("The list is empty!")

        ptr = self.head
        while ptr is not None:
            print(ptr.val)
            ptr = ptr.next

    def insert(self, val, location):
        """Inserts a certain element at a certain location in the linked list"""
        node = ListNode(val)
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            if location == 0:
                node.next = self.head
                self.head = node

            # Correct this
            elif location == -1:
                node.next = None
                self.tail.next = node
                self.tail = node

            else:
                p = 1
                tmp = self.head

                while(tmp):
                    p += 1

                    if p == location:
                        node.next = tmp.next
                        tmp.next = node
                        break

                    tmp = tmp.next

    def search(self, ele):
        """Searches for a given node inside a linked list"""
        index = None

        if self.head is None:
            return index

        else:
            ptr = ll.head
            p = 0

            while ptr is not None:
                if ptr.val == ele:
                    index = p
                    break

                p += 1
                ptr = ptr.next

        return index

    def delete(self, index):
        """Deletes a node from a cetain index in the linked list"""

        if self.head is None:
            print("Cannot delete from an empty list!")

        else:
            if self.head == self.tail:
                self.head = None
                self.tail = None

            if index == 0:
                tmp = self.head.next
                self.head = self.head.next

            elif index == -1:
                ptr = self.head

                while ptr is not None:
                    if ptr.next == self.tail:
                        break
                    ptr = ptr.next

                ptr.next = None
                self.tail = ptr

            else:
                p = 0
                ptr = self.head

                while p < index:
                    if p == index - 1:
                        break

                    p += 1
                    ptr = ptr.next

                ptr.next = ptr.next.next




ll = LinkedList()
ll.insert(4, 0)
ll.insert(3, 0)
ll.insert(2, 0)
ll.insert(1, 0)
print(ll.head.val)
print(ll.tail.val)

# ll.traverse()
