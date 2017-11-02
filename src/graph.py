"""Module to define an unweighted, directed graph."""


class Graph(object):
    """Define an unweighted, directed graph class."""

    def __init__(self):
        """Construct a single instance of unweighted, directed graph."""
        self._edges = {}

    def nodes(self):
        """Return a list of nodes in the graph."""
        return self._edges.keys()

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
        """Add a directed edge to the graph, from node 1 to node 2."""
        self._edges.setdefault(val1, [])
        self._edges.setdefault(val2, [])
        self._edges[val1].append(val2)

    def del_edge(self, val1, val2):
        """Delete the directed edge from the graph."""
        try:
            self._edges[val1].remove(val2)
        except ValueError:
            raise ValueError('No existing edge between nodes.')

    def del_node(self, val):
        """Delete the node from the graph."""
        try:
            self._edges.pop(val, None)
            for node in self._edges.keys():
                if val in self._edges[node]:
                    self.del_edge(node, val)
        except ValueError:
            raise ValueError('Node does not exist.')

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
        Return a boolean if there exists an edge connecting passed nodes.
        Raise a ValueError if either of passed nodes do not exist in graph.
        """
        if not self.has_node(val1) or not self.has_node(val2):
            raise ValueError('At least one node not present in graph.')
        else:
            return val2 in self.neighbors(val1) or val1 in self.neighbors(val2)
