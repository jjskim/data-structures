"""Module to define a stack structure."""

from linked_list import LinkedList


class Stack(object):
    """Define a stack class."""

    def __init__(self, iterable=()):
        """Construct an instance of a stack object."""
        self._linked_list = LinkedList()
        if isinstance(iterable, (str, tuple, list)):
            for thing in iterable:
                self.push(thing)
        elif iterable and not isinstance(iterable, (str, tuple, list)):
            raise TypeError("Passed an invalid iterable value.")

    def push(self, value):
        """Add the passed value to the top of the stack."""
        self._linked_list.push(value)

    def pop(self):
        """Return the top value from the stock."""
        return self._linked_list.pop()

    def __len__(self):
        """Return the length of the stack."""
        return self._linked_list.size()
