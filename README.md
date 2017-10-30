# data-structures

This repository will hold a sample of classic data structures implemented in Python

# Stacks

A stack creates a LIFO (Last-in, first-out) object that can push and pop one value at a time.

- Push: O(1)
    - Appends the passed value to the top of the stack

- Pop: O(1)
    - Removes and returns the value at the top of the stack

- \__len\__: O(1)
    - Returns the number of items stored in the stack

# Linked-Lists

An ordered set of data elements, each containing a link to its successor

- Push: O(1)
    - Insert the passed value at the "head" of the list

- Pop: O(1)
    - Remove and return the value at the head of the list

- Size: O(1)
    - Return the number of items contained in the list

- Search: O(n)
    - Return the first node containing the passed value, else None

- Remove: O(n)
    - Remove the first node containing the passed value, else raises an Exception

- Display: O(n)
    - Returns a unicode string representing the list as if it were a tuple

- \__len\__: O(1)
    - Returns the number of items contained in the list

- \__str\__: O(n)
    - Returns a unicode string representing the list as if it were a tuple

# Doubly-Linked-Lists

An ordered set of data elements, each containing a link to its successor and its predecessor

- Push: O(1)
    - Insert the passed value at the "head" of the list

- Pop: O(1)
    - Remove and return the value at the head of the list

- Append: O(1)
    - Insert the passe vaue at the "tail" of the list

- Shift: O(1)
    - Remove and return the value at the tail of the list.

- Remove: O(n)
    - Remove the first node containing the passed value, else raises an Exception

- \__len\__: O(1)
    - Returns the number of items contained in the list

# Queues

An ordered set of elements that follows a FIFO (first in first out) structure

- Enqueue: O(1)
    - Insert the passed value at the "back" of the queue

- Enqueue: O(1)
    - Remove and return the value at the "front" of the queue

- Peek: O(1)
    - Returns the value at the "front" of the queue, but does not remove it. If queue is empty, returns None

- Size: O(1)
    - Returns the number of elements in the queue.

# Deque

An ordered set of data elements that functions as a queue in both directions. Items can be added and removed at both ends, and their order is preserved

- append: O(1)
    - Insert the passed value at the end of the deque

- appendleft: O(1)
    - Insert the passed value at the front of the deque

- pop: O(1)
    - Remove and return the value at the end of the deque

- popleft: O(1)
    - Remove and return the value at the front of the deque

- peek: O(1)
    - Returns the value at the end of the deque, but does not remove it. If deque is empty, returns None

- peekleft: O(1)
    - Returns the value at the front of the deque, but does not remove it. If deque is empty, returns None

- size: O(1)
    - Returns the number of elements in the deque.