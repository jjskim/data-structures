"""."""
import linked_list

class DoublyLinkedNode(Node):
    """."""

    def __init__(self, prev=None, data=None, next=None):
        """Construct a single Node object."""
        self.prev = prev
        super(DoublyLinkedNode, self).__init__(data, next)



class DoublyLinkedList(LinkedList):
    """."""


    def push(self, val):
        """."""

        self.head = DoublyLinkedNode(None, val, self.head)
        self._counter += 1


    def append(self, val):
        """."""

        self.tail = DoublyLinkedNode(self.tail, val, None)
        self._counter += 1


    def pop(self):
        """."""

        val = super.pop()
        self.head.prev = None
        return val
