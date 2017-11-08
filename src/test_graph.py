"""This is the test file for graph.py."""

import pytest


@pytest.fixture
def empty_graph():
    """Fixture to return an empty graph."""
    from graph import Graph
    return Graph()


def test_graph_constructs_with_no_nodes(empty_graph):
    """Test to verify graph constructs with no nodes."""
    d = empty_graph
    assert d.nodes() == []


def test_graph_constructs_with_no_edges(empty_graph):
    """Test that graph has no edges upon inital construction."""
    d = empty_graph
    assert d.edges() == []


def test_nodes_correctly_returns_all_nodes_in_graph(empty_graph):
    """Test nodes returns list of all nodes in graph."""
    d = empty_graph
    d.add_node(1)
    d.add_node(2)
    assert sorted(d.nodes()) == [1, 2]


def test_nodes_correctly_returns_all_edges_in_graph(empty_graph):
    """Test that edges returns all edges in graph."""
    d = empty_graph
    d.add_node(1)
    d.add_node(2)
    d.add_node(3)
    d.add_edge(1, 2, 1)
    d.add_edge(1, 3, 1)
    d.add_edge(3, 2, 1)
    assert sorted(d.edges()) == [(1, 2), (1, 3), (3, 2)]


def test_add_node_correctly_adds_node_with_no_edges(empty_graph):
    """Test that add_node adds a single node with no edges."""
    d = empty_graph
    d.add_node(2)
    assert d.edges() == []


def test_add_already_existing_node_does_not_overwrite_nodes_edges(empty_graph):
    """Test add_node doesn't overwrite edges for node if already exists."""
    d = empty_graph
    d.add_node(1)
    d.add_node(3)
    d.add_edge(1, 3, 1)
    d.add_node(1)
    assert d.edges() == [(1, 3)]


def test_add_edge_adds_in_specified_direction(empty_graph):
    """Test that add_edge adds edge in specified direction."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    assert (2, 1) not in d.edges() and (1, 2) in d.edges()


def test_add_edge_adds_node_if_node_is_not_present(empty_graph):
    """Test that add_edge adds node to graph if it does not exist."""
    d = empty_graph
    d.add_node(1)
    d.add_edge(1, 2, 1)
    assert 2 in d.nodes()


def test_add_edge_adds_both_nodes_if_both_not_present(empty_graph):
    """Test that add_edge adds both nodes if neither exist."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    assert 2 in d.nodes() and 1 in d.nodes()


def test_del_node_deletes_node_from_graph(empty_graph):
    """Test that del_node deletes node from graph."""
    d = empty_graph
    d.add_node(1)
    d.del_node(1)
    assert d.nodes() == []


def test_del_node_raises_exception_if_passed_nonexistent_node(empty_graph):
    """Test del_node raises exception when passed illegal argument."""
    d = empty_graph
    with pytest.raises(ValueError):
        d.del_node("hahahawtfislife")


def test_del_node_removes_all_edges_leading_to_that_node(empty_graph):
    """Test that del_node also removes all edges leading to that node."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.del_node(2)
    assert d.edges() == []


def test_del_edge_removes_edge_in_correct_direction(empty_graph):
    """Test that del_edge removes edge in only the correct direction."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(2, 1, 1)
    d.del_edge(1, 2)
    assert d.edges() == [(2, 1)]


def test_del_edge_raises_keyerror_for_non_existent_val1(empty_graph):
    """Test that del_edge raises KeyError for nonexistent val1."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(2, 1, 1)
    with pytest.raises(KeyError):
        d.del_edge(3, 1)


def test_has_node_correctly_returns_true(empty_graph):
    """Test has_node returns True if node is present."""
    d = empty_graph
    d.add_node(1)
    assert d.has_node(1)


def test_has_node_correctly_returns_false_for_nonexistent_node(empty_graph):
    """Test has_node returns False if node is not present."""
    d = empty_graph
    assert not d.has_node("anything")


def test_neighbors_raises_exception_when_passed_nonexistent_node(empty_graph):
    """Test that neighbors raises exception when called on nonexistent node."""
    d = empty_graph
    with pytest.raises(ValueError):
        d.neighbors(2)


def test_neigbors_correctly_displays_edges_starting_passed_node(empty_graph):
    """Test that neighbors display nodes that can be reached by passed node."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(2, 1, 1)
    assert d.neighbors(1)


def test_adjacent_raises_exception_if_at_least_1_node_nonexistent(empty_graph):
    """Test adjacent raises exception if at least 1 node does not exist."""
    d = empty_graph
    with pytest.raises(ValueError):
        d.adjacent(1, 2)


def test_adjacent_returns_true_if_either_node_can_reach_other(empty_graph):
    """Test that adjacent returns true if either node can reach other."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    assert d.adjacent(2, 1)


def test_that_breadth_first_raises_error_with_empty_graph(empty_graph):
    """Raise a KeyError on a empty graph."""
    d = empty_graph
    with pytest.raises(KeyError):
        d.breadth_first_traversal(2)


def test_that_depth_first_raises_error_when_looking_empty_graph(empty_graph):
    """Raise KeyError on an empty graph."""
    d = empty_graph
    with pytest.raises(KeyError):
        d.depth_first_traversal(2)


def test_that_breadth_first_returns_proper_output(empty_graph):
    """Test that expected output is returned when ran."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(1, 3, 1)
    d.add_edge(2, 4, 1)
    d.add_edge(2, 5, 1)
    d.add_edge(4, 7, 1)
    d.add_edge(4, 8, 1)
    d.add_edge(5, 9, 1)
    d.add_edge(3, 6, 1)
    assert d.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_that_depth_first_returns_proper_output(empty_graph):
    """Test that expected output is returned when ran."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(1, 3, 1)
    d.add_edge(2, 4, 1)
    d.add_edge(2, 5, 1)
    d.add_edge(4, 7, 1)
    d.add_edge(4, 8, 1)
    d.add_edge(5, 9, 1)
    d.add_edge(3, 6, 1)
    assert d.depth_first_traversal(1) == [1, 2, 4, 7, 8, 5, 9, 3, 6]


def test_that_breadth_first_returns_proper_output_with_loop(empty_graph):
    """Test that expected output is returned when ran."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(1, 3, 1)
    d.add_edge(2, 4, 1)
    d.add_edge(2, 5, 1)
    d.add_edge(4, 7, 1)
    d.add_edge(4, 8, 1)
    d.add_edge(5, 9, 1)
    d.add_edge(3, 6, 1)
    d.add_edge(4, 3, 1)
    assert d.breadth_first_traversal(1) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_that_depth_first_returns_proper_output_with_loop(empty_graph):
    """Test that expected output is returned when ran."""
    d = empty_graph
    d.add_edge(1, 2, 1)
    d.add_edge(1, 3, 1)
    d.add_edge(2, 4, 1)
    d.add_edge(2, 5, 1)
    d.add_edge(4, 3, 1)
    d.add_edge(4, 7, 1)
    d.add_edge(4, 8, 1)
    d.add_edge(5, 9, 1)
    d.add_edge(3, 6, 1)
    assert d.depth_first_traversal(1) == [1, 2, 4, 7, 8, 5, 9, 3, 6]


def test_that_graph_will_not_take_non_int_weights(empty_graph):
    """Test that value error will be raised."""
    d = empty_graph
    with pytest.raises(ValueError):
        d.add_edge(1, 2, 'potato')
