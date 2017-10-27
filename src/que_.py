"""Module to define a Queue."""

from double_linked_list import DoublyLinkedList


class Queue(object):
    """Define a Queue."""

    def __init__(self, iterable=()):
        """Construct a Queue, optionally adding values from iterable."""
        if iterable and not hasattr(iterable, "__iter__"):
            raise TypeError("Passed argument is not iterable")
        self._dll = DoublyLinkedList(iterable)

    def enqueue(self, val):
        """Add a value to the end of the queue."""
        self._dll.append(val)

    def dequeue(self):
        """Remove the value at the front of the queue."""
        if self._dll.head is None:
            raise IndexError("Cannot dequeue from an empty queue")
        return self._dll.pop()

    def peek(self):
        """Return the value of the front of the queue."""
        if self._dll.head is not None:
            return self._dll.head.data
        else:
            return None

    def size(self):
        """Return the number of items in the queue."""
        return self._dll.size()
