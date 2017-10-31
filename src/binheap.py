"""Module to define a binary heap."""


class BinaryHeap(object):
    """Define a binary heap class."""

    def __init__(self, iterable=None):
        """Construct a binary heap object."""
        self._list = [None]
        if iterable:
            try:
                for value in iterable:
                    self.push(value)
            except TypeError:
                raise TypeError("Passed value must be an iterable")

    def push(self, value):
        """Add the value to the heap, maintaining the binary heap structure."""
        push_index = self._percolate_up(len(self._list), value)
        if push_index == len(self._list):
            self._list.append(value)
        else:
            self._list[push_index] = value

    def pop(self):
        """Remove and return the smallest value of heap, maintaining structure."""
        if len(self._list) == 1:
            raise IndexError("Cannot pop from an empty heap")
        top_heap_value = self._list[1]
        hole = self._percolate_down(1, self._list[len(self._list) - 1])
        self._list[hole] = self._list.pop()
        return top_heap_value

    def _percolate_down(self, hole, value):
        """Restore binary heap structure, starting from top-down."""
        while hole * 2 < len(self._list) - 1:
            left_index = 2 * hole
            right_index = left_index + 1
            target = 0
            if self._list[left_index] < self._list[right_index] or right_index >= len(self._list):
                target = left_index
            else:
                target = right_index
            if self._list[target] < value:
                self._list[hole] = self._list[target]
                hole = target
            else:
                break
        return hole

    def _percolate_up(self, hole, value):
        """
        Restore binary heap structure, starting from bottom-up and
        return the index of where the value should be added.
        """
        while hole > 1 and value < self._list[int(hole / 2)]:
            if hole == len(self._list):
                self._list.append(self._list[int(hole / 2)])
            else:
                self._list[hole] = self._list[int(hole / 2)]
            hole = int(hole / 2)
        return hole
