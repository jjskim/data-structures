"""Module to define a Doubly Linked List."""

from linked_list import LinkedList
from linked_list import Node


class DoublyLinkedNode(Node):
    """Define a Doubly Linked Node."""

    def __init__(self, prev=None, data=None, next=None):
        """Construct a single Node object."""
        super(DoublyLinkedNode, self).__init__(data, next)
        self.prev = prev


class DoublyLinkedList(LinkedList):
    """Define a Doubly Linked List."""

    def __init__(self, iterable=()):
        """Construct a new Doubly Linked List."""
        super(DoublyLinkedList, self).__init__(iterable)
        self.tail = None

    def push(self, val):
        """Insert the passed value to the head of the list."""
        temp = DoublyLinkedNode(None, val, self.head)
        if self._counter == 0:
            self.head = temp
            self.tail = temp
        else:
            self.head.prev = temp
            self.head = temp
        self._counter += 1

    def append(self, val):
        """Append the passed value to the tail of the list."""
        temp = DoublyLinkedNode(self.tail, val, None)
        if self._counter == 0:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self._counter += 1

    def pop(self):
        """Remove and return the value at the head of the list."""
        val = super(DoublyLinkedList, self).pop()
        if self._counter == 0:
            self.tail = None
        else:
            self.head.prev = None
        return val

    def shift(self):
        """Remove and return the value at the tail of the list."""
        if self.tail is None:
            raise IndexError('The list is empty')
        temp = self.tail.data
        self.tail = self.tail.prev
        if self.tail is not None:
            self.tail.next = None
        self._counter -= 1
        if self._counter == 0:
            self.head = None
        return temp

    def remove(self, val):
        """Remove the first instance of val found in the list."""
        curr = self.head

        for i in range(self._counter):
            if(curr.data == val):
                if(curr.prev is None):
                    self.pop()
                elif(curr.next is None):
                    self.shift()
                else:
                    curr.prev.next = curr.next
                    curr.next.prev = curr.prev
                    self._counter -= 1
                return
            curr = curr.next
        raise ValueError("Passed value is not in list")

    def __len__(self):
        """Return the number of nodes in the list."""
        return self._counter
