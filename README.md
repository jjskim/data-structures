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