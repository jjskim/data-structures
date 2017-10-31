"""Test the functionality of the heap."""

import pytest


@pytest.fixture
def empty_heap():
    """Fixture to return an empty heap."""
    from binheap import BinaryHeap
    return BinaryHeap()


def test_that_push_adds_items_and_orders_bin_properls(empty_heap):
    """Test that push adds items properly."""
    b = empty_heap
    b.push(10)
    b.push(17)
    b.push(30)
    b.push(15)
    assert b._list == [None, 10, 15, 30, 17]


def test_that_pop_removes_top_of_heap_and_orders_it_properly(empty_heap):
    """Test that pop will remove and order heap properly."""
    b = empty_heap
    b.push(10)
    b.push(17)
    b.push(30)
    b.push(15)
    b.pop()
    assert b._list == [None, 15, 17, 30]


def test_that_heap_can_be_created_with_iterable():
    """Test that a heap can be created with an iterable."""
    from binheap import BinaryHeap
    b = BinaryHeap([1, 2, 6, 9, 3])
    assert b._list == [None, 1, 2, 6, 9, 3]


def test_that_heap_when_passed_non_iterable_raises_error():
    """Test that uppon creation of a heap with a none iterable raises a TypeError."""
    from binheap import BinaryHeap
    with pytest.raises(TypeError):
        b = BinaryHeap(5)


def test_that_pop_from_empty_heap_raises_indexerror(empty_heap):
    """Test that pop from an empty heap will raise an index error."""
    b = empty_heap
    with pytest.raises(IndexError):
        b.pop()


def test_that_percolate_down_selects_target_right(empty_heap):
    """Test that percolate down will organize the heap in accordance with top down method."""
    b = empty_heap
    b.push(10)
    b.push(20)
    b.push(17)
    b.pop()
    assert b._list == [None, 17, 20]


def test_that_push_adds_value_to_middle_of_heap(empty_heap):
    """Test that when given a value that belongs further up in the heap that it is shifted up in the hierarchy."""
    b = empty_heap
    b.push(10)
    b.push(20)
    b.push(17)
    b.push(11)
    assert b._list == [None, 10, 11, 17, 20]
