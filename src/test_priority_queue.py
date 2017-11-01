"""Test the functionality of the priority queue."""

import pytest


@pytest.fixture
def empty_prioque():
    """Create blank prioque for use in tests."""
    from priority_queue import PriorityQueue
    b = PriorityQueue()
    return b


def test_the_functionality_of_insert_into_priority_queue(empty_prioque):
    """Test that multiple items can be added and priority is properly established."""
    b = empty_prioque
    b.insert('fluff', 9000)
    b.insert('stuff', 20)
    b.insert('more', 20)
    b.insert('flerg', 30)
    b.insert('word', 200)
    assert b._queues == {200: ['word'], 30: ['flerg'], 20: ['more', 'stuff'], 9000: ['fluff']}


def test_that_empty_deque_is_made(empty_prioque):
    """Test that an empty prioque can be made."""
    b = empty_prioque
    assert b._queues == {}


def test_that_pop_removes_highest_priority(empty_prioque):
    """Test that item with the highest priority is removed."""
    b = empty_prioque
    b.insert('fluff', 9000)
    b.insert('stuff', 20)
    b.insert('more', 20)
    b.insert('flerg', 30)
    b.insert('word', 9000)
    assert b.pop() == 'fluff'


def test_that_peek_shows_item_with_highest_priority(empty_prioque):
    """Test that peek will displac item with highest priority."""
    b = empty_prioque
    b.insert('fluff', 9000)
    b.insert('stuff', 20)
    b.insert('more', 20)
    b.insert('flerg', 30)
    b.insert('word', 9000)
    assert b.peek() == 'fluff'


def test_that_peek_on_empty_list_returns_proper_error(empty_prioque):
    """Test for error being raised when peek attaempted on an empty prioque."""
    b = empty_prioque
    with pytest.raises(IndexError):
        b.peek()


def test_that_pop_on_empty_list_returns_proper_error(empty_prioque):
    """Test for error being raised when pop attempted on an empty prioque."""
    b = empty_prioque
    with pytest.raises(IndexError):
        b.pop()


def test_that_priority_queue_remains_operable_with_multiple_actions(empty_prioque):
    """Test that priority queue holds up under repetitive actions."""
    b = empty_prioque
    b.insert('fluff', 9000)
    b.insert('stuff', 20)
    b.insert('more', 20)
    b.insert('flerg', 30)
    b.insert('word', 9000)
    b.pop()
    b.insert('morestuff', 9000)
    b.pop()
    b.pop()
    assert b.peek() == 'flerg'


def test_peek_does_not_remove_item(empty_prioque):
    """Test that peek returns only the value, and does not remove the value."""
    b = empty_prioque
    b.insert('test')
    b.peek()
    assert b.pop() == 'test'


def test_peek_and_pop_return_the_same_value(empty_prioque):
    """Test that the value returned from pop and peek are both the same."""
    b = empty_prioque
    b.insert('test')
    assert b.peek() == b.pop()


def test_popping_last_item_removes_key_from_dictionary(empty_prioque):
    """Test that popping the last value makes the priority queue empty."""
    b = empty_prioque
    b.insert('test')
    b.pop()
    assert not b._queues


def test_pop_returns_item_with_most_seniority_if_both_have_same_priority(empty_prioque):
    """Test that pop returns not only the highest priority, but the most senior item."""
    b = empty_prioque
    b.insert('older', 2)
    b.insert('younger', 2)
    assert b.pop() == 'older'
