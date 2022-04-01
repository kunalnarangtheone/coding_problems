from linked_list import LinkedList

ll = LinkedList()
ll.generate(5)

def remove_dups(ll):
    if ll.head is None:
        return
        
    uniques = set()

    pt = ptr = ll.head

    while ptr.next:
        if ptr.next.value in uniques:
            ptr.next = ptr.next.next
            ptr.next.next = None
            continue
        uniques.add(ptr.value)
        ptr = ptr.next

    return pt

print(remove_dups(ll))
