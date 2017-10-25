# data-structures

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