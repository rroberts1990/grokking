from tree_breadth_first_search.tree_breadth_first_search import TreeBreadthFirstSearch, TreeNode
import pytest

@pytest.fixture
def example_tree_1():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    return root

@pytest.fixture
def expected_1():
    return [[12], [7, 1], [9, 10, 5]]

def test_level_order_traversal(example_tree_1, expected_1):
    expected = expected_1
    solver = TreeBreadthFirstSearch()
    actual = solver.level_order_traversal(example_tree_1)
    assert actual == expected

@pytest.fixture
def expected_2():
    return [[9, 10, 5], [7, 1], [12]]

def test_reverse_level_order_traversal(example_tree_1, expected_2):
    solver = TreeBreadthFirstSearch()
    actual = solver.reverse_level_order_traversal(example_tree_1)
    assert actual == expected_2

@pytest.fixture
def example_tree_2():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    return root

@pytest.fixture
def expected_3():
    return [[12], [1, 7], [9, 10, 5], [17, 20]]

def test_zig_zag_reversal(example_tree_2, expected_3):
    solver = TreeBreadthFirstSearch()
    actual = solver.zig_zag_traversal(example_tree_2)
    assert actual == expected_3

@pytest.fixture
def expected_4():
    return [12.0, 4.0, 8.0, 18.5]

def test_level_averages(example_tree_2, expected_4):
    solver = TreeBreadthFirstSearch()
    actual = solver.level_averages(example_tree_2)
    assert actual == expected_4


@pytest.fixture
def example_tree_3():
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    return root

def test_minimum_depth(example_tree_3):
    expected = 2
    solver = TreeBreadthFirstSearch()
    actual = solver.minimum_depth(example_tree_3)
    assert actual == expected


def test_level_order_successor(example_tree_1):
    given_node = 9
    expected_node = TreeNode(10)
    solver = TreeBreadthFirstSearch()
    actual = solver.level_order_successor(example_tree_1, given_node)
    assert actual == expected_node


def test_connect_level_order_siblings(example_tree_1):
    solver = TreeBreadthFirstSearch()
    actual = solver.connect_level_order_siblings(example_tree_1)
    assert actual == exp