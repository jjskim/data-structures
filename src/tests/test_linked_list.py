"""This is the test file for valid_parentheses.py."""

import pytest

# parameters = [
#     ("  (", False),
#     (")test", False),
#     ("", True),
#     ("hi())(", False),
#     ("hi(hi)()", True),
#     ("()()()(", False),
#     (")()()()()()", False),
#     ("()()()()()(())", True),
#     ("()()()((()))()(())()", True)
# ]


# @pytest.mark.parametrize('n, result', parameters)
# def test_valid_parentheses(n, result):
#     """Test for valid_parentheses function."""
#     from valid_parentheses import valid_parentheses
#     assert valid_parentheses(n) == result

def test_node_constructor():
    """Test for the Node constructor."""
    from linked_list import Node
    n = Node(1, None)
    assert n.data == 1 and n.next is None


def test_linked_list_has_head():
    """Test for existence of head in a linked list object."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.head is None


def test_linked_list_push_adds_new_item():
    """Test Linked List push method adds new item to head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    assert l.head.data == 'val'


def test_linked_list_push_two_last_value_is_head():
    """Test when adding two values, that last added value is new head."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.data == 'val2'


def test_linked_list_push_moves_old_head_to_new_head_next():
    """Test that push method moves old head to new heads . next."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('val')
    l.push('val2')
    assert l.head.next.data == 'val'


def test_linked_list_pop_removes_head_and_returns_value():
    """Test that pop removes head and returns its value."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    value = l.pop()
    assert value == 'potato'


def test_linked_list_pop_removes_head():
    """Test that pop removes the head of the linked list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.pop()
    assert l.head is None


def test_linked_list_pop_shifts_head_properly():
    """Test that the pop shifts values appropriately in list."""
    from linked_list import LinkedList
    l = LinkedList()
    l.push('potato')
    l.push('cabbage')
    l.pop()
    assert l.head.data == 'potato'


def test_linked_list_pop_empty_raises_exception():
    """Test that pop on an empty list raises an exception."""
    from linked_list import LinkedList
    l = LinkedList()
    with pytest.raises(IndexError):
        l.pop()


def test_linked_list_size_returns_zero_for_empty_list():
    """Test that the size of an empty list returns correctly as 0."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.size() == 0


@pytest.mark.parametrize('n', range(10))
def test_linked_list_size_returns_list_length(n):
    """Test that the size correctly returns for a list."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert l.size() == n


@pytest.mark.parametrize('n', range(10))
def test_linked_list_can_use_len_function(n):
    """Test that ."""
    from linked_list import LinkedList
    l = LinkedList()
    for i in range(n):
        l.push(i)
    assert len(l) == n


def test_linked_list_search_empty_returns_none():
    """Test that search for an empty list returns none."""
    from linked_list import LinkedList
    l = LinkedList()
    assert l.search(0) is None


@pytest.mark.parametrize('n', range(1, 10))
def test_linked_list_search_in_many_returns_proper_node(n):
    """Test that search for a list returns correct node."""
    from linked_list import LinkedList
    from random import randint
    l = LinkedList()
    for i in range(1, n + 1):
        l.push(i)
    search_me = randint(1, n)
    assert l.search(search_me).data == search_me


def test_linked_list_takes_iterable_and_has_values():
    """Test that the linked list constructor can accept an iterable."""
    from linked_list import LinkedList
    a_list = [5, 2, 9, 0, 1]
    l = LinkedList(a_list)
    for item in a_list:
        assert l.search(item).data == item


def test_remove():
    """."""
    assert True
