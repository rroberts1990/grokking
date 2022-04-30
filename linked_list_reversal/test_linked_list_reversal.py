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
