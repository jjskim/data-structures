"""This is the test file for valid_parentheses.py."""

import pytest


def test_stack_constructor():
    """Test for the Stack constructor."""
    from stack import Stack
    s = Stack()
    assert isinstance(s, Stack)


def test_stack_construtor_passed_iterable():
    """Test the Stack constructor when passed an iterable."""
    from stack import Stack
    l1 = [1, 2, 3]
    s = Stack(l1)
    first = s.pop()
    second = s.pop()
    third = s.pop()
    l2 = [third, second, first]
    assert l2 == l1


def test_stack_push():
    """Test the push method of the Stack object."""
    from stack import Stack
    s = Stack()
    s.push("test")
    assert s.pop() == "test"


def test_stack_pop_returns_most_recently_pushed_value():
    """Test the pop method of the Stack object."""
    from stack import Stack
    s = Stack()
    s.push("test")
    s.push("second")
    assert s.pop() == "second"


def test_stack_len_returns_correct():
    """Test for correct length returned with len called on Stack."""
    from stack import Stack
    list1 = [1, 2, 3, 4, 5, 6]
    s = Stack(list1)
    assert len(s) == len(list1)


def test_stack_constructor_passed_non_iterable():
    """Test constructor raises exception when passed non iterable."""
    from stack import Stack
    with pytest.raises(TypeError):
        s = Stack(5)
