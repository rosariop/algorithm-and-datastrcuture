class Element:
    def __init__(self, id):
        self.id = id

    successor = None


def iterate(head, index):
    element = head.successor
    if element.id != index:
        element = iterate(element, index)
    else:
        return element
    return element


def get_last(head):
    if head.successor is None:
        return head
    else:
        return get_last(head.successor)


def add(head, element):
    last = get_last(head)
    last.successor = element


def remove(head, index):
    if head.id is index:
        return

    prev = iterate(head, index-1)
    if prev is not None:
        next = iterate(head, index).successor
        prev.successor = next


e3 = Element(3)

e2 = Element(2)
e2.successor = e3

e1 = Element(1)
e1.successor = e2

e4 = Element(4)
e5 = Element(5)

add(e1, e4)
add(e1, e5)

remove(e1, e1.id)
