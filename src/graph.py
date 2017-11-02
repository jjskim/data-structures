"""."""


class Graph(object):
    """."""

    def __init__(self):
        """."""
        self._edges = {}

    def nodes(self):
        """."""
        return self._edges.keys()

    def edges(self):
        """."""
        all_edges = []
        for item in self._edges.keys():
            for edge in self._edges[item]:
                all_edges.append((item, edge))
        return all_edges

    def add_node(self, val):
        """."""
        self._edges.setdefault(val, [])

    def add_edge(self, val1, val2):
        """."""
        self._edges.setdefault(val1, [])
        self._edges.setdefault(val2, [])
        self._edges[val1].append(val2)

    def del_edge(self, val1, val2):
        """."""
        try:
            self._edges[val1].remove(val2)
        except ValueError:
            raise ValueError('No existing edge between nodes.')

    def del_node(self, val):
        """."""
        try:
            self._edges.pop(val, None)
            for node in self._edges.keys():
                if val in self._edges[node]:
                    self.del_edge(node, val)
        except ValueError:
            raise ValueError('Node does not exist.')

    def has_node(self, val):
        """."""
        return val in self._edges

    def neighbors(self, val):
        """."""
        if self.has_node(val):
            return self._edges[val]
        raise ValueError('Node does not exist.')

    def adjacent(self, val1, val2):
        """."""
        if not self.has_node(val1):
            raise ValueError('Node value1 not present in graph.')
        elif not self.has_node(val2):
            raise ValueError('Node value2 not present in graph')
        else:
            return val2 in self.neighbors(val1)
