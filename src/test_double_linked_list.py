"""This is the test file for double_linked_list.py."""

import pytest


@pytest.fixture
def empty_dll():
    """Fixture to return an empty doubly linked list."""
    from double_linked_list import DoublyLinkedList
    d = DoublyLinkedList()
    return d


def test_double_node_constructs_data_none():
    """Test to verify Doubly Linked Node data on consturction."""
    from double_linked_list import DoublyLinkedNode
    d = DoublyLinkedNode()
    assert d.data is None


def test_double_node_constructs_next_none():
    """Test to verify Doubly Linked Node next on construction."""
    from double_linked_list import DoublyLinkedNode
    d = DoublyLinkedNode()
    assert d.next is None


def test_double_node_constructs_prev_none():
    """Test to verify Doubly Linked Node prev on consturction."""
    from double_linked_list import DoublyLinkedNode
    d = DoublyLinkedNode()
    assert d.prev is None


def test_double_node_constructs_correctly():
    """Test to verify Doubly Linked Node object consturction."""
    from double_linked_list import DoublyLinkedNode
    d = DoublyLinkedNode(None, 5, None)
    assert d.data == 5


def test_dll_constructs_when_passed_iterable():
    """Test to verify Doubly Linked List constructs when passed iterable."""
    from double_linked_list import DoublyLinkedList
    d = DoublyLinkedList("Test")
    assert len(d) == 4


def test_dll_constructs_empty_none_head(empty_dll):
    """Test that empty dll is created with head of None."""
    d = empty_dll
    assert d.head is None


def test_dll_constructs_empty_none_tail(empty_dll):
    """Test that empty dll is created with tail of None."""
    d = empty_dll
    assert d.tail is None


def test_dll_push_on_empty_list_correctly_updates_head(empty_dll):
    """Test that push on an empty dll updates head correctly."""
    d = empty_dll
    d.push(2)
    assert d.head.data == 2


def test_dll_push_on_empty_list_correctly_updates_tail(empty_dll):
    """Test that push on an empty dll updates tail correctly."""
    d = empty_dll
    d.push(2)
    assert d.tail.data == 2


def test_dll_push_on_nonempty_list_correctly_updates_head(empty_dll):
    """Test that push on a nonempty dll updates head correctly."""
    d = empty_dll
    d.push(2)
    d.push(3)
    assert d.head.data == 3


def test_dll_push_on_nonempty_list_correctly_updates_tail(empty_dll):
    """Test that push on a nonempty dll updates tail correctly."""
    d = empty_dll
    d.push(2)
    d.push(3)
    assert d.tail.data == 2


def test_dll_append_on_empty_list_correctly_updates_head(empty_dll):
    """Test that append on an empty dll updates head correctly."""
    d = empty_dll
    d.append(2)
    assert d.head.data == 2


def test_dll_append_on_empty_list_correctly_updates_tail(empty_dll):
    """Test that append on an empty dll updates tail correctly."""
    d = empty_dll
    d.append(2)
    assert d.tail.data == 2


def test_dll_append_on_nonempty_list_correctly_updates_head(empty_dll):
    """Test that append on a nonempty dll updates head correctly."""
    d = empty_dll
    d.append(2)
    d.append(3)
    assert d.head.data == 2


def test_dll_append_on_nonempty_list_correctly_updates_tail(empty_dll):
    """Test that append on a nonempty dll updates tail correctly."""
    d = empty_dll
    d.append(2)
    d.append(3)
    assert d.tail.data == 3


def test_dll_pop_on_empty_raises_index_error(empty_dll):
    """Test that pop on an empty dll raises an index error."""
    d = empty_dll
    with pytest.raises(IndexError):
        d.pop()


def test_dll_shift_on_empty_raises_index_error(empty_dll):
    """Test that shift on an empty dll raises an index error."""
    d = empty_dll
    with pytest.raises(IndexError):
        d.shift()


def test_dll_pop_on_nonempty_returns_correct(empty_dll):
    """Test that shift on a nonempty dll returns the tail value."""
    d = empty_dll
    d.push(1)
    d.push(2)
    expected = d.head.data
    assert d.pop() == expected


def test_dll_shift_on_nonempty_returns_correct(empty_dll):
    """Test that shift on a nonempty dll returns the tail value."""
    d = empty_dll
    d.append(1)
    d.append(2)
    expected = d.tail.data
    assert d.shift() == expected


def test_dll_remove_raises_value_exception(empty_dll):
    """Test that remove when passed a non existent value raises exception."""
    d = empty_dll
    d.append(2)
    with pytest.raises(ValueError):
        d.remove(3)


def test_dll_remove_correctly_removes_head(empty_dll):
    """Test that remove correctly removes head value."""
    d = empty_dll
    d.push(2)
    d.remove(2)
    assert d.head is None


def test_dll_remove_correctly_removes_tail(empty_dll):
    """Test that remove correctly removes tail value."""
    d = empty_dll
    d.append(2)
    d.append(3)
    d.remove(3)
    assert d.tail.data == 2


def test_dll_removes_node_in_middle_of_list(empty_dll):
    """Test that remove correctly removes value in middle of list."""
    d = empty_dll
    d.append(1)
    d.append(2)
    d.append(3)
    d.remove(2)
    assert d.head.data == 1
