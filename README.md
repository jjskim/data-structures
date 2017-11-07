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

# Binary Heap

An ordered tree like structure in which a parent value is always smaller than the child values.

- push: O(log(n))
    - Insert the value at the end of the heap, then resort to maintain the binary heap structure.

- pop: O(log(n))
    - Remove and return the smallest value (the root of the heap) and then resort the remaining the values to maintain the binary heap structure.

# Priority Queue

An ordered queue where values are sorted based on their passed priority value (higher value = higher priority).
- insert: O(1)
    - Insert the passed value at its priority level, if given, else inserts it at the lowest priority.

- pop: O(n log(n))
    - Remove and return the highest priority value. If more than one value at the highest priority exists, then pop the most senior item at the priority level.

- peek: O(n log(n))
    - Return, but not remove, the highest priority value. If more than one value at the highest priority exists, then pop the most senior item at the priority level.

# Graph (Unweighted, directed)

An collection of values with reference to their connections with each other. Connections between value are directed and are defined explicitly from starting point to ending point.

- nodes: O(n)
    - Return a list of all nodes contained in the graph

- edges: O(n^2)
    - Reeturn a list of all edges in the graph

- add_node: O(1)
    - Adds a new node to the graph if not present

- add_edge: O(1)
    - Add a new directed edge from node 1 to node 2

- del_node: O(n)
    - Deletes the node containing val from the graph, raises an error if no such node exists

- del_edge: O(1)
    - Deletes the directed edge from node 1 to node 2, raises an error if no such edge exists

- has_node: O(1)
    - Return True if node exists within the graph, False otherwise

- neighbors: O(1)
    - Return a list of all nodes the passed node can reach. Raise an error if passed node is not present in graph.

- adjacent: O(1):
    - Return True if there is an edge connecting node 1 and node 2, False otherwise. Raise an error if either node is not present in graph.

- breadth_first_traversal: O(n)
    - Return a list containing elements in the graph, with ordering based on a breadth-first traversal, starting from the passed start value. Raises KeyError if starting value is not in graph.

- depth_first_traversal: O(n):
    - Return a list containing elements in the graph, with ordering based on a depth-first traversal, starting from the passed start value. Raises KeyError if starting value is not in graph.