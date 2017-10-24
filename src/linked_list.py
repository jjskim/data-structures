"""Implementation of a linked list in Python."""


class Node(object):
    """Define a Node class."""

    def __init__(self, data=None, next=None):
        """Construct a single Node object."""
        self.data = data
        self.next = next


class LinkedList(object):
    """Define a LinkedList class."""

    def __init__(self, iterable=()):
        """Construct an instance of a LinkedList."""
        self.head = None
        self._counter = 0

        if isinstance(iterable, (str, tuple, list)):
            for item in iterable:
                self.push(item)
        elif iterable and not hasattr(iterable, "__iter__"):
            raise TypeError("Passed value is not iterable")

    def push(self, val):
        """Insert the passed value at the head of the list."""
        self.head = Node(val, self.head)
        self._counter += 1

    def pop(self):
        """Pop the first value off the head of the list and return it."""
        if self.head is None:
            raise IndexError('The list is empty')
        temp = self.head.data
        self.head = self.head.next
        self._counter -= 1
        return temp

    def size(self):
        """Return the length of the list."""
        return self._counter

    def __len__(self):
        """Return size when interacted with __len__ function."""
        return self._counter

    def search(self, val):
        """Return the node containing the passed vaue if present, else None."""
        curr = self.head
        while curr is not None:
            if curr.data == val:
                return curr
            curr = curr.next
        return

    def remove(self, data):
        """Remove the given node from list."""
        if data == self.head.data:
            self.head = self.head.next
            return
        else:
            curr = self.head.next
            for i in range(self._counter - 1):
                if curr is data:
                    return curr
                curr = curr.next
            raise ValueError("Passed node not in list")

    def display(self):
        """Return a unicode string representation of the list."""
        to_string = "("
        curr = self.head
        if curr is not None:
            to_string += str(curr.data)
            curr = curr.next
        while curr is not None:
            to_string += (", " + str(curr.data))
            curr = curr.next
        to_string += ")"
        return to_string

    def __str__(self):
        """Return a string representation of the list."""
        return self.display()
