"""This is the test file for deque.py."""

import pytest


@pytest.fixture
def empty_deque():
    """Fixture to return an empty deque."""
    from deque import Deque
    return Deque()


def test_deque_constructs_with_iterable():
    """Test that deque constructs correctly when passed an iterable."""
    from deque import Deque
    a = Deque([1, 2])
    assert a.size() == len([1, 2])


def test_deque_constructs_empty_when_passed_no_arguments(empty_deque):
    """Test that an empty deque initializes with size 0."""
    q = empty_deque
    assert q.size() == 0


def test_deque_raises_exception_when_passed_non_iterable():
    """Test that passing a deque a noniterable raises an exception."""
    from deque import Deque
    with pytest.raises(TypeError):
        Deque(5)


def test_popleft_on_empty_deque_raises_exception(empty_deque):
    """Test that a call on dequeue on empty queue raises exception."""
    d = empty_deque
    with pytest.raises(IndexError):
        d.popleft()


def test_append_correctly_adds_item(empty_deque):
    """Test that append correctly adds an item to the end of the deque."""
    q = empty_deque
    prev_size = q.size()
    q.append(5)
    assert q.size() == prev_size + 1


def test_append_correctly_adds_item_and_can_be_popleft(empty_deque):
    """Test that after append, popleft correctly removes the item."""
    q = empty_deque
    q.append(5)
    assert q.popleft() == 5


def test_append_correctly_adds_item_and_can_be_pop(empty_deque):
    """Test that after append, pop correctly removes the item."""
    q = empty_deque
    q.append(5)
    assert q.pop() == 5


def test_popleft_correctly_removes_item_in_front_of_deque(empty_deque):
    """Test that after 2 or more appends, popleft removes first item."""
    q = empty_deque
    q.append("first")
    q.append("second")
    assert q.popleft() == "first"


def test_pop_correctly_removes_item_in_back_of_deque(empty_deque):
    """Test that after 2 or more appends, pop removes last item."""
    q = empty_deque
    q.append("first")
    q.append("second")
    assert q.pop() == "second"


def test_peek_on_empty_deque_returns_none(empty_deque):
    """Test that peek on an empty deque returns none."""
    q = empty_deque
    assert q.peek() is None


def test_peek_on_deque_returns_value_at_end_of_queue(empty_deque):
    """Test that peek on a nonempty deque returns the value of last item."""
    q = empty_deque
    q.append(5)
    q.append(6)
    assert q.peek() == 6


def test_peekleft_on_deque_returns_value_at_front_of_queue(empty_deque):
    """Test that peekleft on a nonempty deque returns value of first item."""
    q = empty_deque
    q.append(5)
    q.append(6)
    assert q.peekleft() == 5


def test_peek_does_not_remove_item_deque(empty_deque):
    """Test that peek only returns the value and does not modify deque."""
    q = empty_deque
    q.append(1)
    q.append(2)
    q.append(3)
    size_before_peek = q.size()
    q.peek()
    assert q.size() == size_before_peek


def test_peekleft_does_not_remove_item_deque(empty_deque):
    """Test that peek only returns the value and does not modify deque."""
    q = empty_deque
    q.append(1)
    q.append(2)
    q.append(3)
    size_before_peekleft = q.size()
    q.peek()
    assert q.size() == size_before_peekleft


def test_appendleft_adds_item_to_front_of_deque(empty_deque):
    """Test that appendleft adds the item to the front of the deque."""
    q = empty_deque
    q.appendleft(2)
    q.append(3)
    q.appendleft(4)
    assert q.peekleft() == 4


def test_pop_on_empty_deque_raises_exception(empty_deque):
    """Test that a call on dequeue on empty queue raises exception."""
    d = empty_deque
    with pytest.raises(IndexError):
        d.pop()


def test_peek_left_on_empty_deque_returns_none(empty_deque):
    """Test that a peekleft on an empty deque returns None."""
    d = empty_deque
    assert d.peek() is None


def test_appendleft_then_pop_returns_value_at_front(empty_deque):
    """Test that pop returns the value at front after appendleft."""
    d = empty_deque
    d.appendleft(1)
    assert d.pop() == 1


def test_append_then_popleft_returns_value_at_end(empty_deque):
    """Test that pop returns the value at front after appendleft."""
    d = empty_deque
    d.append(1)
    assert d.popleft() == 1
