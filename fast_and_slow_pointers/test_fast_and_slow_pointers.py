import pytest
from fast_and_slow_pointers.fast_and_slow_pointers import FastSlowPointers, Node


@pytest.fixture
def example_linked_list():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    return head

@pytest.fixture
def example_linked_list_cycle(example_linked_list):
    head = example_linked_list
    head.next.next.next.next.next.next = head.next.next
    return head

def test_linked_list_no_cycle(example_linked_list):
    solver = FastSlowPointers()
    actual = solver.linked_list_cycle(example_linked_list)
    assert actual == False

def test_linked_list_cycle(example_linked_list_cycle):
    solver = FastSlowPointers()
    actual = solver.linked_list_cycle(example_linked_list_cycle)
    assert actual == True


@pytest.mark.parametrize('input, expected', [
    (23, True),
    (12, False)
])
def test_happy_number(input, expected):
    solver = FastSlowPointers()
    actual = solver.happy_number(input)
    assert actual == expected

@pytest.fixture
def example_middle_list1():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    return head

@pytest.fixture
def example_middle_list2(example_middle_list1):
    head = example_middle_list1
    head.next.next.next.next.next = Node(6)
    return head

@pytest.fixture
def example_middle_list3(example_middle_list2):
    head = example_middle_list2
    head.next.next.next.next.next.next = Node(7)
    return head


def test_linked_list_middle1(example_middle_list1):
    solver = FastSlowPointers()
    actual = solver.linked_list_middle(example_middle_list1)
    assert actual == 3

def test_linked_list_middle2(example_middle_list2):
    solver = FastSlowPointers()
    actual = solver.linked_list_middle(example_middle_list2)
    assert actual == 4

def test_linked_list_middle3(example_middle_list3):
    solver = FastSlowPointers()
    actual = solver.linked_list_middle(example_middle_list3)
    assert actual == 4


@pytest.fixture
def example_palindrome_linked_list():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(9)
    head.next.next.next.next = Node(3)
    head.next.next.next.next.next = Node(7)
    return head

def test_palindromic_linked_list(example_palindrome_linked_list):
    solver = FastSlowPointers()
    actual = solver.palindrome_linked_list(example_palindrome_linked_list)
    assert actual == True

def test_rearrange_linked_list(example_palindrome_linked_list):
    solver = FastSlowPointers()
    actual = solver.rearrange_linked_list(example_palindrome_linked_list)
    str_rep = ""
    print(actual.value)
    while actual is not None and actual.next is not None:
        str_rep += f"{actual.value} -> "
        actual = actual.next
    print(str_rep)
