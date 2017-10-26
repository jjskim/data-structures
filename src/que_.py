"""."""

from double_linked_list import DoublyLinkedList


class Queue(object):
    """."""

    def __init__(self, iterable=()):
        """."""
        self._dll = DoublyLinkedList(iterable)

    def enqueue(self, val):
        """."""
        self._dll.push(val)

    def dequeue(self):
        """."""
        return self._dll.shift()

    def peek(self):
        """."""
        if(self.size is not 0):
            return self._dll.tail.data

    def size(self):
        """."""
        return self._dll.__len__()
