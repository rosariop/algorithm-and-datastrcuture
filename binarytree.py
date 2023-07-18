class Element:
    def __init__(self, content):
        self.content = content

    parent = None
    left = None
    right = None


# <= links > right
def add(root, element):
    if element.content > root.content:
        if root.right is None:
            element.parent = root
            root.right = element
        else:
            add(root.right, element)
    elif element.content < root.content:
        if root.left is None:
            element.parent = root
            root.left = element
        else:
            add(root.left, element)
    else:
        print('element already in the tree')


def find(root, content):
    if root.content == content:
        return root

    if content > root.content:
        return find(root.right, content)
    if content < root.content:
        return find(root.left, content)


def delete(root, content):
    elementToDelete = find(root, content)
    parent = elementToDelete.parent
    if elementToDelete.left is None:
        if parent.content > elementToDelete.content:
            parent.left = elementToDelete.right
        if parent.content < elementToDelete.content:
            parent.right = elementToDelete.right
    elif elementToDelete.right is None:
        if parent.content > elementToDelete.content:
            parent.left = elementToDelete.left
        if parent.content < elementToDelete.content:
            parent.right = elementToDelete.left
    elif elementToDelete.right is not None and (elementToDelete.left is not None):
        indices = index_tree(elementToDelete.right)
        successorIndex = get_next_index(indices, elementToDelete.content)
        successor = find(elementToDelete.right, successorIndex)
        if successor.left is None and elementToDelete == successor.parent:
            successor.parent = elementToDelete.parent
            successor.left = elementToDelete.left
        else:
            successorParent = successor.parent
            successorParent.left = successor.right
            successor.right.parent = successorParent

            successor.parent = elementToDelete.parent
            successor.left = elementToDelete.left
            successor.right = elementToDelete.right
            return successor


def get_next_index(indices, content):
    indices.sort()
    next_biggest_number = indices[-1]

    for index in indices:
        if content < index < next_biggest_number:
            next_biggest_number = index

    return next_biggest_number


def index_tree(root):
    sublist = []
    if root.right is not None:
        sublist.extend(index_tree(root.right))
    if root.left is not None:
        sublist.extend(index_tree(root.left))

    sublist.append(root.content)
    return sublist


rootElement = Element(10)
add(rootElement, Element(5))
add(rootElement, Element(15))
add(rootElement, Element(3))
add(rootElement, Element(7))
add(rootElement, Element(13))
add(rootElement, Element(16))
add(rootElement, Element(2))
add(rootElement, Element(4))
add(rootElement, Element(6))
add(rootElement, Element(8))
add(rootElement, Element(11))
add(rootElement, Element(12))
add(rootElement, Element(14))
add(rootElement, Element(17))

newRoot = delete(rootElement, 10)
print(newRoot.right.content)
