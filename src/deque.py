"""Module to define a dequeue."""

from double_linked_list import DoublyLinkedList


class Deque(object):
    """Define a deque class."""

    def __init__(self, iterable=()):
        """Construct an instance of a deque."""
        if iterable and not hasattr(iterable, "__iter__"):
            raise TypeError("Passed argument is not an iterable value.")
        self._dll = DoublyLinkedList(iterable)

    def append(self, val):
        """Append the value to the end of the deque."""
        self._dll.append(val)

    def appendleft(self, val):
        """Add the value to the front of the deque."""
        self._dll.push(val)

    def pop(self):
        """Remove and return the value at the end of the deque."""
        if self._dll.tail is None:
            raise IndexError("Can't pop from an empty deque")
        return self._dll.shift()

    def popleft(self):
        """Remove and return the value at the front of the deque."""
        if self._dll.head is None:
            raise IndexError("Can't popleft from an empty deque")
        return self._dll.pop()

    def peek(self):
        """Return the value of the end of the deque."""
        if self._dll.tail is not None:
            return self._dll.tail.data
        else:
            return None

    def peekleft(self):
        """Return the value at the front of the deque."""
        if self._dll.head is not None:
            return self._dll.head.data
        else:
            return None

    def size(self):
        """Return the number of items in the deque."""
        return self._dll.size()
