from linked_list import LinkedList

def kth_to_last(ll, k):
    """Finds the kth element from the end of the array"""

    assert k == int(k), "Position should be integer only!"
    assert k < len(ll), "Position should not be bigger than length of linked list!"

    ptr = ll.head
    if ptr is None:
        return None

    else:
        length = len(ll)
        p = 0

        while p <= length - k - 1:
            if p == length - k - 1:
                break

            p += 1
            ptr = ptr.next

        return ptr.next.value if k != 0 else ptr.value

def kth_to_last_v2(ll, k):
    """Finds the kth element from the end of the array"""

    assert k == int(k), "Position should be integer only!"
    assert k < len(ll), "Position should not be bigger than length of linked list!"

    ptr1 = ll.head
    ptr2 = ll.head
    p = 0

    if ptr1 is None:
        return None

    while p < k:
        ptr2 = ptr2.next
        p += 1

    while ptr2.next:
        ptr1 = ptr1.next
        ptr2 = ptr2.next

    return ptr1.next.value if k != 0 else ptr1.value






ll = LinkedList()
ll.generate()
print(ll)
print(kth_to_last_v2(ll, 0))
