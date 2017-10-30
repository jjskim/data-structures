"""."""

from double_linked_list import DoublyLinkedList


class Deque(object):
    """."""

    def __init__(self, iterable=()):
        """."""
        if iterable and not hasattr(iterable, "__iter__"):
            raise TypeError("Passed argument is not an iterable value.")
        self._dll = DoublyLinkedList(iterable)


    def append(self, val):
        """."""
        self._dll.append(val)


    def appendleft(self, val):
        """."""
        self._dll.push(val)


    def pop(self, val):
        """."""
        if self._dll.head is None:
            raise IndexError("Can't pop from an empty deque")
        self._dll.shift()


    def popleft(self, val):
        if self._dll.tail is None:
            raise IndexError("Can't popleft from an empty deque")
        self._dll.pop()


    def peek(self):
        """."""
        if self._dll.tail is not None:
            return self._dll.tail.data
        else:
            return None


    def peekleft(self):
        """."""
        if self._dll.head is not None:
            return self._dll.head.data
        else:
            return None


    def size(self):
        """."""
        return self._dll.size()
