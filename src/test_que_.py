"""This is the test file for que_.py."""

import pytest


@pytest.fixture
def empty_queue():
    """Fixture to return an empty queue."""
    from que_ import Queue
    return Queue()


def test_queue_constructs_with_iterable():
    """."""
    from que_ import Queue
    a = Queue([1, 2])
    assert a.size() == len([1, 2])


def test_queue_constructs_empty_when_passed_no_arguments(empty_queue):
    """Test that an empty queue initializes."""
    q = empty_queue
    assert q.size() == 0


def test_queue_raises_exception_when_passed_non_iterable():
    """Test that passing a queue a noniterable raises an exception."""
    from que_ import Queue
    with pytest.raises(TypeError):
        Queue(5)


def test_dequeue_on_empty_queue_raises_exception(empty_queue):
    """Test that a call on dequeue on empty queue raises exception."""
    d = empty_queue
    with pytest.raises(IndexError):
        d.dequeue()


def test_enqueue_correctly_adds_item(empty_queue):
    """Test that enqueue correctly adds an item to the queue."""
    q = empty_queue
    prev_size = q.size()
    q.enqueue(5)
    assert q.size() == prev_size + 1


def test_enqueue_correctly_adds_item_and_can_be_dequeued(empty_queue):
    """Test that after enqueue, dequeue correctly removes the item."""
    q = empty_queue
    q.enqueue(5)
    assert q.dequeue() == 5


def test_deequeue_correctly_removes_item_in_front_of_queue(empty_queue):
    """Test that after more than 2 enqueues, dequeue removes first item."""
    q = empty_queue
    q.enqueue("first")
    q.enqueue("second")
    assert q.dequeue() == "first"


def test_peek_on_empty_queue_returns_none(empty_queue):
    """Test that peek on an empty queue returns none."""
    q = empty_queue
    assert q.peek() is None


def test_peek_on_queue_returns_value_at_front_of_queue(empty_queue):
    """Test that peek on a nonempty queue returns the front item."""
    q = empty_queue
    q.enqueue(5)
    q.enqueue(6)
    assert q.peek() == 5


def test_peek_does_not_remove_item_queue(empty_queue):
    """Test that peek only returns the value and does not modify queue."""
    q = empty_queue
    q.enqueue(1)
    q.enqueue(2)
    q.enqueue(3)
    q.peek()
    assert q.size() == 3
