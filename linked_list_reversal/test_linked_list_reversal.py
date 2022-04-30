import pytest

from linked_list_reversal.linked_list_reversal import ReverseLinkedList, Node

@pytest.fixture
def example_list_1():
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    return head

@pytest.fixture
def example_result_1():
    return "10->8->6->4->2->null"

def test_reverse_linked_list(example_list_1, example_result_1):
    solver = ReverseLinkedList()
    actual = solver.reverse_linked_list(example_list_1)
    print(actual.print_list())
    assert actual.print_list() == example_result_1

@pytest.fixture
def example_result_2():
    return "2->8->6->4->10->null"

def test_reverse_sub_list(example_list_1, example_result_2):
    p, q = 2, 4
    solver = ReverseLinkedList()
    actual = solver.reverse_sub_list(example_list_1, p, q)
    print(actual.print_list())
    assert actual.print_list() == example_result_2


@pytest.fixture
def example_list_2():
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)
    return head

@pytest.fixture
def example_result_3():
    return "3->2->1->6->5->4->8->7->null"

def test_reverse_every_k_sublist(example_list_2, example_result_3):
    k = 3
    solver = ReverseLinkedList()
    actual = solver.reverse_every_k_sublist(example_list_2, k)
    print(actual.print_list())
    assert actual.print_list() == example_result_3
