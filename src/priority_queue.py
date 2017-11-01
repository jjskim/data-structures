"""Module to define a priority queue."""


class PriorityQueue(object):
    """Define the PriorityQueue class."""

    def __init__(self, iterable=None):
        """Construct an instance of priority queue."""
        self._queues = {}

    def insert(self, value, priority=0):
        """Insert the value in to the priority queue."""
        if priority in self._queues:
            self._queues[priority].insert(0, value)
        else:
            self._queues[priority] = [value]

    def pop(self):
        """Remove and return the value with the highest priority."""
        for priority_level in sorted(self._queues, reverse=True):
            if len(self._queues[priority_level]) > 0:
                return self._queues[priority_level].pop()
        raise IndexError("Cannot pop from an empty priority queue")

    def peek(self):
        """Return the value with the highest priority, without removing it."""
        for priority_level in sorted(self._queues, reverse=True):
            if len(self._queues[priority_level]) > 0:
                return self._queues[priority_level][-1]
        raise IndexError("Cannot peek at an empty priority queue")
