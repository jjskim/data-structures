"""."""

from linked_list import LinkedList


class Stack(object):
    """."""

    def __init__(self, iterable=()):
        """."""
        self._linked_list = LinkedList()
        if isinstance(iterable, (str, tuple, list)):
            for thing in iterable:
                self.push(thing)
        elif iterable and not isinstance(iterable, (str, tuple, list)):
            raise TypeError("Passed an invalid iterable value.")

    def push(self, value):
        """."""
        self._linked_list.push(value)

    def pop(self):
        """."""
        return self._linked_list.pop()

    def __len__(self):
        """."""
        return self._linked_list.size()
