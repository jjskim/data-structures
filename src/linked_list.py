"""Implementation of a linked list in Python."""


class Node():
    """Define a Node class."""

    def __init__(self, value=None, next=None):
        """Construct a single Node object."""
        self.value = value
        self.next = next


class LinkedList():
    """Define a LinkedList class."""

    def __init__(self):
        """Construct an instance of a LinkedList."""
        self.size = 0
        self.head = None

    def push(self, val):
        """Insert the passed value at the head of the list."""
        new_node = Node(val, self.head)
        self.head = new_node
        self.size += 1

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.size > 0:
            temp = self.head.value
            self.head = self.head.next
            self.size -= 1
            return temp
        else:
            raise IndexError("List is empty")

    def size(self):
        """Return the length of the list."""
        return self.size

    def search(self, val):
        """Return the node containing the passed vaue if present, else None."""
        current_node = self.head
        for i in range(self.size):
            if current_node.value == val:
                return current_node
            current_node = current_node.next
        return None

    def remove(self, node):
        """Remove the given node from list."""
        if node is self.head:
            self.head = self.head.next
            return
        else:
            current_node = self.head.next
            for i in range(self.size - 1):
                if current_node is node:
                    return current_node
                current_node = current_node.next

    def display(self):
        """Return a unicode string representation of the list."""
