"""."""
from linked_list import LinkedList
from linked_list import Node


class DoublyLinkedNode(Node):
    """."""

    def __init__(self, prev=None, data=None, next=None):
        """Construct a single Node object."""
        self.prev = prev
        super(DoublyLinkedNode, self).__init__(data, next)


class DoublyLinkedList(LinkedList):
    """."""

    def __init__(self, iterable=()):
        """."""
        self.tail = None
        super(DoublyLinkedList, self).__init__(iterable)


    def push(self, val):
        """."""

        temp = DoublyLinkedNode(None, val, self.head)
        self.head.prev = temp
        self.head = temp
        if self._counter == 0:
            self.tail = self.head
        self._counter += 1


    def append(self, val):
        """."""

        temp = DoublyLinkedNode(self.tail, val, None)
        self.tail.next = temp
        self.tail = temp
        if self._counter == 0:
            self.head = self.tail
        self._counter += 1


    def pop(self):
        """."""

        val = super.pop()
        self.head.prev = None
        if self._counter == 0:
            self.tail = None
        return val


    def shift(self):
        """."""
        if self.tail is None:
            raise IndexError('The list is empty')
        temp = self.tail.data
        self.tail = self.tail.prev
        self._counter -= 1
        if self._counter == 0:
            self.head = None
        return temp


    def remove(self, val):
        """."""

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


