"""Module to define an unweighted, directed graph."""


class Graph(object):
    """Define an unweighted, directed graph class."""

    def __init__(self):
        """Construct a single instance of unweighted, directed graph."""
        self._edges = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return list(self._edges.keys())

    def edges(self):
        """Return a list of all directed edges in the graph as tuples."""
        all_edges = []
        for item in self._edges.keys():
            for edge in self._edges[item]:
                all_edges.append((item, edge))
        return all_edges

    def add_node(self, val):
        """Add a node to the graph."""
        self._edges.setdefault(val, [])

    def add_edge(self, val1, val2):
        """
        Add a directed edge to the graph, from node 1 to node 2.
        If edge already exists, overwrites it.
        """
        self.add_node(val1)
        self.add_node(val2)
        try:
            self.del_edge(val1, val2)
        except ValueError:
            pass
        self._edges[val1].append(val2)

    def del_edge(self, val1, val2):
        """Delete the directed edge from the graph."""
        try:
            self._edges[val1].remove(val2)
        except KeyError:
            raise KeyError(str(val1) + ' not present in graph')
        except ValueError:
            raise ValueError('No existing edge between nodes.')

    def del_node(self, val):
        """Delete the node from the graph."""
        if val not in self._edges:
            raise ValueError('Node does not exist.')
        self._edges.pop(val, None)
        for node in self._edges.keys():
            if val in self._edges[node]:
                self.del_edge(node, val)

    def has_node(self, val):
        """Return boolean if passed node is in graph."""
        return val in self._edges

    def neighbors(self, val):
        """
        Return a list of all directed edges starting from passed node.
        Raise a ValueError if passed node does not exist in graph.
        """
        if self.has_node(val):
            return self._edges[val]
        raise ValueError('Node does not exist.')

    def adjacent(self, val1, val2):
        """
        Return a boolean if there exists a directed edge from val1 to val2.
        Raise a ValueError if either of passed nodes do not exist in graph.
        """
        if not self.has_node(val1) or not self.has_node(val2):
            raise ValueError('At least one node not present in graph.')
        else:
            return val2 in self.neighbors(val1) or val1 in self.neighbors(val2)

    def breadth_first_traversal(self, start_val):
        """
        Return a list containing elements in the graph, with ordering based on
        a breadth-first traversal, starting from the passed start value.

        """
        if start_val not in self._edges:
            raise KeyError(str(start_val) + " does not exist")
        visited = set()
        breadth_queue = [start_val]
        bft = []
        while len(breadth_queue) > 0:
            item = breadth_queue.pop(0)
            if item not in visited:
                visited.add(item)
                bft.append(item)
                breadth_queue += self._edges[item]
        return bft

    def depth_first_traversal(self, start_val):
        """
        Return a list containing elements in the graph, with ordering based on
        a depth-first traversal, starting from the passed start value.

        """
        if start_val not in self._edges:
            raise KeyError(str(start_val) + " does not exist")
        visited = set()
        visited.add(start_val)
        depth_stack = [start_val]
        dft = []
        while len(depth_stack) > 0:
            item = depth_stack.pop()
            dft.append(item)
            for neighbor in reversed(self._edges[item]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    depth_stack.append(neighbor)
        return dft